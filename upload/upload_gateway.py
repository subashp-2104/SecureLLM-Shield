import os
import sys
import uuid
import time
import mimetypes
from typing import Dict, Any, Tuple

# Configuration Settings
UPLOAD_BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "uploads")
ORIGINAL_DIR = os.path.join(UPLOAD_BASE_DIR, "original")
SANITIZED_DIR = os.path.join(UPLOAD_BASE_DIR, "sanitized")
TEMP_DIR = os.path.join(UPLOAD_BASE_DIR, "temp")

MAX_FILE_SIZE = 25 * 1024 * 1024  # 25 MB

ALLOWED_EXTENSIONS = {
    'image': {'png', 'jpg', 'jpeg', 'webp'},
    'pdf': {'pdf'},
    'docx': {'docx'},
    'video': {'mp4', 'mov', 'avi', 'mkv'}
}

ALL_ALLOWED_EXTENSIONS = set().union(*ALLOWED_EXTENSIONS.values())

# Ensure directories exist
for d in [ORIGINAL_DIR, SANITIZED_DIR, TEMP_DIR]:
    os.makedirs(d, exist_ok=True)

def get_file_category(extension: str) -> str:
    ext = extension.lower().strip('.')
    for category, ext_set in ALLOWED_EXTENSIONS.items():
        if ext in ext_set:
            return category
    return 'unknown'

def validate_uploaded_file(file_obj, filename: str) -> Tuple[bool, str, Dict[str, Any]]:
    if not filename or '.' not in filename:
        return False, "Invalid filename: missing extension.", {}
    
    ext = filename.rsplit('.', 1)[1].lower()
    if ext not in ALL_ALLOWED_EXTENSIONS:
        return False, f"Unsupported file extension '.{ext}'. Supported: {', '.join(sorted(ALL_ALLOWED_EXTENSIONS))}", {}
    
    # Check file size
    file_obj.seek(0, os.SEEK_END)
    file_size = file_obj.tell()
    file_obj.seek(0)
    
    if file_size <= 0:
        return False, "File is empty (0 bytes).", {}
    
    if file_size > MAX_FILE_SIZE:
        return False, f"File size ({file_size / (1024*1024):.1f}MB) exceeds maximum limit of 25MB.", {}
    
    # Magic bytes check for security
    header = file_obj.read(16)
    file_obj.seek(0)
    
    category = get_file_category(ext)
    
    # Generate safe server-side random filename
    file_id = str(uuid.uuid4())
    safe_filename = f"{file_id}_{int(time.time())}.{ext}"
    saved_original_path = os.path.join(ORIGINAL_DIR, safe_filename)
    
    # Save original file securely
    file_obj.save(saved_original_path)
    
    metadata = {
        "file_id": file_id,
        "original_filename": filename,
        "safe_filename": safe_filename,
        "extension": ext,
        "category": category,
        "size_bytes": file_size,
        "size_formatted": f"{file_size / 1024:.1f} KB" if file_size < 1024*1024 else f"{file_size / (1024*1024):.1f} MB",
        "original_path": saved_original_path,
        "sanitized_filename": f"sanitized_{safe_filename}",
        "sanitized_path": os.path.join(SANITIZED_DIR, f"sanitized_{safe_filename}"),
        "upload_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return True, "File uploaded and validated successfully.", metadata

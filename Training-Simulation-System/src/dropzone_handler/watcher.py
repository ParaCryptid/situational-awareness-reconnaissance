
import os
import time
from gpg_encryption import gpg_handler

DROPZONE_DIR = "/opt/training-system/dropzone"
ENCRYPTED_LOG = "/opt/training-system/logs/dropzone_cid.log"

def ensure_dirs():
    os.makedirs(DROPZONE_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(ENCRYPTED_LOG), exist_ok=True)

def watch_dropzone():
    print("[DROPZONE] Monitoring for new files...")
    known_files = set(os.listdir(DROPZONE_DIR))
    while True:
        time.sleep(3)
        current_files = set(os.listdir(DROPZONE_DIR))
        new_files = current_files - known_files
        for filename in new_files:
            full_path = os.path.join(DROPZONE_DIR, filename)
            if os.path.isfile(full_path):
                print(f"[DROPZONE] New file detected: {filename}")
                encrypted = gpg_handler.encrypt_file(full_path)
                if encrypted:
                    with open(ENCRYPTED_LOG, 'a') as log:
                        log.write(f"{filename} -> {encrypted}\n")
                    os.remove(full_path)
        known_files = current_files

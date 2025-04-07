
import subprocess
import os

GPG_KEY_ID = "E6B95286AC6227141B449C26D7B417D8E92A829E"

def encrypt_file(filepath):
    encrypted_path = f"{filepath}.gpg"
    try:
        subprocess.run([
            "gpg", "--yes", "--batch", "--output", encrypted_path,
            "--encrypt", "--recipient", GPG_KEY_ID, filepath
        ], check=True)
        return encrypted_path
    except subprocess.CalledProcessError:
        print(f"[GPG] Encryption failed for: {filepath}")
        return None

def decrypt_file(encrypted_path, output_path=None):
    if not output_path:
        output_path = encrypted_path.replace(".gpg", "")
    try:
        subprocess.run([
            "gpg", "--yes", "--batch", "--output", output_path,
            "--decrypt", encrypted_path
        ], check=True)
        return output_path
    except subprocess.CalledProcessError:
        print(f"[GPG] Decryption failed for: {encrypted_path}")
        return None

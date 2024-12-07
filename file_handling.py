import os
import hashlib

def split_file(filePath, chunkSize):
    """Read a file in chunks."""
    with open(filePath, 'rb') as file:
        while True:
            chunk = file.read(chunkSize)
            if not chunk:
                break
            yield chunk

def save_file(filePath, chunks):
    """Write chunks of data into a file."""
    with open(filePath, 'wb') as file:
        for chunk in chunks:
            file.write(chunk)

def get_checksum(file_path):
    """Calculate the MD5 checksum."""
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

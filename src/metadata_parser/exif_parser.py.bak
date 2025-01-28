
import exiftool

def extract_metadata(file_path):
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata(file_path)
    return metadata

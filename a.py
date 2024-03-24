# Recover the file name extension from the given path, and return it as a string.
# Files are photo and video without any extension.
# Example:
# MGYM6489 -> heic
import os
import tqdm


def get_extension(path: str) -> str:
    # Read 8 bytes from the file
    with open(path, "rb") as f:
        header = f.read(16)

    if header[4:12] == b"ftypheic":
        return "HEIC"
    if header[4:10] == b"ftypqt":
        return "MOV"
    if header[4:8] == b"wide":
        return "MOV"
    if header[4:12] == b"ftypisom":
        return "MOV"
    if header[1:4] == b"PNG":
        return "PNG"
    if header[6:10] == b"JFIF":
        return "JPG"
    if header[6:10] == b"Exif":
        return "JPG"
    if header[4:12] == b"ftypmp42":
        return "MP4"
    if header[4:12] == b"ftypiso5":
        return "MP4"
    if header == b'<?xml version="1':
        return "AAE"
    if header[8:] == b"APPLEDNG":
        return "DNG"

    return ""


path = "/Volumes/Hesoyam Personal/My Pjoto"

# Get all folders in the path
folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
# Get all files in the folder
# tqdm is used to show the progress bar
files = []
for folder in folders:
    for file in os.listdir(os.path.join(path, folder)):
        files.append(os.path.join(path, folder, file))

for file in tqdm.tqdm(files):
    # Check if the file does not have an extension
    if "." in file:
        continue
    # Get the extension
    extension = get_extension(os.path.join(path, folder, file))
    # Rename the file
    if extension != "":
        os.rename(
            os.path.join(path, folder, file),
            os.path.join(path, folder, file + "." + extension),
        )

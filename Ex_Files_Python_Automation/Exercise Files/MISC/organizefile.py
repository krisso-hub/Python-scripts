import os
from pathlib import Path
SUBDIRECTORIES = {
"Documents" : [".pdf", ".rtf", ".txt"],
"Audio" : [".mp3", ".m4a", ".m4b"],
"Videos" : [".mov", ".mp4", ".avi"],
"Images" : [".jpg", ".jpeg", ".png"]
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "MISC"
print(pickDirectory(".pdf"))

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
organizeDirectory()
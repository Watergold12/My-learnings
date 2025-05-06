import os
import pathlib

list_of_directories = {
    "Picture_Folder": [".jpeg", ".jpg", ".gif", ".png"],
    "Video_Folder": [".wmv", ".mov", ".mp4", ".mpg", ".mpeg", ".mkv"],
    "Zip_Folder": [".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".zip"],
    "Music_folder": [".mp3", ".msv", ".wav", ".wma"],
    "PDF_Folder": [".pdf"],
    "Doc_Folder": [".docx", ".docm", "doc", "txt"],
    "Python_Folder" : [".py", ".python"]
}

File_Format_Dictionary = {
    final_file_format: directory
    for directory, file_format_stored in list_of_directories.items()
    for final_file_format in file_format_stored
}

def organizer():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = pathlib.Path(entry)
        final_file_format = file_path.suffix.lower()
        if final_file_format in File_Format_Dictionary:
            directory_path = pathlib.Path(File_Format_Dictionary[final_file_format])
            os.makedirs(directory_path, exist_ok=True)
            os.rename(file_path, directory_path.joinpath(file_path.name))

try:
    os.mkdir("Other_Folder")
except (FileExistsError, OSError):
    print("Failed to create new directory")

for dir in os.scandir():
    try:
        if dir.is_dir():
            dir_path = pathlib.Path(dir)
            os.rmdir(dir_path)
        else:
            file_path = pathlib.Path(dir)
            os.rename(file_path, pathlib.Path("Other_Folder").joinpath(file_path.name))
    except (FileExistsError, OSError):
        print("Failed to create new directory called Other Folder. File directory may already exist")

if __name__ == "__main__":
    organizer()
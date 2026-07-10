import os
import string
from pathlib import Path


SKIP_FOLDERS = {
    "$Recycle.Bin",
    "$SysReset",
    "$WinREAgent",
    "AppData",
    "Application Data",
    "Config.Msi",
    "Documents and Settings",
    "Intel",
    "MSOCache",
    "OneDriveTemp",
    "PerfLogs",
    "Program Files",
    "Program Files (x86)",
    "ProgramData",
    "Recovery",
    "System Volume Information",
    "Temp",
    "Windows",
    "Windows.old",
}


def get_drives():
    drives = []
    for letter in string.ascii_uppercase:
        drive = f"{letter}:\\"
        if os.path.exists(drive):
            drives.append(drive)
    return drives


def search_files(search_name, roots):
    matches = []
    search_name = search_name.lower()

    for root in roots:
        for folder_path, folder_names, file_names in os.walk(root):
            folder_names[:] = [
                folder_name
                for folder_name in folder_names
                if folder_name not in SKIP_FOLDERS
            ]

            for file_name in file_names:
                if search_name == file_name.lower():
                    full_path = Path(folder_path) / file_name
                    matches.append(full_path)

    return matches


def main():
    search_name = input("Enter the file name to search for: ").strip()

    if not search_name:
        print("Please enter a file name.")
        return

    roots = get_drives()

    if not roots:
        print("No drives found.")
        return

    print("Searching... this may take a while.")

    matches = search_files(search_name, roots)

    if not matches:
        print("No file(s) found.")
        return

    print(f"\nFound {len(matches)} file(s):\n")

    for i, path in enumerate(matches, start=1):
        print(f"{i}. Name: {path.name}")
        print(f"   Path: {path}")
        print(f"   Folder: {path.parent}\n")


if __name__ == "__main__":
    main()

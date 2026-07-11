# Python File Search

A simple Windows file search script that scans available drive roots and prints matching files.

## Requirements

- Python 3
- Windows

## How to Run

Open a terminal in this project folder and run:

```powershell
python Search.py
```

If `python` is not recognized, try:

```powershell
py Search.py
```

## How to Use

1. Run the script.
2. Enter the exact file name you want to find.
3. Wait while it searches your drives.
4. Review the results that are printed to the terminal.

## What It Does

- Searches all available drive letters on Windows.
- Matches file names exactly, case-insensitive.
- Skips common large folders to improve speed.

## Notes

- If you press Enter without typing a file name, the script will ask you to enter one.
- If no drives are found, the script will exit.
- Search speed depends on how many files are on your machine.

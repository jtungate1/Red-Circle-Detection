from pathlib import Path
from RefinedRedCircles import detect_red_circles as detect
import shutil

# Specify the directory path
directory_path = Path("images/")
destination_path = Path("detected_circles/")

# Loop through items and filter for files only
for file_path in directory_path.iterdir():
    if detect(file_path):
        print(f"Red circles detected in: {file_path.name}")
        # Move the file to the destination directory
        shutil.copy(file_path, destination_path / file_path.name)



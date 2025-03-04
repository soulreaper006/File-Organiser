# File Organizer - Summary 📂

## Overview
This script is a simple file organizer that categorizes files in a selected directory based on predefined extensions.

## Functions & Their Purpose 🚀

### 1. `load_categories()`
- Returns a dictionary of file extensions mapped to their respective categories.
- Example: `.jpg` → "Images", `.mp3` → "Audio".

### 2. `organize_files(directory, categories)`
- Organizes files in the selected directory by moving them into categorized folders.
- Uses `shutil.move()` to move files into appropriate directories.

### 3. `select_directory()`
- Opens a file dialog to allow the user to select a directory for organizing.
- Updates `directory_var` with the chosen path.

### 4. `start_organization()`
- Initiates the file organization process.
- Ensures a valid directory is selected before proceeding.

## GUI Components 🎨
- **Entry Box**: Displays the selected directory path.
- **Browse Button**: Opens a directory selection dialog.
- **Organize Files Button**: Starts the organization process.
- **Log Box**: Displays real-time updates on file movements.

## How to Use 🛠️
1. Run the script (`python script.py`).
2. Click the **Browse** button and select a folder.
3. Click **Organize Files** to start organizing.
4. The log box will show the progress.

### Output Structure 📁
Files will be moved into folders based on their type:
```
📂 Selected Directory
   ├── 📂 Images
   │     ├── file1.jpg
   │     ├── file2.png
   ├── 📂 Documents
   │     ├── file1.pdf
   │     ├── file2.docx
   ├── 📂 Audio
   │     ├── file1.mp3
   ├── 📂 Videos
   │     ├── file1.mp4
```

Happy Organizing! 🎉


# 📂 File Organizer - Summary 🎯

## 🌟 Overview
This script is a powerful yet simple file organizer that automatically sorts files in a selected directory based on their extensions. Say goodbye to messy folders! 🧹🚀

## 🛠️ Functions & Their Purpose

### 1️⃣ `load_categories()` 📋
- Returns a dictionary of file extensions mapped to their respective categories. 📄🎶🎥
- Example: `.jpg` → 🖼️ "Images", `.mp3` → 🎵 "Audio".

### 2️⃣ `organize_files(directory, categories)` 📦
- Organizes files in the selected directory by moving them into categorized folders. 📂
- Uses `shutil.move()` to efficiently move files into appropriate directories. 🚛

### 3️⃣ `select_directory()` 🗂️
- Opens a file dialog allowing the user to select a directory for organizing. 📍
- Updates `directory_var` with the chosen path. ✅

### 4️⃣ `start_organization()` 🔄
- Initiates the file organization process. 🏁
- Ensures a valid directory is selected before proceeding. ⚠️

## 🎨 GUI Components
- 📝 **Entry Box**: Displays the selected directory path.
- 📂 **Browse Button**: Opens a directory selection dialog.
- 🏗️ **Organize Files Button**: Starts the organization process.
- 📜 **Log Box**: Displays real-time updates on file movements.

## 🚀 How to Use
1️⃣ Run the script (`python script.py`) ▶️
2️⃣ Click the **Browse** button and select a folder 📂
3️⃣ Click **Organize Files** to start sorting 🎯
4️⃣ Watch the log box update as files get organized 📜🔄

### 📁 Output Structure
Your files will be neatly categorized like this:
```
📂 Selected Directory
   ├── 🖼️ Images
   │     ├── file1.jpg
   │     ├── file2.png
   ├── 📄 Documents
   │     ├── file1.pdf
   │     ├── file2.docx
   ├── 🎵 Audio
   │     ├── file1.mp3
   ├── 🎥 Videos
   │     ├── file1.mp4
```

✨ Happy Organizing! 🎉📂🚀


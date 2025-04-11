# 📂 File Organizer

A fun and simple **drag-and-drop** file organizer tool built with Python's `tkinter`. It sorts your messy folders by file type — and gives special love to PDFs by organizing them **by date**!

---

## ✨ Features

- ✅ Organizes files into folders by type:
  - 📄 Documents, 🖼️ Images, 🎵 Music, 🎥 Videos, 🗜️ Archives, ⚙️ Programs
- 📅 **PDFs are organized by date**:
  - Automatically moves PDFs into folders based on their **last modified date**
  - Format: `PDF/YYYY-MM-DD/filename.pdf`
- 🖱️ Easy-to-use **GUI interface**
- 🔄 Live progress bar
- 📜 Log of actions performed
- ❌ Skips hidden and system files
- ⚠️ Handles errors without crashing

---

## 🗂️ File Format & Folder Structure

### Supported File Types

| Type            | Extensions                   | Folder Path Example                      |
|------------------|------------------------------|-------------------------------------------|
| 📄 PDF           | `.pdf`                       | `PDF/2025-04-11/filename.pdf`             |
| 📝 Text          | `.txt`                       | `Documents/Text Files/`                   |
| 🖼️ Images         | `.jpg`, `.jpeg`, `.png`      | `Images/`, `Images/Png/`                  |
| 📊 Spreadsheets  | `.xlsx`, `.csv`              | `Documents/Spreadsheets/`, `CVS/`         |
| 📁 Docs          | `.docx`, `.pptx`             | `Documents/`, `Documents/PPT/`            |
| 🎵 Music         | `.mp3`                       | `Music/`                                  |
| 🎥 Videos        | `.mp4`, `.mkv`               | `Videos/MP4/`, `Videos/MkV/`              |
| 🗜️ Archives       | `.zip`, `.rar`, `.7z`        | `Archives/Zip/`, `Archives/Rar/`, etc.    |
| ⚙️ Programs       | `.exe`, `.msi`               | `Program/`                                 |
| 🧠 OS Files       | `.ios`                       | `OS/`                                      |

---

## 🚀 How to Use

1. **Run the Script**  
   Launch the Python file and the app will open in a window.

2. **Select Your Folder**  
   Click **Browse**, pick the folder you want to clean up.

3. **Hit Organize**  
   Sit back as it works its magic — watch the progress bar and logs.

4. **Done!**  
   Your files are now neatly arranged!

---

## ⚙️ Requirements

- Python 3.x
- No third-party libraries needed  
  *(just standard stuff like `tkinter`, `os`, `shutil`, etc.)*

---

## 📁 Example Output (PDF)
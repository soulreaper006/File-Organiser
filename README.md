# 🚀 File Organizer: Features & Specifications

## 📝 Overview  
The **File Organizer** is a C++ program designed to automatically sort files into categorized folders based on their extensions. It enhances user convenience by providing a **configurable, recursive, and GUI-supported** file management solution.

---

## 🎯 Key Features  

### ✅ Automatic File Organization  
- 📂 Scans a specified directory for files.  
- 📁 Moves files into appropriate folders based on their extensions.  
- ⚙️ Uses a **configuration file (`config.txt`)** to allow custom categories.  

### 🔄 Recursive Directory Scanning  
- 📜 Organizes files **within subdirectories**, ensuring thorough sorting.  

### ✏️ Customizable File Categories  
- 📝 Users can edit `config.txt` to define new file extensions and categories.  
- 🚀 No need to modify C++ code to add new categories.  

### 🖥️ GUI Interface for Easy Navigation  
- 🖱️ A Python-based **GUI (`tkinter`)** allows users to select a directory.  
- 🚫 Eliminates the need for command-line input.  

### 🌍 Cross-Platform Compatibility  
- 🏁 Works on **Windows, Linux, and macOS** using `std::filesystem`.  
- 🐍 GUI is implemented using Python for platform independence.  

---

## ⚙️ Technical Specifications  

### 💻 Programming Languages & Libraries  
- 🏗️ **C++17** (`std::filesystem`) for file operations.  
- 🖥️ **Python (`tkinter`)** for GUI integration.  

### 📂 File Handling  
- 📖 Reads **file extensions from `config.txt`**.  
- 🏗️ Creates missing folders dynamically.  
- 🔀 Moves files using `std::filesystem::rename()`.  

### 🎮 User Interaction  
- 🔢 Users enter a directory path **(CLI mode)** or select via GUI.  
- 📜 Program logs **moved files and destination folders**.  

### 🔄 Execution Workflow  
1. 📂 **User selects a folder** via the command line or GUI.  
2. 📖 **The C++ program reads `config.txt`** for file categories.  
3. 📜 **It scans the directory recursively**, sorting files into folders.  
4. ✅ **Logs the operations performed** (file movements).  

---

## ▶️ How to Use  

### 🖥️ CLI Mode:  
```sh
./file_organizer

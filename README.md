# **📂 File Organizer Script - Summary**

## **✨ Overview**  
This Python script provides a **graphical user interface (GUI)** for organizing files within a selected directory based on predefined categories stored in a configuration file (`config.txt`). It utilizes the **Tkinter library** to enable user interactions, such as selecting a directory and initiating file organization. 🖥️

---

## **🔥 Features**

### **1️⃣ GUI-Based File Organizer**  
✅ Uses Tkinter to provide an intuitive graphical interface.  
✅ Allows users to select a directory and organize files with a single click.  

### **2️⃣ Configuration-Based Categorization**  
📝 Reads file categories from `config.txt`, mapping file extensions to folder names.  
📂 Automatically moves files based on their extensions.  

### **3️⃣ File Sorting & Organization**  
🔍 Scans the selected directory for files.  
📦 Moves files into categorized subfolders based on their extensions.  

### **4️⃣ User Feedback & Logging**  
📜 Displays real-time logs in a text box to inform users about moved files.  
📢 Shows success and error messages through message boxes.  

### **5️⃣ Error Handling**  
⚠️ Alerts the user if the `config.txt` file is missing.  
✅ Checks if the selected directory is valid before proceeding.  
🛑 Handles missing categories gracefully to avoid unexpected behavior.  

---

## **🛠️ Specifications & Technologies Used**

- **👨‍💻 Programming Language**: Python  
- **📚 Libraries Used**:  
  - 🖼️ `tkinter` → GUI design, directory selection, and message boxes.  
  - 🚛 `shutil` → Moving files between directories.  
  - 📂 `os` → Directory and file handling.  

- **🔢 Required Input**:  
  - 📁 A valid directory containing files.  
  - 🗂️ A `config.txt` file defining file extension mappings (e.g., `.jpg Images`).  

- **📤 Output**:  
  - 🎯 Files get automatically sorted into subfolders inside the selected directory.  
  - 📝 A log of moved files is displayed in the GUI.  

This script is perfect for users who want to **organize files effortlessly** without manually sorting them into folders. 🚀🎉


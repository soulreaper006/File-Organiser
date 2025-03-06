import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def load_categories():
    categories = {
        ".txt": "Documents\Text Files",
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images\Png",
        ".pdf": "Documents\Pdf",
        ".docx": "Documents",
        ".xlsx": "Documents\Spreadsheets",
        ".csv": "Documents\Spreadsheets\CVS",
        ".pptx": "Documents\PPT",
        ".mp3": "Music",
        ".mp4": "Videos\MP4",
        ".mkv": "Videos\MkV",
        ".zip": "Archives\Zip",
        ".7z": "Archives\_7Z",
        ".rar": "Archives\Rar",
        ".ios": "OS",
        ".exe": "Program",
        ".msi": "Program"
    }
    return categories

def organize_files(directory, categories):
    if not os.path.exists(directory):
        messagebox.showerror("Error", "Invalid directory!")
        return
    
    for root, _, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in categories:
                target_folder = os.path.join(directory, categories[ext])
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(os.path.join(root, file), os.path.join(target_folder, file))
                log_text.insert(tk.END, f"Moved: {file} -> {categories[ext]}\n")
                log_text.yview(tk.END)
    messagebox.showinfo("Success", "File organization completed!")

def select_directory():
    dir_path = filedialog.askdirectory()
    if dir_path:
        directory_var.set(dir_path)

def start_organization():
    directory = directory_var.get()
    if not directory:
        messagebox.showerror("Error", "Please select a directory!")
        return
    categories = load_categories()
    if categories:
        organize_files(directory, categories)

# GUI Setup
root = tk.Tk()
root.title("File Organizer")
root.geometry("500x350")

directory_var = tk.StringVar()

tk.Label(root, text="Select Directory:").pack(pady=5)
tk.Entry(root, textvariable=directory_var, width=50).pack(pady=5)
tk.Button(root, text="Browse", command=select_directory).pack(pady=5)

tk.Button(root, text="Organize Files", command=start_organization).pack(pady=10)

log_text = tk.Text(root, height=12, width=60)
log_text.pack(pady=5)

root.mainloop()
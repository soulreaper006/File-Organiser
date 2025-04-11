import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime

def load_categories():
    categories = {
        ".txt": r"Documents\Text Files",
        ".jpg": r"Images",
        ".jpeg": r"Images",
        ".png": r"Images\Png",
        ".pdf": r"",  # PDFs will be handled separately
        ".docx": r"Documents",
        ".xlsx": r"Documents\Spreadsheets",
        ".csv": r"Documents\Spreadsheets\CVS",
        ".pptx": r"Documents\PPT",
        ".mp3": r"Music",
        ".mp4": r"Videos\MP4",
        ".mkv": r"Videos\MkV",
        ".zip": r"Archives\Zip",
        ".7z": r"Archives\_7Z",
        ".rar": r"Archives\Rar",
        ".ios": r"OS",
        ".exe": r"Program",
        ".msi": r"Program"
    }
    return categories

def get_file_date(filepath):
    timestamp = os.path.getmtime(filepath)  # Use getctime for creation date on Windows
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

def organize_files(directory, categories):
    if not os.path.exists(directory):
        messagebox.showerror("Error", "Invalid directory!")
        return

    organize_button.config(state="disabled")
    log_text.delete(1.0, tk.END)

    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith('.') or file in ['Thumbs.db']:
                continue
            all_files.append((root, file))

    total_files = len(all_files)
    moved_count = 0

    for i, (root_dir, file) in enumerate(all_files, start=1):
        ext = os.path.splitext(file)[1].lower()
        file_path = os.path.join(root_dir, file)

        if ext == ".pdf":
            date_folder = get_file_date(file_path)
            target_folder = os.path.join(directory, "PDF", date_folder)
        elif ext in categories:
            if not categories[ext]:  # Skip if it's the PDF placeholder
                continue
            target_folder = os.path.join(directory, categories[ext])
        else:
            continue

        os.makedirs(target_folder, exist_ok=True)
        try:
            shutil.move(file_path, os.path.join(target_folder, file))
            moved_count += 1
            log_text.insert(tk.END, f"Moved: {file} -> {target_folder}\n")
            log_text.yview(tk.END)
        except Exception as e:
            log_text.insert(tk.END, f"Failed to move {file}: {e}\n")

        progress_var.set(i / total_files * 100)
        root.update_idletasks()

    messagebox.showinfo("Success", f"Organized {moved_count} files!")
    organize_button.config(state="normal")

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
root.geometry("550x420")

directory_var = tk.StringVar()

tk.Label(root, text="Select Directory:").pack(pady=5)
tk.Entry(root, textvariable=directory_var, width=60).pack(pady=5)
tk.Button(root, text="Browse", command=select_directory).pack(pady=5)

organize_button = tk.Button(root, text="Organize Files", command=start_organization)
organize_button.pack(pady=10)

# Progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate", variable=progress_var)
progress_bar.pack(pady=5)

log_text = tk.Text(root, height=12, width=65)
log_text.pack(pady=5)

root.mainloop()
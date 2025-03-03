import tkinter as tk
from tkinter import filedialog
import subprocess

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        command = ["./file_organizer", folder_selected]
        subprocess.run(command, shell=True)

# Create GUI window
root = tk.Tk()
root.title("File Organizer")
root.geometry("300x150")

label = tk.Label(root, text="Select a folder to organize files")
label.pack(pady=10)

btn_select = tk.Button(root, text="Select Folder", command=select_folder)
btn_select.pack(pady=10)

root.mainloop()
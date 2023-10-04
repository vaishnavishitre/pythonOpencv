import tkinter as tk
from tkinter import filedialog
import os
import subprocess

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        process_images(folder_path)

def process_images(folder_path):
    # List all image files in the specified folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    # Check if there are any images in the folder
    if not image_files:
        print("No image files found in the selected folder.")
        return

    # Run the colorize.py script for each image in the folder
    for image_file in image_files:
        img_path = os.path.join(folder_path, image_file)
        subprocess.run(["python", "colorize.py", img_path])

# Create the main window
root = tk.Tk()
root.title("Colorize Images")

# Create a "Select Folder" button
browse_button = tk.Button(root, text="Select Folder", command=browse_folder)
browse_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()

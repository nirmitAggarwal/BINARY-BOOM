import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_folder_path.delete(0, tk.END)
        entry_folder_path.insert(0, folder_path)

def split_file():
    file_path = entry_file_path.get()
    num_chunks = int(entry_num_chunks.get())

    if not os.path.isfile(file_path):
        messagebox.showerror("Error", "Invalid file path")
        return

    file_size = os.path.getsize(file_path)
    chunk_size = file_size // num_chunks

    output_folder = os.path.join(os.path.dirname(file_path), "split_files")
    os.makedirs(output_folder, exist_ok=True)

    with open(file_path, 'rb') as f:
        for i in range(num_chunks):
            chunk = f.read(chunk_size)
            if not chunk:
                break
            binary_data = ''.join(format(byte, '08b') for byte in chunk)
            with open(os.path.join(output_folder, f"chunk_{i}.txt"), 'w') as chunk_file:
                chunk_file.write(binary_data)

    messagebox.showinfo("Success", f"File split into {num_chunks} chunks.")

def reconstruct_file():
    folder_path = entry_folder_path.get()
    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid folder path")
        return

    binary_data = ""
    for file_name in sorted(os.listdir(folder_path)):
        if file_name.startswith("chunk_") and file_name.endswith(".txt"):
            with open(os.path.join(folder_path, file_name), 'r') as chunk_file:
                binary_data += chunk_file.read()

    output_file_path = os.path.join(folder_path, "reconstructed_file")
    with open(output_file_path, 'wb') as output_file:
        bytes_data = int(binary_data, 2).to_bytes(len(binary_data) // 8, byteorder='big')
        output_file.write(bytes_data)

    messagebox.showinfo("Success", f"File reconstructed as {output_file_path}")

app = tk.Tk()
app.title("File Splitter and Reconstructor")

# File selection
tk.Label(app, text="Select File:").grid(row=0, column=0, padx=10, pady=10)
entry_file_path = tk.Entry(app, width=50)
entry_file_path.grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=10)

# Number of chunks
tk.Label(app, text="Number of Chunks:").grid(row=1, column=0, padx=10, pady=10)
entry_num_chunks = tk.Entry(app, width=50)
entry_num_chunks.grid(row=1, column=1, padx=10, pady=10)

# Split file button
tk.Button(app, text="Split File", command=split_file).grid(row=2, columnspan=3, padx=10, pady=10)

# Folder selection for reconstruction
tk.Label(app, text="Select Folder:").grid(row=3, column=0, padx=10, pady=10)
entry_folder_path = tk.Entry(app, width=50)
entry_folder_path.grid(row=3, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_folder).grid(row=3, column=2, padx=10, pady=10)

# Reconstruct file button
tk.Button(app, text="Reconstruct File", command=reconstruct_file).grid(row=4, columnspan=3, padx=10, pady=10)

app.mainloop()

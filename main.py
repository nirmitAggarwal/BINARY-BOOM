import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def select_folder(entry_widget):
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, folder_path)

def split_file():
    file_path = entry_file_path.get()
    num_chunks = int(entry_num_chunks.get())
    save_folder = entry_save_folder.get()

    if not os.path.isfile(file_path):
        messagebox.showerror("Error", "Invalid file path")
        return

    if not os.path.isdir(save_folder):
        messagebox.showerror("Error", "Invalid save folder path")
        return

    file_size = os.path.getsize(file_path)
    chunk_size = file_size // num_chunks

    output_folder = os.path.join(save_folder, "split_files")
    os.makedirs(output_folder, exist_ok=True)

    with open(file_path, 'rb') as f:
        for i in range(num_chunks):
            chunk = f.read(chunk_size)
            if not chunk:
                break
            binary_data = ''.join(format(byte, '08b') for byte in chunk)
            with open(os.path.join(output_folder, f"chunk_{i}.txt"), 'w') as chunk_file:
                chunk_file.write(binary_data)
            progress_var.set((i + 1) / num_chunks * 100)
            app.update_idletasks()

    # Write README file
    file_name = os.path.basename(file_path)
    with open(os.path.join(output_folder, "README.txt"), 'w') as readme_file:
        readme_file.write(f"Original File Name: {file_name}\n")
        readme_file.write(f"Number of Chunks: {num_chunks}\n")

    messagebox.showinfo("Success", f"File split into {num_chunks} chunks.")

def reconstruct_file():
    folder_path = entry_folder_path.get()
    save_folder = entry_reconstructed_save_folder.get()

    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid folder path")
        return

    if not os.path.isdir(save_folder):
        messagebox.showerror("Error", "Invalid save folder path")
        return

    # Read README file
    readme_path = os.path.join(folder_path, "README.txt")
    if not os.path.isfile(readme_path):
        messagebox.showerror("Error", "README file not found in the selected folder")
        return

    with open(readme_path, 'r') as readme_file:
        lines = readme_file.readlines()
        original_file_name = lines[0].split(":")[1].strip()

    binary_data = ""
    chunk_files = sorted([f for f in os.listdir(folder_path) if f.startswith("chunk_") and f.endswith(".txt")])
    for i, file_name in enumerate(chunk_files):
        with open(os.path.join(folder_path, file_name), 'r') as chunk_file:
            binary_data += chunk_file.read()
        progress_var.set((i + 1) / len(chunk_files) * 100)
        app.update_idletasks()

    output_file_path = os.path.join(save_folder, original_file_name)
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

# Save folder for split files
tk.Label(app, text="Save Split Files To:").grid(row=2, column=0, padx=10, pady=10)
entry_save_folder = tk.Entry(app, width=50)
entry_save_folder.grid(row=2, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=lambda: select_folder(entry_save_folder)).grid(row=2, column=2, padx=10, pady=10)

# Split file button
tk.Button(app, text="Split File", command=split_file).grid(row=3, columnspan=3, padx=10, pady=10)

# Folder selection for reconstruction
tk.Label(app, text="Select Folder with Split Files:").grid(row=4, column=0, padx=10, pady=10)
entry_folder_path = tk.Entry(app, width=50)
entry_folder_path.grid(row=4, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=lambda: select_folder(entry_folder_path)).grid(row=4, column=2, padx=10, pady=10)

# Save folder for reconstructed file
tk.Label(app, text="Save Reconstructed File To:").grid(row=5, column=0, padx=10, pady=10)
entry_reconstructed_save_folder = tk.Entry(app, width=50)
entry_reconstructed_save_folder.grid(row=5, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=lambda: select_folder(entry_reconstructed_save_folder)).grid(row=5, column=2, padx=10, pady=10)

# Reconstruct file button
tk.Button(app, text="Reconstruct File", command=reconstruct_file).grid(row=6, columnspan=3, padx=10, pady=10)

# Progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(app, variable=progress_var, maximum=100)
progress_bar.grid(row=7, columnspan=3, padx=10, pady=10, sticky='ew')

app.mainloop()

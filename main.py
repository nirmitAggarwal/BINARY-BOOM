import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import StringVar, IntVar

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_file_path.set(file_path)

def select_folder(entry_widget):
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_widget.set(folder_path)

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

# Define the enhanced dark theme
style = ttk.Style(app)
style.theme_use('clam')

style.configure("TLabel",
                background="#1c1c1c",
                foreground="#e0e0e0",
                font=("Segoe UI", 12))
style.configure("TButton",
                background="#333333",
                foreground="#ffffff",
                font=("Segoe UI", 10, "bold"),
                padding=10,
                relief="flat")
style.map("TButton",
          background=[('active', '#444444')])
style.configure("TEntry",
                fieldbackground="#333333",
                foreground="#ffffff",
                insertcolor="#ffffff",
                font=("Segoe UI", 12),
                padding=10)
style.configure("TProgressbar",
                troughcolor="#333333",
                background="#4caf50",
                thickness=25)
style.configure("TFrame", background="#1c1c1c")

# Variables
entry_file_path = StringVar()
entry_num_chunks = IntVar()
entry_save_folder = StringVar()
entry_folder_path = StringVar()
entry_reconstructed_save_folder = StringVar()
progress_var = tk.DoubleVar()

main_frame = ttk.Frame(app, padding=(20, 10, 20, 20))
main_frame.grid(row=0, column=0, sticky="nsew")

# File selection
ttk.Label(main_frame, text="Select File:").grid(row=0, column=0, sticky="w")
ttk.Entry(main_frame, textvariable=entry_file_path, width=50).grid(row=0, column=1, padx=10, pady=5)
ttk.Button(main_frame, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=5)

# Number of chunks
ttk.Label(main_frame, text="Number of Chunks:").grid(row=1, column=0, sticky="w")
ttk.Entry(main_frame, textvariable=entry_num_chunks, width=50).grid(row=1, column=1, padx=10, pady=5)

# Save folder for split files
ttk.Label(main_frame, text="Save Split Files To:").grid(row=2, column=0, sticky="w")
ttk.Entry(main_frame, textvariable=entry_save_folder, width=50).grid(row=2, column=1, padx=10, pady=5)
ttk.Button(main_frame, text="Browse", command=lambda: select_folder(entry_save_folder)).grid(row=2, column=2, padx=10, pady=5)

# Split file button
ttk.Button(main_frame, text="Split File", command=split_file).grid(row=3, columnspan=3, padx=10, pady=10)

# Folder selection for reconstruction
ttk.Label(main_frame, text="Select Folder with Split Files:").grid(row=4, column=0, sticky="w")
ttk.Entry(main_frame, textvariable=entry_folder_path, width=50).grid(row=4, column=1, padx=10, pady=5)
ttk.Button(main_frame, text="Browse", command=lambda: select_folder(entry_folder_path)).grid(row=4, column=2, padx=10, pady=5)

# Save folder for reconstructed file
ttk.Label(main_frame, text="Save Reconstructed File To:").grid(row=5, column=0, sticky="w")
ttk.Entry(main_frame, textvariable=entry_reconstructed_save_folder, width=50).grid(row=5, column=1, padx=10, pady=5)
ttk.Button(main_frame, text="Browse", command=lambda: select_folder(entry_reconstructed_save_folder)).grid(row=5, column=2, padx=10, pady=5)

# Reconstruct file button
ttk.Button(main_frame, text="Reconstruct File", command=reconstruct_file).grid(row=6, columnspan=3, padx=10, pady=10)

# Progress bar
ttk.Progressbar(main_frame, variable=progress_var, maximum=100).grid(row=7, columnspan=3, padx=10, pady=20, sticky='ew')

app.configure(bg='#1c1c1c')  # Set background color
app.mainloop()


import os
import argparse

def split_file(file_path, num_chunks, save_folder):
    if not os.path.isfile(file_path):
        print("Invalid file path")
        return

    if not os.path.isdir(save_folder):
        print("Invalid save folder path")
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
            print(f"Progress: {((i + 1) / num_chunks) * 100:.2f}%")

    # Write README file
    file_name = os.path.basename(file_path)
    with open(os.path.join(output_folder, "README.txt"), 'w') as readme_file:
        readme_file.write(f"Original File Name: {file_name}\n")
        readme_file.write(f"Number of Chunks: {num_chunks}\n")

    print(f"File split into {num_chunks} chunks.")

def reconstruct_file(folder_path, save_folder):
    if not os.path.isdir(folder_path):
        print("Invalid folder path")
        return

    if not os.path.isdir(save_folder):
        print("Invalid save folder path")
        return

    # Read README file
    readme_path = os.path.join(folder_path, "README.txt")
    if not os.path.isfile(readme_path):
        print("README file not found in the selected folder")
        return

    with open(readme_path, 'r') as readme_file:
        lines = readme_file.readlines()
        original_file_name = lines[0].split(":")[1].strip()

    binary_data = ""
    chunk_files = sorted([f for f in os.listdir(folder_path) if f.startswith("chunk_") and f.endswith(".txt")])
    for i, file_name in enumerate(chunk_files):
        with open(os.path.join(folder_path, file_name), 'r') as chunk_file:
            binary_data += chunk_file.read()
        print(f"Progress: {((i + 1) / len(chunk_files)) * 100:.2f}%")

    output_file_path = os.path.join(save_folder, original_file_name)
    with open(output_file_path, 'wb') as output_file:
        bytes_data = int(binary_data, 2).to_bytes(len(binary_data) // 8, byteorder='big')
        output_file.write(bytes_data)

    print(f"File reconstructed as {output_file_path}")

def main():
    parser = argparse.ArgumentParser(description="File Splitter and Reconstructor")
    subparsers = parser.add_subparsers(dest="command")

    # Split file command
    split_parser = subparsers.add_parser("split", help="Split a file into multiple chunks")
    split_parser.add_argument("file_path", help="Path to the input file")
    split_parser.add_argument("num_chunks", type=int, help="Number of chunks to split the file into")
    split_parser.add_argument("save_folder", help="Folder to save the split files")

    # Reconstruct file command
    reconstruct_parser = subparsers.add_parser("reconstruct", help="Reconstruct a file from split chunks")
    reconstruct_parser.add_argument("folder_path", help="Folder containing the split files")
    reconstruct_parser.add_argument("save_folder", help="Folder to save the reconstructed file")

    args = parser.parse_args()

    if args.command == "split":
        split_file(args.file_path, args.num_chunks, args.save_folder)
    elif args.command == "reconstruct":
        reconstruct_file(args.folder_path, args.save_folder)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

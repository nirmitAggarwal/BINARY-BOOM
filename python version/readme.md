# File Splitter and Reconstructor

This Python GUI application allows you to split a file into smaller binary text files and reconstruct the original file from those binary text files. The application uses the `tkinter` library for the GUI and handles file operations using the `os` and `shutil` libraries.

## Features

- Select a file to split.
- Specify the number of smaller files (chunks).
- Choose a folder to save the split files.
- Reconstruct the original file from the split binary text files.
- Progress bar to show the percentage of conversion.
- Save the reconstructed file to a specified folder.

## Usage

1. **Split File**:
   - Click the "Browse" button next to "Select File" to choose the file you want to split.
   - Enter the number of chunks you want to split the file into.
   - Click the "Browse" button next to "Save Split Files To" to select the folder where the split files will be saved.
   - Click the "Split File" button to start the splitting process.

2. **Reconstruct File**:
   - Click the "Browse" button next to "Select Folder with Split Files" to choose the folder containing the split files.
   - Click the "Browse" button next to "Save Reconstructed File To" to select the folder where the reconstructed file will be saved.
   - Click the "Reconstruct File" button to start the reconstruction process.

## File Format

- The split files are saved as text files containing binary data.
- A `README.txt` file is created in the output folder during the splitting process. It contains:
  - Original file name.
  - Number of chunks.

## Requirements

- Python 3.x
- `tkinter` library

## Installation

No installation is required. Just run the `main.py` script.

## License

This project is open-source and does not have any specific license.


### README.md for the CLI Version

# File Splitter and Reconstructor - CLI Version

## Overview

The File Splitter and Reconstructor CLI Version is a command-line tool for splitting large files into smaller chunks and reconstructing them from these chunks. Built using Python, this tool operates through terminal commands, providing a straightforward and efficient way to manage file operations.

### Features

- **File Splitting**: Split a large file into several binary chunks via terminal commands.
- **File Reconstruction**: Reassemble the original file from split chunks using command-line arguments.
- **Progress Reporting**: View progress updates directly in the terminal.

### Installation

#### Prerequisites

Ensure that Python 3.6 or higher is installed.

#### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/file-splitter-cli.git
   cd file-splitter-cli
   ```

2. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should contain:

   ```
   argparse
   ```

3. **Run the CLI Tool**

   Use the following commands to run the tool:

   ```bash
   python cli_splitter.py split --help
   python cli_splitter.py reconstruct --help
   ```

### Usage

#### File Splitting

To split a file, run:

```bash
python cli_splitter.py split <file_path> <num_chunks> <save_folder>
```

- `<file_path>`: Path to the file to be split.
- `<num_chunks>`: Number of chunks to create.
- `<save_folder>`: Folder where split files will be saved.

#### File Reconstruction

To reconstruct a file, use:

```bash
python cli_splitter.py reconstruct <folder_path> <save_folder>
```

- `<folder_path>`: Folder containing the split files.
- `<save_folder>`: Folder to save the reconstructed file.

### Functionality Details

#### File Splitting

- Splits the file into binary chunks based on the number of chunks provided.
- Saves each chunk as a `.txt` file containing binary data.
- Creates a `README.txt` file in the output folder with details about the original file and the number of chunks.

#### File Reconstruction

- Reads the `README.txt` file to find the original file name.
- Combines binary chunks to reconstruct the original file.
- Saves the reconstructed file in the specified location.

### Troubleshooting

- **Invalid File Path/Error**: Ensure that file and folder paths are correct.
- **Progress Reporting Issues**: If progress updates do not appear, check for errors in the terminal output.

### Contact

For any questions or issues, please reach out to:

- **Nirmit Aggarwal**
- **Email**: nirmitjee@gmail.com
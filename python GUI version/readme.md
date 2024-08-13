Here are the detailed texts for the `README.md` files for both the CLI and GUI versions:

---

### README.md for the GUI Version

# File Splitter and Reconstructor - GUI Version

## Overview

The File Splitter and Reconstructor GUI Version is a user-friendly application designed to handle the splitting and reconstruction of large files. Utilizing Python's Tkinter library, this tool provides an intuitive graphical interface for managing file operations. 

### Features

- **File Splitting**: Divide a large file into multiple smaller chunks.
- **File Reconstruction**: Reassemble the original file from its split chunks.
- **Progress Tracking**: Real-time progress tracking with a visual progress bar.
- **File and Folder Selection**: Easy selection of files and destination folders through dialog boxes.
- **Modern Dark Theme**: A visually appealing dark theme that enhances usability.

### Installation

#### Prerequisites

Make sure Python 3.6 or newer is installed on your system.

#### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/file-splitter-gui.git
   cd file-splitter-gui
   ```

2. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should list:

   ```
   tkinter
   ```

3. **Run the Application**

   Start the application using:

   ```bash
   python gui_splitter.py
   ```

### Usage

#### File Splitting

1. Click "Browse" next to "Select File" to choose the file you want to split.
2. Enter the desired number of chunks.
3. Click "Browse" next to "Save Split Files To" to choose the output directory.
4. Click "Split File" to begin the splitting process. A progress bar will show the current progress.

#### File Reconstruction

1. Click "Browse" next to "Select Folder with Split Files" to select the folder containing the split files.
2. Click "Browse" next to "Save Reconstructed File To" to choose where the reconstructed file will be saved.
3. Click "Reconstruct File" to start the reconstruction. The progress will be updated via the progress bar.

### Functionality Details

#### File Splitting

- The application splits the selected file into binary chunks based on the number of chunks specified.
- Each chunk is saved as a `.txt` file containing binary data.
- A `README.txt` file is generated in the output folder, documenting the original file name and number of chunks.

#### File Reconstruction

- The application reads the `README.txt` file to determine the original file name.
- It combines the binary chunks to reconstruct the original file.
- The reconstructed file is saved in the specified location.

### Troubleshooting

- **Invalid File Path/Error**: Ensure that the file path and save folder paths are correct and accessible.
- **Progress Bar Issues**: If the progress bar does not update, check for application freezes or errors.

### Contact

For support or inquiries, please contact:

- **Nirmit Aggarwal**
- **Email**: nirmitjee@gmail.com

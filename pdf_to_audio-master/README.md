# PDF to Audio Converter

A Python application that converts PDF files to audio using text-to-speech technology. This application provides a user-friendly graphical interface for easy conversion of PDF documents to MP3 audio files.

## Features

- Simple and intuitive graphical user interface
- PDF text extraction
- Text-to-speech conversion
- Progress indication
- Save audio as MP3 files
- Support for multiple pages
- Error handling and user feedback

## Requirements

- Python 3.7 or higher
- Required Python packages (install using `pip install -r requirements.txt`):
  - PyMuPDF`
  - gTTS (Google Text-to-Speech)
  - pydub
  - tkinter (usually comes with Python)

## Installation

1. Clone or download this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python pdf_to_audio.py
   ```

2. Using the application:
   - Click "Browse" to select your PDF file
   - Choose an output location for the audio file
   - Click "Convert to Audio" to start the conversion
   - Wait for the conversion to complete
   - The audio file will be saved in the selected location

## Notes

- The application uses Google's Text-to-Speech service, so an internet connection is required
- Large PDF files may take longer to process
- The output audio file will be saved in MP3 format
- The filename will be the same as the PDF file with a .mp3 extension

## Troubleshooting

If you encounter any issues:
- Make sure all required packages are installed correctly
- Check if the PDF file is readable and contains extractable text
- Ensure you have write permissions in the output directory
- Verify your internet connection is active (required for gTTS) 
# PDF to Audio Converter

A Python-based utility that converts PDF documents to audio files, making content more accessible for users with visual impairments or those who prefer audio formats.

## Features

- Extracts text from PDF documents 
- Converts extracted text to speech using text-to-speech technology
- Supports various audio output formats
- User-friendly command-line interface
- Options to customize voice, speed, and output format

## Requirements

- Python 3.6 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/siddarha17/PDF_TO_AUDIO_CONVERTER.git
   cd PDF_TO_AUDIO_CONVERTER
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```
python pdf_to_audio.py --input document.pdf --output audio_file
```

### Options

- `--input`: Path to the PDF file (required)
- `--output`: Filename for the output audio file (without extension)
- `--voice`: Select voice type (default: default system voice)
- `--rate`: Speech rate (default: normal)
- `--format`: Output audio format like mp3, wav (default: mp3)

## Example

```
python pdf_to_audio.py --input research_paper.pdf --output research_summary --voice female --rate slow --format mp3
```

## Project Structure

- `pdf_to_audio.py`: Main conversion script
- `requirements.txt`: List of required Python packages
- `README.md`: Project documentation

## How It Works

1. The script reads the PDF file using PDF processing libraries
2. Text is extracted from the PDF document
3. The extracted text is processed to improve speech quality (removing special characters, fixing formatting)
4. Text-to-speech engine converts the processed text into spoken words
5. The audio is saved in the specified format

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the developers of the PDF processing and text-to-speech libraries used in this project
- Inspired by the need to make written content more accessible

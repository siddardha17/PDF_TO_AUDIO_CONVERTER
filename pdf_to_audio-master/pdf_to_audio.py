import tkinter as tk #used for creating GUI(Graphical user Interface)
from tkinter import filedialog, ttk, messagebox #To browse for PDF and output directory
from PyPDF2 import PdfReader # Styled widgets (buttons, entries, progress bar, etc.).
from gtts import gTTS #Converts text to speech (saves as MP3).
import os #File and path operations.
import threading #To keep GUI responsive during long operations.

class PDFToAudioConverter: #This class encapsulates the GUI app and logic.
    def __init__(self, root):#root: Tkinter root window.Initializes GUI window title, size, and background.
        self.root = root
        self.root.title("PDF to Audio Converter")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")
        
        # Variables
        self.pdf_path = tk.StringVar()#path to selected PDF.
        self.output_path = tk.StringVar()#where to save MP3
        self.status_var = tk.StringVar()#displays the current status ("Ready", "Converting", etc.).
        self.status_var.set("Ready")
        
        self.create_widgets()#to build the GUI.
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # PDF Selection
        ttk.Label(main_frame, text="Select PDF File:").pack(anchor=tk.W)
        pdf_frame = ttk.Frame(main_frame)
        pdf_frame.pack(fill=tk.X, pady=(5, 15))
        
        ttk.Entry(pdf_frame, textvariable=self.pdf_path).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(pdf_frame, text="Browse", command=self.browse_pdf).pack(side=tk.LEFT, padx=(5, 0))
        
        # Output Selection
        ttk.Label(main_frame, text="Select Output Location:").pack(anchor=tk.W)
        output_frame = ttk.Frame(main_frame)
        output_frame.pack(fill=tk.X, pady=(5, 15))
        
        ttk.Entry(output_frame, textvariable=self.output_path).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(output_frame, text="Browse", command=self.browse_output).pack(side=tk.LEFT, padx=(5, 0))
        
        # Convert Button
        ttk.Button(main_frame, text="Convert to Audio", command=self.start_conversion).pack(pady=20)
        
        # Progress Bar
        self.progress_bar = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress_bar.pack(fill=tk.X, pady=(10, 5))
        
        # Status Label
        ttk.Label(main_frame, textvariable=self.status_var).pack()
    
    def browse_pdf(self):#Opens file/folder dialogs and stores paths in variables using set()
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_path.set(file_path)
    
    def browse_output(self):#Opens file/folder dialogs and stores paths in variables using set()
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.output_path.set(folder_path)
    
    def extract_text_from_pdf(self, pdf_path):
        text = ""
        try:
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")
    
    def convert_to_audio(self):
        try:
            if not self.pdf_path.get() or not self.output_path.get():
                raise Exception("Please select both PDF file and output location")
            
            self.status_var.set("Extracting text from PDF...")
            text = self.extract_text_from_pdf(self.pdf_path.get())
            
            if not text.strip():
                raise Exception("No text found in the PDF")
            
            self.status_var.set("Converting text to speech...")
            pdf_name = os.path.splitext(os.path.basename(self.pdf_path.get()))[0]
            output_file = os.path.join(self.output_path.get(), f"{pdf_name}.mp3")
            
            # Split text into smaller chunks if it's too long
            max_chars = 5000  # gTTS works better with smaller chunks
            text_chunks = [text[i:i+max_chars] for i in range(0, len(text), max_chars)]
            
            # Create final output file
            if len(text_chunks) == 1:
                # If text is small enough, convert directly
                tts = gTTS(text=text_chunks[0], lang='en')
                tts.save(output_file)
            else:
                # For longer texts, process each chunk separately
                temp_dir = os.path.join(self.output_path.get(), "temp_chunks")
                os.makedirs(temp_dir, exist_ok=True)
                
                chunk_files = []
                total_chunks = len(text_chunks)
                
                for i, chunk in enumerate(text_chunks):
                    self.status_var.set(f"Converting chunk {i+1} of {total_chunks}...")
                    chunk_file = os.path.join(temp_dir, f"chunk_{i}.txt")
                    with open(chunk_file, 'w', encoding='utf-8') as f:
                        f.write(chunk)
                    chunk_files.append(chunk_file)
                
                # Combine all text chunks into one file
                with open(output_file, 'w', encoding='utf-8') as outfile:
                    for chunk_file in chunk_files:
                        with open(chunk_file, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read())
                
                # Convert the combined file
                tts = gTTS(text=text, lang='en')
                tts.save(output_file)
                
                # Clean up temporary files
                for chunk_file in chunk_files:
                    try:
                        os.remove(chunk_file)
                    except:
                        pass
                try:
                    os.rmdir(temp_dir)
                except:
                    pass
            
            self.status_var.set("Conversion completed successfully!")
            messagebox.showinfo("Success", f"Audio file saved as:\n{output_file}")
            
        except Exception as e:
            self.status_var.set("Error: " + str(e))
            messagebox.showerror("Error", str(e))
        
        finally:
            self.progress_bar.stop()
            self.progress_bar.pack_forget()
    
    def start_conversion(self):#Runs convert_to_audio in a separate thread using threading.Thread to prevent GUI from freezing.

        self.progress_bar.pack(fill=tk.X, pady=(10, 5))
        self.progress_bar.start()
        threading.Thread(target=self.convert_to_audio, daemon=True).start()

if __name__ == "__main__":#Creates and runs the application window.
    root = tk.Tk()
    app = PDFToAudioConverter(root)
    root.mainloop() 
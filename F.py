import os
import random
import string
import torch
from reportlab.pdfgen import canvas
from pelican import signals
from pelican.generators import Generator
import tkinter as tk
from tkinter import filedialog

class AdvancedPdfGenerator(Generator):
   

    def __init__(self, *args, **kwargs):
        super(AdvancedPdfGenerator, self).__init__(*args, **kwargs)

    def _generate_random_string(self, length=10):
        
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def _create_advanced_pdf(self, obj, output_path):
        
        if obj.source_path.endswith('.rst'):
            filename = self._generate_random_string() + ".pdf"
            output_pdf = os.path.join(output_path, filename)

          
            data = torch.randn(3, 3)
            eigenvalues, eigenvectors = torch.symeig(data)
            scipy_result = scipy.special.exp10(eigenvalues.numpy())

            with canvas.Canvas(output_pdf) as pdf:
                pdf.drawString(100, 100, f"PyTorch and SciPy PDF for {obj.title}")
                pdf.drawString(100, 120, f"Eigenvalues: {eigenvalues}")
                pdf.drawString(100, 140, f"SciPy result: {scipy_result}")

            print(f'[Advanced] Created PDF for {obj.source_path} at {output_pdf}')

    def generate_context(self):
        pass

    def generate_output(self, writer=None):
        
        print('[Advanced] Generating PDF files...')
        pdf_path = os.path.join(self.output_path, 'advanced_pdf')
        if not os.path.exists(pdf_path):
            try:
                os.mkdir(pdf_path)
            except OSError:
                print("Couldn't create the advanced pdf output folder in " + pdf_path)

        for article in self.context['articles']:
            self._create_advanced_pdf(article, pdf_path)

        for page in self.context['pages']:
            self._create_advanced_pdf(page, pdf_path)


class PdfGeneratorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PDF Generator")
        self.root.geometry("300x100")

        self.generate_button = tk.Button(self.root, text="Generate PDFs", command=self.generate_pdfs)
        self.generate_button.pack(pady=20)

    def generate_pdfs(self):
        
        signals.get_generators.connect(get_advanced_generator)
        self.root.destroy()

def get_advanced_generator(generators):
    return AdvancedPdfGenerator

def main():
    
    gui = PdfGeneratorGUI()
    gui.root.mainloop()

if __name__ == "__main__":
    main()

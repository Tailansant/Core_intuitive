from abc import ABC, abstractmethod
import pdfplumber

class PDFExtractor(ABC):
    @abstractmethod
    def extract(self):
        pass

class PDFPlumberExtractor(PDFExtractor):
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract(self):
        datas = []
        try:
            with pdfplumber.open(self.pdf_path) as pdf_file:
                for page in pdf_file.pages:
                    text = page.extract_text()
                    for line in text.split('\n'):
                        if line.strip():
                            split_line = line.split()
                            datas.append(split_line)
        except Exception as e:
            print(f"Error reading PDF: {e}")
            exit()
        return datas
from handlers.file_handler import CSVFileHandler
from handlers.pdf_extractor import PDFPlumberExtractor
from transformers.abbreviation_replacer import AbbreviationReplacer
from compressors.file_compressor import FileCompressor
import pandas as pd

class DataTransformationPipeline:
    def __init__(self, pdf_path, csv_path, abbreviation_substitutions):
        self.pdf_path = pdf_path
        self.csv_handler = CSVFileHandler(csv_path)
        self.pdf_extractor = PDFPlumberExtractor(pdf_path)
        self.abbreviation_replacer = AbbreviationReplacer(abbreviation_substitutions)
        self.compressor = FileCompressor(csv_path)

    def execute(self):
        data = self.pdf_extractor.extract()
        
        data_frame = pd.DataFrame(data)
        data_frame = self.abbreviation_replacer.transform(data_frame)
        
        self.csv_handler.save(data_frame)
        
        self.compressor.compress('teste_tailan.zip')
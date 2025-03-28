import pdfplumber
import pandas as pd
import zipfile

class DataTransformation:
    def __init__(self, pdf_path, csv_output_path):
        self.pdf_path = pdf_path
        self.csv_output_path = csv_output_path
        
    
    def extract_file_data(self):
        
        datas = []
        
        with pdfplumber.open(self.pdf_path) as pdf_file:
            for page in pdf_file.pages:
                text = page.extract_text()
                for line in text.split('\n'):
                    if line.strip():
                        datas.append(line.split())
                        
                        
        return datas
    
    
    def save_csv(self, datas):
                
        data_frame = pd.DataFrame(datas, columns=['Procedimento', 'Categoria'])
        data_frame.to_csv(self.csv_output_path, index=False)
        
        print(f"Data saved in {self.csv_output_path}")
        
        
    def substitute_abbreviation(self):
        
        substitute =  {'OD': 'Descrição Completa OD', 'AMB': 'Descrição Completa AMB'}
        
        data_frame = pd.read_csv(self.csv_output_path)
        data_frame.replace(substitute, inplace=True)
        data_frame.to_csv(self.csv_output_path, index=False)
        
        
    def compact_csv(self):
        
        with zipfile.ZiptFile('teste_tailan.zip', 'w') as zip_file:
            zip_file.write(self.csv_output_path)
            
        print(f"file compacted")

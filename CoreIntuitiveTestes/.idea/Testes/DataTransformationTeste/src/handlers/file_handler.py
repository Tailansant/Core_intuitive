from abc import ABC, abstractmethod
import pandas as pd

class FileHandler(ABC):
    @abstractmethod
    def save(self, data):
        pass
    
    @abstractmethod
    def load(self):
        pass

class CSVFileHandler(FileHandler):
    def __init__(self, file_path):
        self.file_path = file_path
    
    def save(self, data):
        data.to_csv(self.file_path, index=False)
        print(f"Data saved to {self.file_path}")
    
    def load(self):
        return pd.read_csv(self.file_path)
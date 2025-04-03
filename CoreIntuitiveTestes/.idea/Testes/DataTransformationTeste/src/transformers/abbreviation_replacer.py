import pandas as pd
from abc import ABC, abstractmethod

class DataTransformer(ABC):
    @abstractmethod
    def transform(self, data):
        pass

class AbbreviationReplacer(DataTransformer):
    def __init__(self, substitutions):
        self.substitutions = substitutions

    def transform(self, data):
        data.replace(self.substitutions, inplace=True)
        return data
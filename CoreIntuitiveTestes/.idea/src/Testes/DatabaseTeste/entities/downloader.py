import os
from urllib.request import urlretrieve

class Downloader:
    def download_file(self, url, filename):
        try:

            self.ensure_data_folder()

            print(f"Downloading {url} to datas/{filename}...")
            urlretrieve(url, f'datas/{filename}')
            print(f"File {filename} downloaded successfully!")
        except Exception as e:
            print(f"Error downloading the file {filename}: {e}")

    def ensure_data_folder(self):
        """Verifica se a pasta 'datas' existe, caso contrário, cria."""
        if not os.path.exists('datas'):
            os.makedirs('datas')
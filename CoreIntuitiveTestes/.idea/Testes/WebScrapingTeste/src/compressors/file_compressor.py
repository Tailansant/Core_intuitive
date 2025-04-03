import zipfile
import os

class FileCompressor:
    def __init__(self, directory):
        self.directory = directory

    def compress_files(self, output_path):
        try:
            with zipfile.ZipFile(output_path, 'w') as zip_file:
                for file in os.listdir(self.directory):
                    if file.endswith('.pdf'):
                        zip_file.write(os.path.join(self.directory, file), file)
            print(f"Files compressed to {output_path}")
        except Exception as e:
            raise ValueError(f"Error compressing files: {e}")
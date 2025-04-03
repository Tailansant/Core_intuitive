import zipfile

class FileCompressor:
    def __init__(self, file_path):
        self.file_path = file_path

    def compress(self, output_path):
        with zipfile.ZipFile(output_path, 'w') as zip_file:
            zip_file.write(self.file_path)
        print(f"File compressed to {output_path}")
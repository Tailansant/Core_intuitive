import os
import requests

class FileDownloader:
    def __init__(self, save_directory):
        self.save_directory = save_directory

    def download_files(self, urls):
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)

        for url in urls:
            file_name = url.split('/')[-1]
            file_path = os.path.join(self.save_directory, file_name)

            try:
                response = requests.get(url)
                if response.status_code == 200:
                    with open(file_path, 'wb') as file:
                        file.write(response.content)
                    print(f"File downloaded: {file_name}")
                else:
                    print(f"Failed to download {url}. HTTP Status: {response.status_code}")
            except Exception as e:
                raise ValueError(f"Error downloading {url}: {e}")
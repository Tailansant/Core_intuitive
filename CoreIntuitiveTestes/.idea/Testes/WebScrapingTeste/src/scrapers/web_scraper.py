from drivers.drivers_initializer import DriverInitializer
from downloaders.file_downloader import FileDownloader
from compressors.file_compressor import FileCompressor
import time

class WebScraper:
    def __init__(self, url, save_directory):
        self.url = url
        self.save_directory = save_directory
        self.driver_initializer = DriverInitializer()
        self.file_downloader = FileDownloader(save_directory)
        self.file_compressor = FileCompressor(save_directory)
        self.driver = self.driver_initializer.init_driver()

    def access_site(self):
        try:
            self.driver.get(self.url)
            self.driver.implicitly_wait(10)
        except Exception as e:
            raise ValueError(f"Error accessing the site: {e}")

    def download_files(self, file_urls):
        self.file_downloader.download_files(file_urls)

    def compress_files(self):
        self.file_compressor.compress_files(f"{self.save_directory}/anexos.zip")

    def close_browser(self):
        try:
            time.sleep(2)
            self.driver.quit()
        except Exception as e:
            raise ValueError(f"Error closing the browser: {e}")
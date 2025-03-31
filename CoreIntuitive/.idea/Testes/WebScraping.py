import os
import requests
import zipfile
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class WebScraping:
    def __init__(self, url, save_directory):
        self.url = url
        self.save_directory = save_directory  
        self.driver = self.init_driver()

    def init_driver(self):
        
        try:
            chrome_options = Options()
            chrome_options.headless = True
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            
            return driver
        except Exception as e:
            raise ValueError(f"Error with the WebDriver: {e}")

    def acessing_site(self):
        
        try:
            self.driver.get(self.url)
            self.driver.implicitly_wait(10)
            
        except Exception as e:
            raise ValueError(f"Error accessing the site: {e}")

    def downloading_files(self, urls):
        
        try:

            if not os.path.exists(self.save_directory):
                os.makedirs(self.save_directory)

            for url in urls:
                file_name = url.split('/')[-1]
                file_path = os.path.join(self.save_directory, file_name)  
                
                response = requests.get(url)
                if response.status_code == 200:
                    with open(file_path, 'wb') as file:
                        file.write(response.content)
                    print(f"File downloaded: {file_name}")
                else:
                    print(f"Failed to download {url}. HTTP Status: {response.status_code}")

            print("Downloading files succeeded!")
        except Exception as e:
            raise ValueError(f"Error downloading files: {e}")


    def compressing_files(self):
        
        try:
            zip_path = os.path.join(self.save_directory, 'anexos.zip') 
            
            with zipfile.ZipFile(zip_path, 'w') as zip_file:
                for file in os.listdir(self.save_directory):
                    if file.endswith('.pdf'):
                        zip_file.write(os.path.join(self.save_directory, file), file)  
                        
            print("Files compressed!")
            
            print(f"O script está sendo executado no diretório: {self.save_directory}")
            
        except Exception as e:
            raise ValueError(f"Error compressing files: {e}")
        

    def closing_table(self):
        try:
            time.sleep(2)
            self.driver.quit()
        except Exception as e:
            raise ValueError(f"Error closing the browser: {e}")

        
def main():
    save_directory = './downloaded_files'  
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    web_scraper = WebScraping(url, save_directory)
    web_scraper.acessing_site()

    files_urls = [
        'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf', 
        'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf'
    ]

    web_scraper.downloading_files(files_urls)
    web_scraper.compressing_files()
    web_scraper.closing_table()

    return save_directory  

save_directory = main()



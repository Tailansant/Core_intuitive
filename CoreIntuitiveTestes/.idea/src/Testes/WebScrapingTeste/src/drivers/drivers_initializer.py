from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class DriverInitializer:
    def __init__(self):
        self.driver = None

    def init_driver(self):
        chrome_options = Options()
        chrome_options.headless = True
        
        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            return self.driver
        except Exception as e:
            raise ValueError(f"Error initializing the WebDriver: {e}")
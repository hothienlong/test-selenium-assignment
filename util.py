from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Util:
    def __init__(self, *args, **kwargs):
        options = Options()
        options.add_argument("--ignore-certificate-errors")
        # options.add_argument("start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        
    def go_to_main_page(self):
        self.driver.get('https://vnexpress.net/')
        
    def click_element(self, ele):
        ele.click()
        
    def get_title(self):
        self.driver.get('https://vnexpress.net/')
        return self.driver.title
        

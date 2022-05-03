from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Util:
    def __init__(self, *args, **kwargs):
        options = Options()
        options.add_argument("--ignore-certificate-errors")
        # options.add_argument("start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        
    def go_to_main_page(self):
        self.driver.get('https://tinhte.vn/')
        
    def click_element(self, byType, eleValue):
        self.driver.find_element(byType, eleValue).click()
        
    def get_title(self):
        self.go_to_main_page()
        return self.driver.title
    
    # --- By ----
    # ID = "id"
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"
    def set_text(self, byType: By, eleValue: str, text: str):
        self.driver.find_element(byType, eleValue).clear()
        self.driver.find_element(byType, eleValue).send_keys(text)
        
        
        

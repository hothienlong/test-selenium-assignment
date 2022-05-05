from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class Util:
    def __init__(self, *args, **kwargs):
        options = Options()
        options.add_argument("--ignore-certificate-errors")
        # options.add_argument("start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        
    def go_to_main_page(self):
        self.driver.get('https://tinhte.vn/')
    
    def go_to_signup_page(self):
        self.driver.get('https://tinhte.vn/register/')
        
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
        try:
            self.driver.find_element(byType, eleValue).clear()
            self.driver.find_element(byType, eleValue).send_keys(text)
            print("set text: %s" % text)
        except NoSuchElementException:
            print('Error:', 'Element not found')
            
    # def check_field_required(self, byType: By, inputEleValue: str):
    #     try:
    #         element = self.driver.find_element(byType, f"//input[@id='{inputEleValue}' and @required]")
    #         print(inputEleValue)
    #         print(element)
    #         print(element.is_displayed)
    #         return element.is_displayed
    #     except NoSuchElementException:
    #         print('Error:', 'Element not found')
            
    def get_HTML5_validation_message(self, byType: By, inputEleValue: str):
        try:
            element = self.driver.find_element(byType, inputEleValue)
            return self.driver.executeScript("return arguments[0].validationMessage;", element)
        except NoSuchElementException:
            print('Error:', 'Element not found')
            
    def get_form_error(self):
        try:
            error_form_selector = '.TinhteMods_Form_Error > div > span'
            
            error_form_message = self.driver.find_element(
                By.CSS_SELECTOR, error_form_selector).get_attribute('innerHTML')
            
            print(error_form_message)
            return error_form_message
        except NoSuchElementException:
            print('Error:', 'Element not found')
            

    def sign_in(self, email, password):
        self.go_to_main_page()
        time.sleep(1)
        menu_btn_ele_value = "//button[@type='button']"
        self.click_element(By.XPATH, menu_btn_ele_value)
        
        self.driver.implicitly_wait(1)
        
        go_to_sign_in_ele_value = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div > div > div > ul > li:nth-child(1) > a'
        self.click_element(By.CSS_SELECTOR, go_to_sign_in_ele_value)
        
        email_field = 'ctrl_pageLogin_login2'
        password_field = 'ctrl_pageLogin_password2'
        # set field to signup
        self.set_text(By.ID, email_field, email)
        self.set_text(By.ID, password_field, password)
        
        # click signup button
        sign_in_button_selector = '#content > div > div > div > div > form > div.TinhteMods_Form_Wrapper > input.button.primary'
        self.click_element(By.CSS_SELECTOR, sign_in_button_selector)

        
        
        

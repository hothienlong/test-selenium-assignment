# https://cuccode.com/python_virtual_environment.html
import unittest
import time
from util import Util
from selenium.webdriver.common.by import By

util = Util()

class SignUpPage:
    def sign_up(self, name, email, password, confirmPassWord):
        util.go_to_main_page()
        time.sleep(1)
        menuBtnEleValue = "//button[@type='button']"
        util.click_element(By.XPATH, menuBtnEleValue)
        
        util.driver.implicitly_wait(1)
        
        goToSignUpPageEleValue = "//a[contains(text(),'Đăng ký tài khoản mới')]"
        util.click_element(By.XPATH, goToSignUpPageEleValue)
        
        nameField = "//input[@placeholder='Tên']"
        emailField = "//input[@placeholder='Email']"
        passwordField = "//input[@placeholder='Mật khẩu']"
        confirmPasswordField = "//input[@placeholder='Xác nhận mật khẩu']"
        # set field to signup
        util.setText(By.XPATH, nameField, name)
        util.setText(By.XPATH, emailField, email)
        util.setText(By.XPATH, passwordField, password)
        util.setText(By.XPATH, confirmPasswordField, confirmPassWord)
        
        # click signup button
        
        

class SignUpTest(unittest.TestCase):
    signupPage = SignUpPage()
    
    def test_signup1(self):
        # util.go_to_main_page()
        # time.sleep(1)
        
        # menuBtnEleValue = "//button[@type='button']"
        # util.click_element(By.XPATH, menuBtnEleValue)
        
        # util.driver.implicitly_wait(1)
        
        # goToSignUpPageEleValue = "//a[contains(text(),'Đăng ký tài khoản mới')]"
        # util.click_element(By.XPATH, goToSignUpPageEleValue)
        
        self.signupPage.sign_up("thienlong", "thienlong460@gmail.com", "123456", "123456")
        
        


if __name__ == "__main__":
    unittest.main(verbosity=2)
    util.driver.quit()
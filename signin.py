# https://cuccode.com/python_virtual_environment.html
import unittest
import time
from util import Util
from selenium.webdriver.common.by import By

util = Util()

class SignInPage:
    def signIn(self, email, password):
        util.go_to_main_page()
        time.sleep(1)
        menuBtnEleValue = "//button[@type='button']"
        util.click_element(By.XPATH, menuBtnEleValue)
        
        util.driver.implicitly_wait(1)
        
        goToSignInEleValue = '#__next > div.root > header > div > div > div.jsx-3599443646.col-right.right > div > div > div > div > ul > li:nth-child(1) > a'
        util.click_element(By.CSS_SELECTOR, goToSignInEleValue)
        
        emailField = 'ctrl_pageLogin_login2'
        passwordField = 'ctrl_pageLogin_password2'
        # set field to signup
        util.set_text(By.ID, emailField, email)
        util.set_text(By.ID, passwordField, password)
        
        # click signup button
        signInButtonSelector = '#content > div > div > div > div > form > div.TinhteMods_Form_Wrapper > input.button.primary'
        util.click_element(By.CSS_SELECTOR, signInButtonSelector)


        
        

class SignUpTest(unittest.TestCase):
    signupPage = SignInPage()
    
    def testSignIn1(self):
        self.signupPage.signIn("dang.nguyen.100420@hcmut.edu.vn", "Xxt]jdoxX0410")
        


if __name__ == "__main__":
    unittest.main(verbosity=2)
    util.driver.quit()
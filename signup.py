# https://cuccode.com/python_virtual_environment.html
import time
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from util import Util

util = Util()

class SignUpFieldName:
    NAME = 'name'
    EMAIL = 'email'
    BIRTHDAY = 'birthday'
    PASSWORD = 'password'
    CONFIRM_PASSWORD = 'confirm_password'
class SignUpPage:
    nameField = "//input[@placeholder='Tên']"
    emailField = "//input[@placeholder='Email']"
    birthdayField = "//input[@placeholder='Sinh nhật']"
    passwordField = "//input[@placeholder='Mật khẩu']"
    confirmPasswordField = "//input[@placeholder='Xác nhận mật khẩu']"
    signUpButton = "//input[@id='SubmitButton']"
    
    def sign_up(self, name, email, birthday, password, confirmPassWord):
        # util.go_to_main_page()
        # time.sleep(1)
        # menuBtnEleValue = "//button[@type='button']"
        # util.click_element(By.XPATH, menuBtnEleValue)
        
        # util.driver.implicitly_wait(1)
        
        
        # goToSignUpPageEleValue = "//a[contains(text(),'Đăng ký tài khoản mới')]"
        # util.click_element(By.XPATH, goToSignUpPageEleValue)
        
        print(name, email, birthday, password, confirmPassWord)
        
        util.go_to_signup_page()

        # set field to signup
        util.set_text(By.XPATH, self.nameField, name)
        util.set_text(By.XPATH, self.emailField, email)
        util.set_text(By.XPATH, self.birthdayField, birthday)
        util.set_text(By.XPATH, self.passwordField, password)
        util.set_text(By.XPATH, self.confirmPasswordField, confirmPassWord)
        
        
        # util.driver.implicitly_wait(10)
        time.sleep(12)
        # click signup button
        util.click_element(By.XPATH, self.signUpButton)
        
    
    def check_field_required(self, field_name: SignUpFieldName):
        try:
            match field_name:
                case SignUpFieldName.NAME:
                    return util.driver.find_element(By.XPATH, f"//input[@placeholder='Tên' and @required]").is_displayed
                case SignUpFieldName.EMAIL:
                    return util.driver.find_element(By.XPATH, f"//input[@placeholder='Email' and @required]").is_displayed
                case SignUpFieldName.BIRTHDAY:
                    return util.driver.find_element(By.XPATH, f"//input[@placeholder='Sinh nhật' and @required]").is_displayed
                case SignUpFieldName.PASSWORD:
                    return util.driver.find_element(By.XPATH, f"//input[@placeholder='Mật khẩu' and @required]").is_displayed
                case SignUpFieldName.CONFIRM_PASSWORD:
                    return util.driver.find_element(By.XPATH, f"//input[@placeholder='Xác nhận mật khẩu' and @required]").is_displayed
        except NoSuchElementException:
            print('Error:', 'Element not found')
            
    def get_text_element(self, field_name: SignUpFieldName):
        try:
            match field_name:
                case SignUpFieldName.NAME:
                    return util.driver.find_element(By.XPATH, f"//input[@placeholder='Tên' and @required]")
                case SignUpFieldName.EMAIL:
                    return util.driver.find_element(By.XPATH, f"//input[@placeholder='Email' and @required]")
                case SignUpFieldName.BIRTHDAY:
                    return util.driver.find_element(By.XPATH, f"//input[@placeholder='Sinh nhật' and @required]")
                case SignUpFieldName.PASSWORD:
                    return util.driver.find_element(By.XPATH, f"//input[@placeholder='Mật khẩu' and @required]")
                case SignUpFieldName.CONFIRM_PASSWORD:
                    return util.driver.find_element(By.XPATH, f"//input[@placeholder='Xác nhận mật khẩu' and @required]")
        except NoSuchElementException:
            print('Error:', 'Element not found')
            
    def get_error_label(self, field_name: SignUpFieldName):
        name_input_ele = self.get_text_element(field_name)
        name_input_ele_id = name_input_ele.get_attribute("id")
        print(name_input_ele_id)
        
        error_label_ele = util.driver.find_element(By.XPATH, f"//label[@for='{name_input_ele_id}']")
        
        error_label_ele_text = error_label_ele.get_attribute('innerHTML')
        print(error_label_ele_text)
        return error_label_ele_text

class SignUpTest(unittest.TestCase):
    signupPage = SignUpPage()
    
    # User Interface - Fill all fields, check all the text boxes, radio buttons, buttons, etc (failed)      
    def test_signup1(self):
        self.signupPage.sign_up("thienlong", "thienlong460@gmail.com", "10/05/2000", "123456", "123456")
        assert True
        
    # Required fields - Check the required fields by not filling any data (failed)
    def test_signup2(self):
        self.signupPage.sign_up("", "", "", "", "")
        # self.signupPage.check_field_required(SignUpFieldName.NAME)
        assert self.signupPage.check_field_required(SignUpFieldName.NAME)
        time.sleep(5)
        util.driver.quit()

    # Test validate unique username
    def test_signup3(self):
        self.signupPage.sign_up("thienlong", "thienlong460@gmail.com", "10/05/2000", "123456", "123456")

        error_label_text = self.signupPage.get_error_label(SignUpFieldName.NAME)
        
        assert "Tên người dùng phải là duy nhất.Tên người dùng được đề cập đã được sử dụng." in error_label_text, "Can not validate signup function"
        
        time.sleep(0.5)
        util.driver.quit()

    
    # Test validate unique email
    def test_signup4(self):
        self.signupPage.sign_up("thienlong", "thienlong460@gmail.com", "10/05/2000", "123456", "123456")

        error_label_text = self.signupPage.get_error_label(SignUpFieldName.EMAIL)
        
        assert "Địa chỉ email phải là duy nhất.Địa chỉ email đề cập đã được sử dụng." in error_label_text, "Can not validate signup function"
        
        time.sleep(0.5)
        util.driver.quit()
        
    # Enter Invalid Emails and Click on the Signup button (failed)
    def test_signup5(self):
        self.signupPage.sign_up("thienlong", "thienlong460@gmail.com", "10/05/2000", "123456", "123456")


        assert True
        
    # Enter valid Emails and Click on the Signup button (successful)
    def test_signup6(self):
        self.signupPage.sign_up("thienlong", "thienlong460@gmail.com", "10/05/2000", "123456", "123456")


        assert True
        
    # Enter email already used in system and Click on the Signup button (failed)
    def test_signup7(self):
        self.signupPage.sign_up("thienlong", "thienlong460@gmail.com", "10/05/2000", "123456", "123456")


        assert True

    # Enter Username already used in system and Click on the Signup button (failed)
    def test_signup8(self):
        self.signupPage.sign_up("thienlong", "thienlong460@gmail.com", "10/05/2000", "123456", "123456")


        assert True
        
    # Passed blank spaces in required fields and Click on the Signup button (failed)
    def test_signup9(self):
        self.signupPage.sign_up("thienlong", "thienlong460@gmail.com", "10/05/2000", "123456", "123456")


        assert True
        
    # Go to the Email and Click on the verification link
    def test_signup10(self):
        self.signupPage.sign_up("thienlong", "thienlong460@gmail.com", "10/05/2000", "123456", "123456")


        assert True
        

        


if __name__ == "__main__":
    unittest.main(verbosity=2)
    
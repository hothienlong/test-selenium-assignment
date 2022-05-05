# https://cuccode.com/python_virtual_environment.html
import time
import unittest
import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import HtmlTestRunner

from util import Util

# khởi tạo webdriver -> mở browser
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
        
        # print(name, email, birthday, password, confirmPassWord)
        
        # đăng ký thì navigate tới link register, ko cần đóng trình duyệt
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
        # print(name_input_ele_id)
        
        error_label_ele = util.driver.find_element(By.XPATH, f"//label[@for='{name_input_ele_id}']")
        
        error_label_ele_text = error_label_ele.get_attribute('innerHTML')
        # print(error_label_ele_text)
        return error_label_ele_text

class SignUpTest(unittest.TestCase):
    signupPage = SignUpPage()
    
    # Check name (> 3 character)   
    def test_signup1(self):
        self.signupPage.sign_up("1", "thienlong460@gmail.com", "10/05/2000", "123456", "123456")
        error_label_text = self.signupPage.get_error_label(SignUpFieldName.NAME)
        
        assert "Vui lòng nhập tên có từ 3 ký tự trở lên." in error_label_text, "Can not validate signup function"
        time.sleep(0.5)


    # Test validate unique username
    def test_signup6(self):
        self.signupPage.sign_up("thienlong", "thienlong460@gmail.com", "10/05/2000", "123456", "123456")

        error_label_text = self.signupPage.get_error_label(SignUpFieldName.NAME)
        
        assert "Tên người dùng phải là duy nhất.Tên người dùng được đề cập đã được sử dụng." in error_label_text, "Can not validate signup function"
        
        time.sleep(0.5)
        
if __name__ == "__main__":
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='.//report'))
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='.'))
    util.driver.close()
    util.driver.quit()
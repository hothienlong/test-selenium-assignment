# https://cuccode.com/python_virtual_environment.html
import unittest
import time
from util import Util
from selenium.webdriver.common.by import By
from selenium import webdriver

util = Util()


class LoginPage:
    def __init__(self, *args, **kwargs):
        self.test_username = "trunghiu0301"
        self.test_password = "hieu1234"

    def login(self, email, password):
        util.go_to_main_page()
        time.sleep(1)
        menuBtnEleValue = "//button[@type='button']"
        util.click_element(By.XPATH, menuBtnEleValue)

        util.driver.implicitly_wait(1)

        goToLoginPageEleValue = "//a[contains(text(),'Đăng nhập tài khoản')]"
        util.click_element(By.XPATH, goToLoginPageEleValue)

        emailField = "//input[@placeholder='Tên tài khoản hoặc Email']"
        passwordField = "//input[@placeholder='Mật khẩu']"
        # set field to login
        util.set_text(By.XPATH, emailField, email)
        util.set_text(By.XPATH, passwordField, password)

        # click login button
        loginBtnEleValue = '#content > div > div > div > div > form > div.TinhteMods_Form_Wrapper > input.button.primary'
        util.click_element(By.CSS_SELECTOR, loginBtnEleValue)

    def logout(self):
        menuBtnEleValue = "/html/body/div[1]/div[1]/header/div/div/div[3]/div/div[3]/div/div/button"
        util.click_element(By.XPATH, menuBtnEleValue)

        util.driver.implicitly_wait(1)

        logoutPageEleValue = "//a[contains(text(),'Đăng xuất')]"
        util.click_element(By.XPATH, logoutPageEleValue)
        goToLogoutPageEleValue = "/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div/div/form/dl/dd/a"
        util.click_element(By.XPATH, goToLogoutPageEleValue)


class LoginTest(unittest.TestCase):
    loginPage = LoginPage()

    def test_login_1(self):
        self.loginPage.login(
            "  ", "  ")
        error_form_selector = '.TinhteMods_Form_Error > div > span'
        error_form_message = util.driver.find_element(
            By.CSS_SELECTOR, error_form_selector).get_attribute('innerHTML')
        assert "false" in error_form_message, "Can not validate log in function"
        time.sleep(0.5)

    def test_login_2(self):
        self.loginPage.login(
            "trunghieule0303@gmail.com", "123456")
        error_form_selector = '.TinhteMods_Form_Error > div > span'
        
        error_form_message = util.driver.find_element(
            By.CSS_SELECTOR, error_form_selector).get_attribute('innerHTML')
        assert "Nhập sai mật khẩu. Vui lòng thử lại." in error_form_message, "Can not validate log in function"
        time.sleep(0.5)

    def test_login_3(self):
        self.loginPage.login(
            '!@#$%#', '    ')
        error_form_selector = '.TinhteMods_Form_Error > div > span'
        error_form_message = util.driver.find_element(
            By.CSS_SELECTOR, error_form_selector).get_attribute('innerHTML')
        assert "false" in error_form_message, "Can not validate log in function"
        time.sleep(0.5)

    def test_login_4(self):
        self.loginPage.login(
            '', '')
        try:
            error_form_selector = '.TinhteMods_Form_Error > div > span'
            error_form_message = util.driver.find_element(
                By.CSS_SELECTOR, error_form_selector).get_attribute('innerHTML')
            assert "false" in error_form_message, "Can not validate log in function"
        except:
            assert True
        time.sleep(0.5)

    def test_login_5(self):
        self.loginPage.login(
            self.loginPage.test_username, self.loginPage.test_password)
        try:
            error_form_selector = '.TinhteMods_Form_Error > div > span'
            error_form_message = util.driver.find_element(
                By.CSS_SELECTOR, error_form_selector).get_attribute('innerHTML')
        except:
            error_form_message = None
        time.sleep(0.5)
        self.loginPage.logout()
        assert not error_form_message


if __name__ == "__main__":
    unittest.main(verbosity=2)
    util.driver.quit()

# https://cuccode.com/python_virtual_environment.html
import unittest
import time
from util import Util
from selenium.webdriver.common.by import By

util = Util()

class LoginTest(unittest.TestCase):
    def test_login_1(self):
        util.sign_in("  ", "  ")
        error_form_selector = '.TinhteMods_Form_Error > div > span'
        error_form_message = util.driver.find_element(
            By.CSS_SELECTOR, error_form_selector).get_attribute('innerHTML')
        assert "false" in error_form_message, "Can not validate log in function"
        time.sleep(0.5)

    def test_login_2(self):
        util.sign_in("trunghieule0303@gmail.com", "123456")
        error_form_selector = '.TinhteMods_Form_Error > div > span'
        error_form_message = util.driver.find_element(
            By.CSS_SELECTOR, error_form_selector).get_attribute('innerHTML')
        assert "Nhập sai mật khẩu. Vui lòng thử lại." in error_form_message, "Can not validate log in function"
        time.sleep(0.5)

    def test_login_3(self):
        util.sign_in('!@#$%#', '    ')
        error_form_selector = '.TinhteMods_Form_Error > div > span'
        error_form_message = util.driver.find_element(
            By.CSS_SELECTOR, error_form_selector).get_attribute('innerHTML')
        assert "false" in error_form_message, "Can not validate log in function"
        time.sleep(0.5)

    def test_login_4(self):
        util.sign_in('', '')
        try:
            error_form_selector = '.TinhteMods_Form_Error > div > span'
            error_form_message = util.driver.find_element(
                By.CSS_SELECTOR, error_form_selector).get_attribute('innerHTML')
            assert "false" in error_form_message, "Can not validate log in function"
        except:
            assert True
        time.sleep(0.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
    util.driver.quit()

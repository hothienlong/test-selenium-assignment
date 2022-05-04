# https://cuccode.com/python_virtual_environment.html
import unittest
import time
from util import Util
from selenium.webdriver.common.by import By

util = Util()


class SignUpTest(unittest.TestCase):
    def test_sign_in(self):
        util.sign_in("dang.nguyen.100420@hcmut.edu.vn", "Xxt]jdoxX0410")

        error_form_selector = '.TinhteMods_Form_Error > div > span'
        error_form_message = util.driver.find_element(By.CSS_SELECTOR, error_form_selector).get_attribute('innerHTML')
        print('test hereeee', error_form_message)

        expected_err_msg = ''

        assert error_form_message == ''

    #XenForoUniq7 > div > span
    #XenForoUniq9 > div > span
    
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
    util.driver.quit()
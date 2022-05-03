# https://cuccode.com/python_virtual_environment.html
import unittest
import time
from util import Util
from selenium.webdriver.common.by import By

util = Util()

class MainTest(unittest.TestCase):
    def test_go_to_main(self):
        util.go_to_main_page()
        time.sleep(1)
        
        assert True
        
    def test_get_title(self):
        expected = 'Tinhte.vn - MXH Hỏi đáp, Review, Thông tin công nghệ'
        
        result = util.get_title()
                
        assert result == expected
        
    def test_set_text_search(self):
        util.go_to_main_page()
        searchEleValue = "//div[@role='button']"
        util.click_element(By.XPATH, searchEleValue)
        
        inputSearchEleValue = "//input[@placeholder='Nhập gì đó để tìm...']"
        util.set_text(By.XPATH, inputSearchEleValue, "thienlong search")
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
    util.driver.quit()
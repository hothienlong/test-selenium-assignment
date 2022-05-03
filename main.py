# https://cuccode.com/python_virtual_environment.html
import unittest
import time
from util import Util

util = Util()

class MainTest(unittest.TestCase):
    def test_go_to_main(self):
        util.go_to_main_page()
        time.sleep(1)
        
        self.assertTrue('PYTHON'.islower())
        
    def test_get_title(self):
        expected = 'VnExpress - Báo tiếng Việt nhiều người xem nhất'
        
        result = util.get_title()
        print(result)
        assert result == expected


if __name__ == "__main__":
    # HTMLTestRunner.main()
    unittest.main(verbosity=2)
    util.driver.close()
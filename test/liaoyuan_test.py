import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

class ResumeTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        driver.close()
        pass

    def test_name_should_exist(self):
        driver.get("http://www.google.com")
        sleep(2)
        driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys("燎原")
        sleep(3)
        driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
        sleep(3)
        
        while True:
            try:
                driver.find_element_by_css_selector('a[href*="https://liaoyuan.io/"]').click()
                break
            
            except:
                driver.find_element_by_css_selector('#pnnext').click()

if __name__ == "__main__":
    unittest.main() # run all tests

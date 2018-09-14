import unittest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

class ResumeTestCase(unittest.TestCase):
     def setUp(self):
         driver.get("http://www.google.com")

     def tearDown(self):
         pass

     def test_school_test_should_exist(self):
         school_text = driver.find_element_by_css_selector('p').text
         assert school_text == 'school', "can't find school text"

if __name__ == "__main__":
      unittest.main() # run all tests
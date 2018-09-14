import unittest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

class ResumeTestCase(unittest.TestCase):
     def setUp(self):
         driver.get("http://localhost:8000")

     def tearDown(self):
         driver.close()
         pass

     def test_name_should_exist(self):
         name_text = driver.find_element_by_css_selector('.title h1').text
         assert name_text == 'Sike Dong (Christina)', "can't find name text"

     def xtest_school_should_exist(self):
         school_selector = 'div.school'
         school_text = driver.find_element_by_css_selector(school_selector).text
         assert school_text.lower == 'northeast', "can't find school text"


if __name__ == "__main__":
      unittest.main() # run all tests
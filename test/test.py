import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import page

class TestLiaoyuan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.get("http://lancer.host.3rdex.com/#poster")

    def tearDown(self):
        self.driver.close()
        pass

    def xtest_3rdex(self):
        main_page = page.main_3rdex(self.driver)
        main_page.verify_3rdex()
        main_page.click_button()

        eos_page = page.ram_eos_page(self.driver)
        eos_page.verify_ram_eos()
        eos_page.click_create()

    def test_3rdex_login(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        signup_page.name_generation()
        signup_page.name_text()


if __name__ == "__main__":
    unittest.main() # run all tests

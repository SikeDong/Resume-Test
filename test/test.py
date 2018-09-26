import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import page

class TestLiaoyuan(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
        driver.get("http://www.google.com")


    def test_search_liaoyuan(self):
        main_page = google_main_page.get_main_page(self.driver)
        text_input = google_main_page.search_input("燎原")
        google_main_page.click_search_button(self.driver)
        result_page = google_result_page(self.driver)
        get_liaoyuan = liaoyuan_main_page(self.driver)

    def tearDown(self):
        driver.close()
        pass


if __name__ == "__main__":
    unittest.main() # run all tests

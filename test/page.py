mport unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import page

class Basepage(object):
    def __init__(self,driver):
        self.driver = driver

class google_main_page(Basepage):
    def get_main_page(self):
        return "http://www.google.com"
    sleep(2)

    def search_input(self, text):
        search_input = find_element_by_css_selector('.gLFyf.gsfi').send_keys(text)
    sleep(3)

    def click_search_button(self):
        click = find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
    sleep(3)

    """def search(self, keyword):
        self.search_input(keyword)
        googleresultpage(self.browser).wait_for_page()"""

class google_result_page(Basepage):
    def result_on_page(self):
        while True:
            try:
                driver.find_element_by_css_selector('a[href*="https://liaoyuan.io/"]').click()
                break
            
            except:
                driver.find_element_by_css_selector('#pnnext').click()

class liaoyuan_main_page(Basepage):
    def liaoyuan_open(self):
        return "https://liaoyuan.io/"
        sleep(20)



mport unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import page

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

""" class Basepage(object):
    def __init__(self,driver):
        self.driver = driver """

class google_main_page(page):
    def get_main_page(self):
        return "http://www.google.com"
    sleep(2)

    def search_input(self, keyword):
        search_input = find_element_by_css_selector('.gLFyf.gsfi').send_keys(keyword)
    sleep(3)

    def click_search_button(self):
        click = find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
    sleep(3)

    def search(self, keyword):
        self.search_input(keyword)
        self.click_search_button()
        googleresultpage(self.browser).wait_for_page()

class google_result_page(page):
    def result_on_page(self):
        while True:
            try:
                driver.find_element_by_css_selector('a[href*="https://liaoyuan.io/"]').click()
                break
            
            except:
                driver.find_element_by_css_selector('#pnnext').click()

class liaoyuan_main_page(page):
    def liaoyuan_open(self):
        ## driver.find_element_by_css_selector('a[href*="https://liaoyuan.io/"]')
        sleep(20)



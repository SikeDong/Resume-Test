import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import page

class Basepage(object):
    def __init__(self,driver):
        self.driver = driver

class google_main_page(Basepage):
    def search_input(self, text):
        self.driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(text)
    sleep(3)

    def click_search_button(self):
        self.driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
    sleep(3)

class google_result_page(Basepage):
    def search_liaoyuan(self):
        while True:
            try:
                self.driver.find_element_by_css_selector('a[href*="https://liaoyuan.io/"]').click()
                break
            
            except:
                self.driver.find_element_by_css_selector('#pnnext').click()

class liaoyuan_main_page(Basepage):
    def verify_liaoyuan(self):

        liaoyuan_title = self.driver.find_element_by_css_selector('head > title').text
        assert liaoyuan_title == '「燎原」', "can't find the title"
        liaoyuan_logo = self.driver.find_element_by_css_selector('body > div > img .logo')
        assert liaoyuan_logo == '', "can't find the logo"
        
        sleep(20)

        

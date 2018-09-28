import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import page

class Basepage(object):
    def __init__(self,driver):
        self.driver = driver
    
    def wait_locator(self,locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

class google_main_page(Basepage):
    def search_input(self, text):
        self.driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(text)
        sleep(2)

    def click_search_button(self):
        self.driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
        sleep(2)

class google_result_page(Basepage):
    def search_liaoyuan(self):
        while True:
            try:
                self.driver.find_element_by_css_selector('a[href*="https://liaoyuan.io/"]').click()
                break
            
            except:
                self.driver.find_element_by_css_selector('#pnnext').click()

class liaoyuan_main_page(Basepage):
    url = 'https://liaoyuan.io/'
    title_locator = (By.TAG_NAME, 'head > title')
    logo_locator = (By.CSS_SELECTOR, 'body > div > img[alt = "「燎原」"')
    login_button_locator = (By.LINK_TEXT,'登录')

    def verify_liaoyuan(self):
        assert self.driver.current_url == 'https://liaoyuan.io/', "cannot find liaoyuan"
        liaoyuan_title = self.wait_locator(self.title_locator)
        liaoyuan_logo = self.wait_locator(self.logo_locator) 

    def click_login_button(self):
        login = self.wait_locator(self.login_button_locator)
        print(login)
        login.click()
        sleep(2)

 ##class login_page(Basepage):
    

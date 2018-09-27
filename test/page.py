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
    
    def wait_locator(locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

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
    url = 'https://liaoyuan.io/'
    title_locator = (By.CSS_SELECTOR, 'head > title')
    logo_locator = (By.CSS_SELECTOR,'body > div > img[alt = "「燎原」"')

    def verify_liaoyuan(self):
        try:
            liaoyuan_url = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'https://liaoyuan.io/')))
            liaoyuan_title = wait_locator((self.title_locator))
            liaoyuan_logo = wait_locator((self.logo_locator))
        
        except TimeoutException:
            print("Cannot open Liaoyuan")

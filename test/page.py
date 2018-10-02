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
    logo_locator = (By.CSS_SELECTOR, 'div > img[alt = "「燎原」"]')
    login_button_locator = (By.LINK_TEXT,'登录')

    def verify_liaoyuan(self):
        assert self.driver.current_url == 'https://liaoyuan.io/', "cannot find liaoyuan"
        liaoyuan_title = self.driver.title
        liaoyuan_logo = self.wait_locator(self.logo_locator) 

    def click_login(self):
        self.wait_locator(self.login_button_locator)
        login = self.driver.find_element(*self.login_button_locator)
        login.click()
        sleep(2)
    
class login_page(Basepage):
    login_url = 'https://liaoyuan.io/login/'
    liaoyuan_username = (By.CSS_SELECTOR,'input[type="email"]')
    liaoyuan_password = (By.CSS_SELECTOR,'input[type="password"]')
    login_liaoyuan_button = (By.CSS_SELECTOR,'.action-wrapper')

    """def verify_login_page(self):
        print('current_url:', self.driver.current_url)
        assert self.driver.current_url == 'https://liaoyuan.io/login/', 'cannot open login page'"""

    def login_username(self,username):
        self.wait_locator(self.liaoyuan_username)
        login_liaoyuan_username = self.driver.find_element(*self.liaoyuan_username)
        login_liaoyuan_username.send_keys(username)
        sleep(2)
        
    def login_password(self,password):
        self.wait_locator(self.liaoyuan_password)
        login_liaoyuan_password = self.driver.find_element(*self.liaoyuan_password)
        login_liaoyuan_password.send_keys(password)
        sleep(2)
    
    def click_login_liaoyuan(self):
        self.wait_locator(self.login_liaoyuan_button)
        login_button = self.driver.find_element(*self.login_liaoyuan_button)
        print("login button:", login_button)
        login_button.click()
        sleep(2)

class login_main_page(Basepage):
    url = "https://liaoyuan.io/profession/"
    
    def verify_login_main_page(self):
        assert self.driver.current_url == 'https://liaoyuan.io/profession/', "cannot login"


    

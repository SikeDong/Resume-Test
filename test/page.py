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
    logo_locator = (By.CSS_SELECTOR, 'div > img[alt = "「燎原」"')
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
    login_username = (By.LINK_TEXT,'邮箱')
    login_password = (By.LINK_TEXT,'密码')
    liaoyuan_login_button_locator = (By.LINK_TEXT,'登录')

    def verify_login_page(self):
        print(self.driver.current_url)
        assert self.driver.current_url == 'https://liaoyuan.io/login/', 'cannot open login page'

    def login_username(self,username):
        ##login.username = self.driver.find_element_by_link_text('邮箱').send_keys(username)
        liaoyuan_login_username = self.wait_locator(self.login_username)
        liaoyuan_login_username.send_keys(username)
        assert login.username == "username","不存在该用户名"
        sleep(2)
        
    def login_password(self,password):
        ##login.password = self.driver.find_element_by_link_text('密码').send_keys(password)
        liaoyuan_login_password = self.wait_locator(self.login_password)
        liaoyuan_login_password.send_keys(password)
        assert login.password =="password", "密码不正确"
        sleep(2)
    
    def click_login_button(self):
        self.wait_locator(self.liaoyuan_login_button_locator)
        login_button_click = self.driver.find_element(*self.liaoyuan_login_button_locator)
        login_button_click.click()
        sleep(2)
    

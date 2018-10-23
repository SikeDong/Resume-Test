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

class main_3rdex(Basepage):
    url = 'http://lancer.host.3rdex.com/#poster'
    logo_locator = (By.CSS_SELECTOR, 'div > a > img[alt = "3rdex"]') 

    def verify_3rdex(self):
        assert self.driver.current_url == 'http://lancer.host.3rdex.com/#poster', "cannot find 3rdex"
        page_logo = self.wait_locator(self.logo_locator)

    def click_button(self):
        start_exchange = self.driver.find_element_by_css_selector('.src-Screens-Landing-___PosterSection__ram-exchange-beta-btn___3j2NU')
        start_exchange.click()
        sleep(2)

class ram_eos_page(Basepage):
    url = 'http://lancer.host.3rdex.com/ram-eos'
    eos_logo_locator = (By.CSS_SELECTOR, '.src-Components-___SideNav__app-logo___2pFZc')
    market_price_chart_locator = (By.CSS_SELECTOR, '.src-Components-RamExchange-___RamPriceHistory__ram-price-history-container___2DJXK') 
    hidden_component_locator = (By.CSS_SELECTOR, 'div > section.hide-lt-md.src-Components-___SideNav__app-side-nav___2zRkt') 
    signup_button_locator =(By.LINK_TEXT, 'Create Account')

    def verify_ram_eos(self):
        assert self.driver.current_url == 'http://lancer.host.3rdex.com/ram-eos', "cannot find ram eos"
        eos_logo = self.wait_locator(self.eos_logo_locator)
        ram_eos_market_chart = self.wait_locator(self.market_price_chart_locator) 
        ram_eos_hidden_component = self.wait_locator(self.hidden_component_locator)

    def click_create(self):
        self.wait_locator(self.signup_button_locator)
        signup = self.driver.find_element(*self.signup_button_locator)
        signup.click()
        sleep(2)
    
class signup_3rdex(Basepage):
    url = 'http://lancer.host.3rdex.com/account/create'
    signup_page_title = (By.LINK_TEXT,'New Account')
    eos_account_creation = (By.CSS_SELECTOR, '.color-text-primary')
    username_generation = (By.CSS_SELECTOR,'.src-Screens-___AccountScreen__random-generation___1g3pF > span')
    username_textfield = (By.CSS_SELECTOR, '.src-Components-Account-___AccountNameInput__input___1Ym0q')

    def verify_signup_page(self):
        assert self.driver.current_url == 'http://lancer.host.3rdex.com/account/create', "cannot find signup page"
        signup_title = self.wait_locator(self.signup_page_title)
        eos_account_exp = self.wait_locator(self.eos_account_creation) 

    def name_generation(self): 
        self.wait_locator(self.username_generation)
        new_username = self.driver.find_element(*self.username_generation)
        new_username.click()
        sleep(2)

    def name_text(self):  
        self.wait_locator(self.username_textfield)
        name_text_field = self.driver.find_element(*self.username_textfield)
        print (name_text_field.is_displayed())
        print(name_text_field.text)
        
   
 
    """def login_password(self,password):
        self.wait_locator(self.liaoyuan_password)
        login_liaoyuan_password = self.driver.find_element(*self.liaoyuan_password)
        login_liaoyuan_password.send_keys(password)
        sleep(2)
    
    def click_login_liaoyuan(self):
        self.wait_locator(self.login_liaoyuan_button)
        login_button = self.driver.find_element(*self.login_liaoyuan_button)
        login_button.click()
        sleep(2)

class login_main_page(Basepage):
    url = "https://liaoyuan.io/profession/"
    
    def verify_login_main_page(self):
        assert self.driver.current_url == 'https://liaoyuan.io/profession/', "cannot login"

class register_liaoyuan(Basepage):
    signup_page_title = ((By.CSS_SELECTOR,'.ng-binding'))
    signup_username = (By.CSS_SELECTOR,'input[type="email"]')
    signup_liaoyuan_button = (By.CSS_SELECTOR,'.action-wrapper')

    def verify_signup_page(self):
        self.wait_locator(self.signup_page_title)
        login_main_page = self.driver.find_element(*self.signup_page_title).text
        assert login_main_page == "注册", "cannot open login page"
    
    def register_username(self,username): 
        self.wait_locator(self.signup_username)
        signup_liaoyuan_username = self.driver.find_element(*self.signup_username)
        signup_liaoyuan_username.send_keys(username)
        sleep(2)

    def click_signup_liaoyuan(self):
        self.wait_locator(self.signup_liaoyuan_button)
        signup_button = self.driver.find_element(*self.signup_liaoyuan_button)
        signup_button.click()
        sleep(2)"""





    

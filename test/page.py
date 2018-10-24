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
    checkbox_click = (By.CSS_SELECTOR, "input[type='checkbox']")
    next_button = (By.CSS_SELECTOR, '.primary-button-container')

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
        return name_text_field.value
        sleep(2)
        
    def toast_text(self):
        pass

    def input_name(self, text):
        # change name input value
        pass
    
    def click_next(self):
        click_next = self.driver.find_element(*self.next_button)
        click_next.click()
    
    def click_agree_term(self):
        checkbox_selected = self.driver.find_element(*self.checkbox_click)
        checkbox_selected.click()
        
    def term_status(self):
        checkbox_selected = self.driver.find_element(*self.checkbox_click)
        #return checkbox_selected.checked?

    """def next_click(self):
        checkbox_selected = self.driver.find_element(*self.checkbox_click)
        checkbox_selected.click()
        self.wait_locator(self.next_button)
        click_next = self.driver.find_element(*self.next_button)
        click_next.click()

class generate_key(Basepage):
    url = 'http://lancer.host.3rdex.com/account/key-gen'
    key_page_title = (By.LINK_TEXT,'Enter your public key or click')
    key_pairs_exp = (By.CSS_SELECTOR, '.color-text-primary')

    def verify_key_page(self):
        assert self.driver.current_url == 'http://lancer.host.3rdex.com/account/key-gen', "cannot find key page"
        key_title = self.wait_locator(self.key_page_title)
        key_pairs = self.wait_locator(self.key_pairs_exp) """




    

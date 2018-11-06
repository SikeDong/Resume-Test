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

    def verify_3rdex_main_page(self):
        assert self.driver.current_url == 'http://lancer.host.3rdex.com/#poster', "cannot find 3rdex"
        page_logo = self.wait_locator(self.logo_locator)

    def start_exchange_button(self):
        start_change = self.driver.find_element_by_css_selector('.src-Screens-Landing-___PosterSection__ram-exchange-beta-btn___3j2NU')
        start_change.click()
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

    def click_create_account(self):
        self.wait_locator(self.signup_button_locator)
        start_signup = self.driver.find_element(*self.signup_button_locator)
        start_signup.click()
        sleep(2)
    
class signup_3rdex(Basepage):
    url = 'http://lancer.host.3rdex.com/account/create'
    signup_page_title = (By.CSS_SELECTOR,'.src-Screens-___AccountScreen__panel-title___E6XML')
    signup_explanation = (By.CSS_SELECTOR, '.src-Components-Account-___AccountStageInfo__account-info-stage-container___1SE9N')
    username_generation = (By.CSS_SELECTOR,'.src-Screens-___AccountScreen__random-generation___1g3pF > span')
    username_textfield = (By.CSS_SELECTOR, 'input.src-Components-Account-___AccountNameInput__input___1Ym0q')
    checkbox_click = (By.CSS_SELECTOR, "input[type='checkbox']")
    next_button_to_key = (By.CSS_SELECTOR, '.primary-button-container')
    toast_error_username = (By.CSS_SELECTOR, '.Toastify')

    def verify_signup_page(self):
        assert self.driver.current_url == 'http://lancer.host.3rdex.com/account/create', "cannot find signup page"
        signup_title = self.driver.find_element(*self.signup_page_title)
        eos_account_exp = self.driver.find_element(*self.signup_explanation) 

    def generate_username(self): 
        self.wait_locator(self.username_generation)
        new_username = self.driver.find_element(*self.username_generation)
        new_username.click()
        sleep(2)

    def get_username_text(self):  
        self.wait_locator(self.username_textfield)
        username_random_generation = self.driver.find_element(*self.username_textfield)
        return username_random_generation.get_attribute('value')

    def fill_in_username(self, text):
        self.wait_locator(self.username_textfield)
        name_textfield = self.driver.find_element(*self.username_textfield)
        name_textfield.clear()
        name_textfield.send_keys(text)
        
    def toast_text(self):
        self.wait_locator(self.toast_error_username)
        toast_error_alert = self.driver.find_element(*self.toast_error_username)
        alert_text = toast_error_alert.text
        sleep(2)
    
    def click_next_to_key(self):
        click_next_button_to_key = self.driver.find_element(*self.next_button_to_key)
        click_next_button_to_key.click()
    
    def select_agree_term(self):
        checkbox_selected = self.driver.find_element(*self.checkbox_click)
        checkbox_selected.click()
        return checkbox_selected.is_selected()
        
class generate_key(Basepage):
    url = 'http://lancer.host.3rdex.com/account/key-gen'
    key_page_title = (By.CSS_SELECTOR,'.src-Screens-Account-___KeyGenScreen__header-text___28f_l')
    key_pairs_exp = (By.CSS_SELECTOR, '.src-Components-Account-___AccountStageInfo__page-summary___3I4gd')
    key_generation = (By.CSS_SELECTOR, '.general-button-container.src-Screens-Account-___KeyGenScreen__generate-key-button___3rz0_')
    key_pairs_text = (By.CSS_SELECTOR,'.src-Screens-Account-___KeyGenScreen__private-key___1KDma')
    key_textfield = (By.CSS_SELECTOR, '.src-Screens-Account-___KeyGenScreen__public-key___1-Nnn')
    public_key_textfield = (By.CSS_SELECTOR, '.src-Components-Account-___KeyInput__key-input-container___15QpZ > input[placeholder = "Enter Your Owner Public Key"]')
    active_key_textfield = (By.CSS_SELECTOR, '.src-Components-Account-___KeyInput__key-input-container___15QpZ > input[placeholder = "Enter Your Active Public Key"]')
    next_button_to_payment = (By.CSS_SELECTOR, '.primary-button-container')
    toast_error_key = (By.CSS_SELECTOR, '.Toastify')
    reminder_before_payment = (By.CSS_SELECTOR, '.src-Screens-Account-___KeyGenScreen__alert-container___2q_Wl')
    alert_action = (By.CSS_SELECTOR, '.src-Screens-Account-___KeyGenScreen__alert-actions___1LuH9 > div > p')

    def verify_key_page(self):
        assert self.driver.current_url == 'http://lancer.host.3rdex.com/account/key-gen', "cannot find key page"
        key_pair_title = self.driver.find_element(*self.key_page_title)
        key_pairs_explanation = self.driver.find_element(*self.key_pairs_exp)
    
    def generate_key(self): 
        self.wait_locator(self.key_generation)
        new_key_pair = self.driver.find_element(*self.key_generation)
        new_key_pair.click()
        sleep(2)

    def get_key(self):  
        self.wait_locator(self.key_textfield)
        key_pairs_generation = self.driver.find_element(*self.key_textfield)
        
        self.wait_locator(self.key_pairs_text)
        key_pair_results = self.driver.find_element(*self.key_pairs_text)
        return key_pair_results.text

    def input_owner_key(self, text):
        self.wait_locator(self.public_key_textfield)
        owner_key_textfield = self.driver.find_element(*self.public_key_textfield)
        owner_key_textfield.send_keys(text)
    
    def input_active_key(self, text):
        self.wait_locator(self.active_key_textfield)
        active_key_text = self.driver.find_element(*self.active_key_textfield)
        active_key_text.send_keys(text)

    def toast_text(self):
        self.wait_locator(self.toast_error_key)
        toast_error_key_alert = self.driver.find_element(*self.toast_error_key)
        key_alert_text = toast_error_key_alert.text
        sleep(2)
    
    def click_next_to_payment(self):
        click_next_button_to_payment = self.driver.find_element(*self.next_button_to_payment)
        click_next_button_to_payment.click()

    def article_reminder(self):
        self.wait_locator(self.reminder_before_payment)
        reminder_content = self.driver.find_element(*self.reminder_before_payment)
        reminder_content_text = reminder_content.text
        sleep(2)
    
    def reminder_button_yes(self):
        self.wait_locator(self.alert_action)
        for alert_yes in self.driver.find_elements(*self.alert_action):
            if alert_yes.text == "Yes, I have":
                alert_yes.click()
            
    def reminder_button_no(self):
        self.wait_locator(self.alert_action)
        for alert_no in self.driver.find_elements(*self.alert_action):
            if alert_no.text == "No, I have't":
                alert_no.click()
            
class payment(Basepage):
    url = 'http://lancer.host.3rdex.com/account/payment/5bd344db2ecbfa4d9f0a8275'
    payment_page_title = (By.CSS_SELECTOR,'.src-Screens-Account-___PaymentScreen__title___uyJ5l')
    payment_exp = (By.CSS_SELECTOR, '.src-Components-Account-___AccountStageInfo__page-summary___3I4gd')
    credit_card_button = (By.CSS_SELECTOR, '.primary-button-container.active.src-Screens-Account-___PaymentScreen__pay-usd-button___1KdYo')
    payment_informaton_filling = (By.CSS_SELECTOR, '.Modal')
    payment_email = (By.CSS_SELECTOR, 'input[type = "email"]')
    payment_card_number = (By.CSS_SELECTOR, 'input[type = "tel"]')
    payment_date = (By.CSS_SELECTOR, 'input[placeholder="MM / YY"]')
    payment_cvc= (By.CSS_SELECTOR, 'input[placeholder="CVC"]')
    payment_zip_code =(By.CSS_SELECTOR, 'input[placeholder="ZIP Code"]')
    payment_button = (By.CSS_SELECTOR, '.Button-animationWrapper-child--primary.Button')
    payment_by_friend = (By.CSS_SELECTOR, '.general-button-container.src-Screens-Account-___PaymentScreen__send-link-button___2JXNR')
    payment_friend_link_or_email = (By.CSS_SELECTOR, '.src-Screens-Account-___PaymentScreen__action-row___2oy_d')
    toast_payment = (By.CSS_SELECTOR, '.Toastify')
    friend_email_address_window = (By.CSS_SELECTOR, '.src-Screens-Account-___PaymentScreen__email-friend-overlay-container___zm1qU')
    friend_email_address_input = (By.CSS_SELECTOR, 'input.general-input')
    send_email_button = (By.CSS_SELECTOR, '.src-Screens-Account-___PaymentScreen__ok-button___1gA0v > div.primary-button-container')
    toast_email = (By.CSS_SELECTOR, '.Toastify')

    def verify_payment_page(self):
        sleep(2)
        payment_title = self.driver.find_element(*self.payment_page_title)
        payment_text = self.driver.find_element(*self.payment_exp)

    def click_credit_card_to_pay(self):
        self.wait_locator(self.credit_card_button)
        click_credit_card = self.driver.find_element(*self.credit_card_button)
        click_credit_card.click()

    def credit_card_information(self):
        self.driver.switch_to.frame('stripe_checkout_app')
        payment_information = self.driver.find_element(*self.payment_informaton_filling)

    def credit_card_email(self,text):
        payment_email_textfield = self.driver.find_element(*self.payment_email)
        payment_email_textfield.send_keys(text)

    def credit_card_number(self,text):
        payment_card_number_textfield = self.driver.find_element(*self.payment_card_number)
        payment_card_number_textfield.send_keys(text)

    def credit_card_date(self,text):
        payment_date_textfield = self.driver.find_element(*self.payment_date)
        payment_date_textfield.send_keys(text)

    def credit_card_cvc(self,text):
        payment_cvc_textfield = self.driver.find_element(*self.payment_cvc)
        payment_cvc_textfield.send_keys(text)

    def credit_card_zip(self,text):
        payment_zip_textfield = self.driver.find_element(*self.payment_zip_code)
        payment_zip_textfield.send_keys(text)

    def click_credit_card_pay_button(self):
        payment_button_click = self.driver.find_element(*self.payment_button)
        payment_button_click.click()
        self.driver.switch_to.default_content()

    def pay_by_friend(self):
        friend_payment = self.driver.find_element(*self.payment_by_friend)
        friend_payment.click()

    def link_to_friend(self):
        for copy_link in self.driver.find_elements(*self.payment_friend_link_or_email):
            if copy_link.text == "Copy the Link":
                ## print('copy link: ', copy_link.text)
                ## sleep(2)
                copy_link.click()
            
    def email_to_friend(self):
        for email_friend in self.driver.find_elements(*self.payment_friend_link_or_email):
            if email_friend.text == "Email my friend":
                email_friend.click()

    def toast_link_text(self):
        self.wait_locator(self.toast_payment)
        toast_link_alert = self.driver.find_element(*self.toast_payment)
        link_alert_text = toast_link_alert.text
        sleep(2)

    def friend_email_address(self):
        sleep(2)
        self.wait_locator(self.friend_email_address_window)
        friend_email_input_place = self.driver.find_element(*self.friend_email_address_window)

    def fill_friend_email(self,text):
        self.wait_locator(self.friend_email_address_input)
        friend_email_input = self.driver.find_element(*self.friend_email_address_input)
        friend_email_input.send_keys(text)

    def click_email_to_friend_button(self):
        sleep(2)
        send_friend_email = self.driver.find_element(*self.send_email_button)
        send_friend_email.click()

    def toast_email_text(self):
        self.wait_locator(self.toast_email)
        toast_email_alert = self.driver.find_element(*self.toast_email)
        email_alert_text = toast_email_alert.text
        sleep(2)

class payment_successful(Basepage):
    url = 'http://lancer.host.3rdex.com/account/payment/5bd8b72c2ecbfa4d9f0ab962'
    payment_account_name = (By.CSS_SELECTOR, '.src-Components-Account-___DoneStage__account-name___3oQjx')
    what_is_next_text = (By.CSS_SELECTOR, '.src-Components-Account-___AccountStageInfo__account-info-stage-container___1SE9N')

    def verify_payment_page(self):
        self.driver.switch_to.default_content()
        sleep(5)
        self.wait_locator(self.payment_account_name)
        payment_account = self.driver.find_element(*self.payment_account_name)
        self.wait_locator(self.what_is_next_text)
        after_payment = self.driver.find_element(*self.what_is_next_text)




    





        




    

    
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import page

class TestLiaoyuan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.get("http://lancer.host.3rdex.com/#poster")

    def tearDown(self):
        self.driver.close()
        pass

    def xtest_3rdex(self):
        main_page = page.main_3rdex(self.driver)
        main_page.verify_3rdex()
        main_page.click_button()

        eos_page = page.ram_eos_page(self.driver)
        eos_page.verify_ram_eos()
        eos_page.click_create()

    def xtest_3rdex_signup_generate_name(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        name_length = len(signup_page.name_text())
        assert name_length == 12, "Name generation error"

    def xtest_signup_with_name_and_term_should_goto_key_page(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        valid_name = signup_page.name_text()
        signup_page.click_agree_term()
        signup_page.click_next()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

    def xtest_3rdex_signup_with_invalid_name_and_term_should_show_error_toast(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        invalid_name = signup_page.input_name("edrf0000")
        signup_page.click_agree_term()
        signup_page.click_next()
        signup_page.toast_text()

    def xtest_3rdex_signup_with_name_without_term_should_show_error_toast(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        valid_name = signup_page.name_text()
        ##signup_page.click_agree_term()
        signup_page.click_next()
        signup_page.toast_text()

    def xtest_3rdex_signup_generate_key(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        valid_name = signup_page.name_text()
        signup_page.click_agree_term()
        signup_page.click_next()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        key_page.verify_key_page()
        key_page.key_generation()
        valid_key = key_page.key_text()
        key_length = len(key_page.key_text())
        assert key_length == 51, "Key generation error" 

    def xtest_signup_with_key_should_goto_payment_page(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        valid_name = signup_page.name_text()
        signup_page.click_agree_term()
        signup_page.click_next()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        key_page.key_generation()
        valid_key = key_page.key_text()
        key_page.click_next_button()
        key_page.article_reminder()
        key_page.reminder_button_yes()
        payment_information = page.payment(self.driver)
        payment_information.verify_payment_page()

    def test_signup_with_key_but_without_safety_should_not_goto_payment_page(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        valid_name = signup_page.name_text()
        signup_page.click_agree_term()
        signup_page.click_next()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        key_page.key_generation()
        valid_key = key_page.key_text()
        key_page.click_next_button()
        key_page.article_reminder()
        key_page.reminder_button_no()
        key_page.verify_key_pairs_page()

    def xtest_3rdex_key_with_invalid_owner_key_and_should_show_error_toast(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        valid_name = signup_page.name_text()
        signup_page.click_agree_term()
        signup_page.click_next()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        owner_key = key_page.input_owner_key("EOS7NGjfHqHHCS1auyvyckhqF3SGK9vR7my89yDk2uCGk4RWHUkaC")
        active_key = key_page.input_active_key("ssswe3r")
        key_page.click_next_button()
        key_page.toast_text()
    
    def xtest_3rdex_key_with_invalid_active_key_and_should_show_error_toast(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        valid_name = signup_page.name_text()
        signup_page.click_agree_term()
        signup_page.click_next()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        owner_key = key_page.input_owner_key("wederef")
        active_key = key_page.input_active_key("EOS8Rri65Qk5YF6j6NVZPnp3Jay2r114sUdhX2EeSPLcGkfP7ykCW")
        key_page.click_next_button()
        key_page.toast_text()

    def xtest_3rdex_without_key_should_show_error_toast(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        valid_name = signup_page.name_text()
        signup_page.click_agree_term()
        signup_page.click_next()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        ##valid_key = key_page.key_text()
        key_page.click_next_button()
        key_page.toast_text()

    def xtest_3rdex_payment(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        valid_name = signup_page.name_text()
        signup_page.click_agree_term()
        signup_page.click_next()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        key_page.key_generation()
        valid_key = key_page.key_text()
        key_page.click_next_button()
        key_page.article_reminder()
        key_page.reminder_button_yes()

        payment_information = page.payment(self.driver)
        payment_information.verify_payment_page()
        payment_information.click_credit_to_pay()
        payment_information.credit_card_information()
        
if __name__ == "__main__":
    unittest.main() # run all tests

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

class Test3rdex(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.get("http://lancer.host.3rdex.com/#poster")

    def tearDown(self):
        self.driver.close()
        pass

    def test_3rdex_main_page(self):
        main_page = page.main_3rdex(self.driver)
        main_page.verify_3rdex_main_page()
        main_page.start_exchange_button()

        eos_page = page.ram_eos_page(self.driver)
        eos_page.verify_ram_eos()
        eos_page.click_create_account()

    def test_3rdex_signup_name(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        name_length = len(signup_page.get_username_text())
        assert name_length == 12, "Name generation error"

    def test_3rdex_signup_random_generate_name(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        signup_page.generate_username()
        name_length = len(signup_page.get_username_text())
        assert name_length == 12, "Name generation error"

    def test_signup_with_name_and_term_should_goto_key_page(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        valid_name = signup_page.get_username_text()
        signup_page.select_agree_term()
        signup_page.click_next_to_key()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

    def test_3rdex_signup_with_invalid_name_and_term_should_show_error_toast(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        invalid_name = signup_page.fill_in_username("edrf0000")
        signup_page.select_agree_term()
        signup_page.click_next_to_key()
        signup_page.toast_text()

    def test_3rdex_signup_with_name_without_term_should_show_error_toast(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        valid_name = signup_page.get_username_text()
        ##signup_page.select_agree_term()
        signup_page.click_next_to_key()
        signup_page.toast_text()

    def test_3rdex_signup_generate_key_should_be_successful(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        valid_name = signup_page.get_username_text()
        signup_page.select_agree_term()
        signup_page.click_next_to_key()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        key_page.verify_key_page()
        key_page.generate_key()
        valid_key = key_page.get_key()
        key_length = len(key_page.get_key())
        assert key_length == 51, "Key generation error" 

    def test_signup_with_key_and_confirmation_should_goto_payment_page(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        valid_name = signup_page.get_username_text()
        signup_page.select_agree_term()
        signup_page.click_next_to_key()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        key_page.verify_key_page()
        key_page.generate_key()
        valid_key = key_page.get_key()
        key_page.click_next_to_payment()
        key_page.article_reminder()
        key_page.reminder_button_yes()
        payment_information = page.payment(self.driver)
        payment_information.verify_payment_page()

    def test_signup_with_key_but_without_confirmation_should_not_goto_payment_page(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        valid_name = signup_page.get_username_text()
        signup_page.select_agree_term()
        signup_page.click_next_to_key()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        key_page.verify_key_page()
        key_page.generate_key()
        valid_key = key_page.get_key()
        key_page.click_next_to_payment()
        key_page.article_reminder()
        key_page.reminder_button_no()
        key_page.verify_key_page()

    def test_3rdex_signup_but_with_invalid_owner_key_should_show_error_toast(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        valid_name = signup_page.get_username_text()
        signup_page.select_agree_term()
        signup_page.click_next_to_key()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        key_page.verify_key_page()
        owner_key = key_page.input_owner_key("EOS7NGjfHqHHCS1auyvyckhqF3SGK9vR7my89yDk2uCGk4RWHUkaC")
        active_key = key_page.input_active_key("ssswe3r")
        key_page.click_next_to_payment()
        key_page.toast_text()
    
    def test_3rdex_signup_but_with_invalid_active_key_should_show_error_toast(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        valid_name = signup_page.get_username_text()
        signup_page.select_agree_term()
        signup_page.click_next_to_key()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        owner_key = key_page.input_owner_key("wederef")
        active_key = key_page.input_active_key("EOS8Rri65Qk5YF6j6NVZPnp3Jay2r114sUdhX2EeSPLcGkfP7ykCW")
        key_page.click_next_to_payment()
        key_page.toast_text()

    def test_3rdex_signup_without_key_should_show_error_toast(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        valid_name = signup_page.get_username_text()
        signup_page.select_agree_term()
        signup_page.click_next_to_key()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        verify_next_page = page.generate_key(self.driver)
        key_page.click_next_to_payment()
        key_page.toast_text()

    def test_3rdex_payment_by_credit_card(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        valid_name = signup_page.get_username_text()
        signup_page.select_agree_term()
        signup_page.click_next_to_key()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        key_page.verify_key_page()
        key_page.generate_key()
        valid_key = key_page.get_key()
        key_page.click_next_to_payment()
        key_page.article_reminder()
        key_page.reminder_button_yes()
        payment_information = page.payment(self.driver)
        payment_information.verify_payment_page()

        payment_information = page.payment(self.driver)
        payment_information.verify_payment_page()
        payment_information.click_credit_card_to_pay()
        payment_information.credit_card_information()
        email_address = payment_information.credit_card_email("dfdrfv@example.com")
        credit_card = payment_information.credit_card_number("4242 4242 4242 4242")
        expire_date = payment_information.credit_card_date("09/20")
        cvc_code = payment_information.credit_card_cvc("123")
        zip_code = payment_information.credit_card_zip("12345")
        payment_information.click_credit_card_pay_button()
        payment_successful_page = page.payment_successful(self.driver)
        payment_successful_page.verify_payment_page()

    def xtest_3rdex_payment_by_friend_link(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        valid_name = signup_page.get_username_text()
        signup_page.select_agree_term()
        signup_page.click_next_to_key()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        key_page.generate_key()
        valid_key = key_page.get_key()
        key_page.click_next_to_payment()
        key_page.article_reminder()
        key_page.reminder_button_yes()
        payment_information = page.payment(self.driver)
        payment_information.verify_payment_page()

        payment_information = page.payment(self.driver)
        payment_information.verify_payment_page()
        payment_information.pay_by_friend()
        payment_information.link_to_friend()
        payment_information.toast_link_text()
        payment_information.verify_payment_page()

    def test_3rdex_payment_by_friend_email(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        valid_name = signup_page.get_username_text()
        signup_page.select_agree_term()
        signup_page.click_next_to_key()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        key_page.generate_key()
        valid_key = key_page.get_key()
        key_page.click_next_to_payment()
        key_page.article_reminder()
        key_page.reminder_button_yes()
        payment_information = page.payment(self.driver)
        payment_information.verify_payment_page()

        payment_information = page.payment(self.driver)
        payment_information.verify_payment_page()
        payment_information.pay_by_friend()
        payment_information.email_to_friend()
        payment_information.friend_email_address()
        payment_information.fill_friend_email("dsfefg@example.com")
        payment_information.click_email_to_friend_button()
        payment_information.verify_payment_page()

    def test_3rdex_payment_by_friend_email_without_confirmation_to_send(self):
        self.driver.get("http://lancer.host.3rdex.com/account/create")
        signup_page = page.signup_3rdex(self.driver)
        signup_page.verify_signup_page()
        valid_name = signup_page.get_username_text()
        signup_page.select_agree_term()
        signup_page.click_next_to_key()
        verify_next_page = page.generate_key(self.driver)
        verify_next_page.verify_key_page()

        ##self.driver.get("http://lancer.host.3rdex.com/account/key-gen")
        key_page = page.generate_key(self.driver)
        key_page.generate_key()
        valid_key = key_page.get_key()
        key_page.click_next_to_payment()
        key_page.article_reminder()
        key_page.reminder_button_yes()
        payment_information = page.payment(self.driver)
        payment_information.verify_payment_page()

        payment_information = page.payment(self.driver)
        payment_information.verify_payment_page()
        payment_information.pay_by_friend()
        payment_information.email_to_friend()
        payment_information.friend_email_address()
        payment_information.click_email_to_friend_button()
        payment_information.toast_email_text()

if __name__ == "__main__":
    unittest.main() # run all tests

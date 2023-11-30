
from selenium.webdriver.common.by import By

from tests.pages.BasePageObject import BasePageObject


class CheckoutInformationPage(BasePageObject):
    
    URL = "https://www.saucedemo.com/checkout-step-one.html"

    loc_page_title_selector = ".header_secondary_container span.title"
    loc_first_name_input_selector = '[data-test="firstName"]'
    loc_last_name_input_selector = '[data-test="lastName"]'
    loc_zipcode_input_selector = '[data-test="postalCode"]'
    loc_continue_button_selector = '[data-test="continue"]'


    def is_checkout_information_page_url(self) -> bool:
        return self.driver.current_url == self.URL
    

    def verify_page_title_is(self, expected_value: str = ""):
        page_title = self.driver.find_element(By.CSS_SELECTOR, self.loc_page_title_selector).text
        return page_title.lower() == expected_value.lower()
    
    
    def type_first_name(self, value="Not given"):
        self.driver.find_element(By.CSS_SELECTOR, self.loc_first_name_input_selector).send_keys(value)
    
    
    def type_last_name(self, value="Not given"):
        self.driver.find_element(By.CSS_SELECTOR, self.loc_last_name_input_selector).send_keys(value)
    
    
    def type_zipcode(self, value="Not given"):
        self.driver.find_element(By.CSS_SELECTOR, self.loc_zipcode_input_selector).send_keys(value)

    
    def type_valid_client_information(self):
        self.type_first_name("Etta")
        self.type_last_name("James")
        self.type_zipcode("123-321")

    
    def click_to_continue_with_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.loc_continue_button_selector).click()


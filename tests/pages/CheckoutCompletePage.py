
from selenium.webdriver.common.by import By

from tests.pages.BasePageObject import BasePageObject


class CheckoutCompletePage(BasePageObject):

    URL = "https://www.saucedemo.com/checkout-complete.html"

    loc_page_title_selector = ".header_secondary_container span.title"
    loc_appreciation_message_class = "complete-header"
    loc_back_home_button_selector = '[data-test="back-to-products"]'


    def verify_page_title_is(self, expected_value: str = ""):
        page_title = self.driver.find_element(By.CSS_SELECTOR, self.loc_page_title_selector).text
        return page_title.lower() == expected_value.lower()
    

    def verify_appreciation_message_is(self, expected_message: str):
        displayed_message = self.driver.find_element(By.CLASS_NAME, self.loc_appreciation_message_class).text
        return displayed_message.lower() == expected_message.lower()    
    
    def click_back_home(self):
        self.driver.find_element(By.CSS_SELECTOR, self.loc_back_home_button_selector).click()



from selenium.webdriver.common.by import By

from tests.pages.BasePageObject import BasePageObject


class CheckoutOverviewPage(BasePageObject):

    URL = "https://www.saucedemo.com/checkout-step-two.html"

    loc_page_title_selector = ".header_secondary_container span.title"
    loc_checkout_list_selector = "#checkout_summary_container .cart_list"
    loc_checkout_item_class = "cart_item"
    loc_checkout_item_quantity_class = "cart_quantity"
    loc_checkout_item_name_class = "inventory_item_name"
    loc_checkout_item_price_class = "inventory_item_price"
    loc_finish_checkout_button_selector = '[data-test="finish"]'


    def verify_page_title_is(self, expected_value: str = ""):
        page_title = self.driver.find_element(By.CSS_SELECTOR, self.loc_page_title_selector).text
        return page_title.lower() == expected_value.lower()


    def get_checkout_items(self) -> list:
        """
        Retrieve a list of Products and its information from the Checkout Overview page

        @return list[ (element: WebElement, element_name: str, element_price: str, element_quantity: str) ]
        """
        checkout_items = self.driver.find_elements(By.CSS_SELECTOR, self.loc_checkout_list_selector)
        checkout_item_list = []

        for item in checkout_items:
            item_name = item.find_element(By.CLASS_NAME, self.loc_checkout_item_name_class).text
            item_price = item.find_element(By.CLASS_NAME, self.loc_checkout_item_price_class).text
            item_quantity = item.find_element(By.CLASS_NAME, self.loc_checkout_item_quantity_class).text
            checkout_item_list.append((item, item_name, item_price, item_quantity))

        return checkout_item_list
    

    def verify_if_item_is_part_of_checkout_list(self, item) -> bool:
        """Compare a given item with the ones present on the Checkout Summary items list and return if its part or not the checkout list"""
        
        is_item_part_of_checkout_list = False
        _, expected_name, expected_price, expected_quantity = item

        checkout_list = self.get_checkout_items()
        for checkout_item in checkout_list:
            _, checkout_item_name, checkout_item_price, checkout_item_quantity = checkout_item
            if expected_name == checkout_item_name and expected_price == checkout_item_price and expected_quantity == checkout_item_quantity:
                is_item_part_of_checkout_list = True
                print("[    debug   ]   Checkout Item comparison - Name: {} - Price: {} - Quantity: {}"
                      .format(expected_name, expected_price, expected_quantity))

        return is_item_part_of_checkout_list

    
    
    def click_finish_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.loc_finish_checkout_button_selector).click()


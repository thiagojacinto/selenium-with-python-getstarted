from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from tests.pages.BasePageObject import BasePageObject


class InventoryPage(BasePageObject):
    """Page Object representation for the Inventory Page"""

    URL = "https://www.saucedemo.com/inventory.html"

    loc_inventory_list_selector = "#inventory_container > div.inventory_list div.inventory_item"
    loc_inventory_item_name_class = "inventory_item_name"
    loc_inventory_item_price_class = "inventory_item_price"
    loc_inventory_item_add_button_selector = "button.btn_primary"
    loc_inventory_item_remove_button_selector = "button.btn_secondary"


    def has_access_to_inventory(self) -> bool:
        return "inventory" in self.get_url()


    def _get_list_of_products(self):
        """Get a list of elements that represents products or items"""
        return self.driver.find_elements(By.CSS_SELECTOR, self.loc_inventory_list_selector)
    

    def choose_an_item_randomsly(self):
        """
        From the inventory list, select randomsly an item.
        
        @return (element: WebElement, element_name: str, element_price: str)
        """
        items_list = self._get_list_of_products()

        selected_item = choice(items_list)
        selected_item_name = selected_item.find_element(By.CLASS_NAME, self.loc_inventory_item_name_class).text
        selected_item_price = selected_item.find_element(By.CLASS_NAME, self.loc_inventory_item_price_class).text

        return (selected_item, selected_item_name, selected_item_price)

    def add_item_to_cart(self, product_item: WebElement):
        """Click on item's Add to Cart button"""
        add_button = product_item.find_element(By.CSS_SELECTOR, self.loc_inventory_item_add_button_selector)
        add_button.click()

    def get_item_button_text(self, product_item: WebElement) -> str:
        """Returns the Text value of the item's button"""
        return product_item.find_element(By.TAG_NAME, "button").text
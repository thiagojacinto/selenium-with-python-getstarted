
from selenium.webdriver.common.by import By

from tests.pages.BasePageObject import BasePageObject


class CartPage(BasePageObject):
    
    URL = "https://www.saucedemo.com/cart.html"

    loc_cart_page_title_selector = "#header_container .title"
    loc_cart_list_selector = "#cart_contents_container .cart_list"
    loc_cart_item_class = "cart_item"
    loc_cart_item_quantity_class = "cart_quantity"
    loc_cart_item_name_class = "inventory_item_name"
    loc_cart_item_price_class = "inventory_item_price"

    def is_cart_page_url(self) -> bool:
        return self.driver.current_url == self.URL

    def get_cart_items(self) -> list:
        cart_items = self.driver.find_elements(By.CSS_SELECTOR, self.loc_cart_list_selector)
        cart_item_list = []

        for item in cart_items:
            item_name = item.find_element(By.CLASS_NAME, self.loc_cart_item_name_class).text
            item_price = item.find_element(By.CLASS_NAME, self.loc_cart_item_price_class).text
            item_quantity = item.find_element(By.CLASS_NAME, self.loc_cart_item_quantity_class).text
            cart_item_list.append((item, item_name, item_price, item_quantity))

        return cart_item_list

    def verify_product_is_in_cart(self, product_name: str, product_price: str) -> bool:
        cart_list = self.get_cart_items()

        for item in cart_list:
            added_product_name = item[1].lower()
            added_product_price = item[2].lower()
            if added_product_name == product_name.lower() and added_product_price == product_price.lower(): return True

        return False
        

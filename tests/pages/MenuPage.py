
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.BasePageObject import BasePageObject

class MenuPage(BasePageObject):
    
    loc_open_menu_id = "react-burger-menu-btn"
    loc_menu_navbar_selector = "nav.bm-item-list"
    loc_close_menu_id = "react-burger-cross-btn"
    loc_logout_button_id = "logout_sidebar_link"
    loc_cart_icon_selector = "#shopping_cart_container .shopping_cart_badge"

    def open_menu(self):
        """From Menu, tap on Menu Icon to open the Menu"""
        menu_open_button = self.driver.find_element(By.ID, self.loc_open_menu_id)
        
        wait = WebDriverWait(self.driver, timeout = self.DEFAULT_TIMEOUT)
        wait.until(lambda e : menu_open_button.is_displayed())

        menu_open_button.click()

    def click_logout(self):
        """From Menu, tap on Logout"""
        wait = WebDriverWait(self.driver, timeout = self.DEFAULT_TIMEOUT)
        wait.until(
            lambda e : self.driver.find_element(By.CSS_SELECTOR, self.loc_menu_navbar_selector).is_displayed()
            )
        
        menu_logout_button = self.driver.find_element(By.ID, self.loc_logout_button_id)
        menu_logout_button.click()


    def get_cart_icon_count(self) -> int:
        """Cart Icon items counter number"""
        cart_counter_value = self.driver.find_element(By.CSS_SELECTOR, self.loc_cart_icon_selector).text
        return int(cart_counter_value)
    
    def click_on_cart_icon(self):
        self.driver.find_element(By.CSS_SELECTOR, self.loc_cart_icon_selector).click()

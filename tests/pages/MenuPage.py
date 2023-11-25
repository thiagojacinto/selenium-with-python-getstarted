
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.BasePageObject import BasePageObject

class MenuPage(BasePageObject):
    
    loc_open_menu_id = "react-burger-menu-btn"
    loc_menu_navbar_selector = "nav.bm-item-list"
    loc_close_menu_id = "react-burger-cross-btn"
    loc_logout_button_id = "logout_sidebar_link"

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


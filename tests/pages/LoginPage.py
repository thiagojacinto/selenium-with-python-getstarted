from .BasePageObject import BasePageObject

from selenium.webdriver.common.by import By

class LoginPage(BasePageObject):
    """Page Object representation for the Login Page"""

    URL = "https://www.saucedemo.com/"

    valid_username = "standard_user"
    valid_password = "secret_sauce"

    loc_username_input_field_id = "user-name"
    loc_password_input_field_id = "password"
    loc_submit_login_button_id = "login-button"
    loc_loging_error_message_selector = "h3[data-test=error]"

    def access_page(self):
        """Go to Login Page url"""
        self.driver.get(self.URL)

    def type_username(self, username_input: str):
        """Type the username on the correct field"""

        login_field = self.driver.find_element(By.ID, self.loc_username_input_field_id)
        login_field.send_keys(username_input)

    def type_password(self, password_input: str):
        """Type the password on the correct field"""

        login_field = self.driver.find_element(By.ID, self.loc_password_input_field_id)
        login_field.send_keys(password_input)

    def click_on_login(self):
        """Click on login button"""
        self.driver.find_element(By.ID, self.loc_submit_login_button_id).click()

    def is_login_button_visible(self):
        """Click on login button"""
        return self.driver.find_element(By.ID, self.loc_submit_login_button_id).is_displayed()
    
    def type_successfull_credentials(self):
        self.type_username(self.valid_username)
        self.type_password(self.valid_password)

    def has_error_on_username_field(self) -> bool:
        """Verify if there's an error on username field attributes"""
        
        login_field = self.driver.find_element(By.ID, self.loc_username_input_field_id)
        return "error" in login_field.get_dom_attribute("class")

    def has_error_on_password_field(self) -> bool:
        """Verify if there's an error on password field attributes"""

        login_field = self.driver.find_element(By.ID, self.loc_password_input_field_id)
        return "error" in login_field.get_dom_attribute("class")
    
    def has_error_alert(self, error_text = None) -> bool:
        """Verify if there's an error alert, and validate its content IF `error_text` is given"""

        error_alert = self.driver.find_element(By.CSS_SELECTOR, self.loc_loging_error_message_selector)
        
        if error_alert is not None:
            return error_text.lower() in error_alert.text.lower()
        
        return error_alert.is_displayed()


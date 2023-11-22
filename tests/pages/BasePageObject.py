from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class BasePageObject:
    """Base class for PageObject implementations"""

    def __init__(self, driver = None):
        """PageObject constructor to handle the driver instance - creation or reuse"""

        if driver is not None and type(driver) is not str:
            self.driver = driver

        match driver:
            case None:
                new_driver_options = Options()
                new_driver_options.add_argument("-headless")
                self.driver = webdriver.Firefox(new_driver_options)
            case "firefox":
                self.driver = webdriver.Firefox()
            case "headless-firefox":
                new_driver_options = Options()
                new_driver_options.add_argument("-headless")
                self.driver = webdriver.Firefox(new_driver_options)
            case "chrome":
                self.driver = webdriver.Chrome()
            case "headless-chrome":
                new_driver_options = Options()
                new_driver_options.add_argument("-headless")
                self.driver = webdriver.Chrome(new_driver_options)
            case "safari":
                self.driver = webdriver.Safari()
            case "headless-firefox":
                new_driver_options = Options()
                new_driver_options.add_argument("-headless")
                self.driver = webdriver.Firefox(new_driver_options)
            case _:
                raise Exception("Not supported webdriver. Try to use a supported webdriver")
            

    def get_url(self):
        return self.driver.current_url()
    
    def close_driver(self):
        """Closes WebDriver connection"""
        self.driver.close()


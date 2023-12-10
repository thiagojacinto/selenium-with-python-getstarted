import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions


class BasePageObject:
    """Base class for PageObject implementations"""

    DEFAULT_TIMEOUT = 5

    def __init__(self, driver = None):
        """PageObject constructor to handle the driver instance - creation or reuse"""

        if driver is not None and type(driver) is not str:
            self.driver = driver
            return

        match driver:
            case None:
                new_driver_options = FirefoxOptions()
                new_driver_options.add_argument("-headless")
                self.driver = webdriver.Firefox(new_driver_options)
            case "remote":
                hostname = os.environ.get("SELENIUM_HOST", "selenium")
                
                match hostname.lower():
                    case "chrome":
                        new_driver_options = ChromeOptions()
                    case "firefox":
                        new_driver_options = FirefoxOptions()
                    case "edge":
                        new_driver_options = EdgeOptions()
                    case _:
                        new_driver_options = FirefoxOptions()
                
                self.driver = webdriver.Remote(
                        command_executor="http://{}:4444".format(hostname),
                        options=new_driver_options,
                        keep_alive=True,
                    )

            case "firefox":
                self.driver = webdriver.Firefox()
            case "headless-firefox":
                new_driver_options = FirefoxOptions()
                new_driver_options.add_argument("-headless")
                self.driver = webdriver.Firefox(new_driver_options)
            case "chrome":
                self.driver = webdriver.Chrome()
            case "headless-chrome":
                new_driver_options = ChromeOptions()
                new_driver_options.add_argument("-headless")
                self.driver = webdriver.Chrome(new_driver_options)
            case "safari":
                self.driver = webdriver.Safari()
            case "headless-safari":
                new_driver_options = SafariOptions()
                new_driver_options.add_argument("-headless")
                self.driver = webdriver.Firefox(new_driver_options)
            case _:
                raise Exception("Not supported webdriver. Try to use a supported webdriver")
            
        self.driver.set_window_size(1366, 768)
            

    def get_url(self):
        return self.driver.current_url
    
    def close_driver(self):
        """Closes WebDriver connection"""
        self.driver.close()


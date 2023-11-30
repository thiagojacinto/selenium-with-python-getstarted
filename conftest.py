import pytest
from tests.pages.InventoryPage import InventoryPage

from tests.pages.LoginPage import LoginPage
from tests.pages.MenuPage import MenuPage

SUPPORTED_BROWSERS_LIST = [
    "chrome",
    "firefox",
    "safari",
    "headless-chrome",
    "headless-firefox",
    "headless-safari",
]

def pytest_addoption(parser):
    parser.addoption(
        "--use-browser",
        action="store",
        default="headless-firefox",
        help="Define the browser to be executed. Current supported versions: " + ", ".join(SUPPORTED_BROWSERS_LIST)
    )

@pytest.fixture(scope="function")
def use_browser_option(request):
    """Fixture to handle the use of argument --use-browser to select"""
    
    force_browser = request.node.get_closest_marker("FORCE_BROWSER")
    if force_browser is None:    
        selected_browser = request.config.getoption("--use-browser")
        return selected_browser
    
    return force_browser.args[0]


@pytest.fixture(scope="function")
def start_by_login_page(use_browser_option):
    """Fixture that starts the WebDriver by accessing the Login page"""
    
    login_page = LoginPage(driver=use_browser_option)
    yield login_page
    
    login_page.close_driver()


@pytest.fixture(scope="function")
def start_already_logged(use_browser_option):
    """Fixture that starts the WebDriver with an user already logged"""
    
    login_page = LoginPage(driver=use_browser_option)
    login_page.access_page()
    login_page.type_successfull_credentials()
    login_page.click_on_login()
    inventory_page = InventoryPage(driver = login_page.driver)

    yield inventory_page
    
    inventory_page.close_driver()


@pytest.fixture(scope="function")
def start_with_one_product_added(start_already_logged):
    """Fixture that starts the WebDriver with an user logged and at least one product added"""
    inventory_page = InventoryPage(driver = start_already_logged.driver)
    selected_item, _, _ = inventory_page.choose_an_item_randomsly()
    inventory_page.add_item_to_cart(selected_item)
    
    menu_page = MenuPage(driver = inventory_page.driver)
    menu_page.click_on_cart_icon()
    return menu_page
    

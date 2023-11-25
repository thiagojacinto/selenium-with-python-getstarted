
from tests.pages.InventoryPage import InventoryPage
from tests.pages.LoginPage import LoginPage


def test_successfully_login_leads_to_inventory(start_by_login_page):
    login_page: LoginPage = start_by_login_page
    login_page.access_page()
    login_page.type_successfull_credentials()
    login_page.click_on_login()

    inventory_page = InventoryPage(driver=login_page.driver)
    assert inventory_page.has_access_to_inventory()


from tests.pages.InventoryPage import InventoryPage
from tests.pages.LoginPage import LoginPage
from tests.pages.MenuPage import MenuPage


def test_successfully_logout_leads_to_login_page(start_already_logged):
    inventory_page: InventoryPage = start_already_logged
    assert inventory_page.has_access_to_inventory()

    menu_page = MenuPage(driver = inventory_page.driver)
    menu_page.open_menu()
    menu_page.click_logout()

    login_page = LoginPage(driver = menu_page.driver)
    assert login_page.is_login_button_visible()

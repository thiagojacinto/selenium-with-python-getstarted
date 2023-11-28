
from tests.pages.CartPage import CartPage
from tests.pages.InventoryPage import InventoryPage
from tests.pages.MenuPage import MenuPage


def test_successfully_add_item_to_cart(start_already_logged):
    inventory_page: InventoryPage = start_already_logged

    selected_item, selected_item_name, selected_item_price = inventory_page.choose_an_item_randomsly()
    inventory_page.add_item_to_cart(selected_item)
    assert inventory_page.get_item_button_text(selected_item).lower() == "remove", "Button text should be REMOVE"

    menu_page = MenuPage(driver = inventory_page.driver)
    assert menu_page.get_cart_icon_count() == 1, "Cart Icon badge should be equal 1"
    menu_page.click_on_cart_icon()

    cart_page = CartPage(driver = menu_page.driver)
    assert cart_page.is_cart_page_url()
    assert cart_page.verify_product_is_in_cart(selected_item_name, selected_item_price), "Cart Items do NOT match the one added"


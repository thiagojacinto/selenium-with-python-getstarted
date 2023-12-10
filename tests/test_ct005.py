
import pytest

from tests.pages.CartPage import CartPage
from tests.pages.CheckoutCompletePage import CheckoutCompletePage
from tests.pages.CheckoutInformationPage import CheckoutInformationPage
from tests.pages.CheckoutOverviewPage import CheckoutOverviewPage

@pytest.mark.parametrize(
        (""), [
            pytest.param(id="default"), 
            pytest.param(id="firefox", marks=pytest.mark.FORCE_BROWSER("firefox"))
            ]
    )
def test_successfully_buy_a_product(start_with_one_product_added):
    cart_page = CartPage(driver = start_with_one_product_added.driver)
    cart_products_list = cart_page.get_cart_items()
    cart_page.click_on_checkout()

    checkout_info_page = CheckoutInformationPage(driver = cart_page.driver)
    assert checkout_info_page.is_checkout_information_page_url()
    assert checkout_info_page.verify_page_title_is("Checkout: Your Information"), "Checkout Information should be the page title"
    checkout_info_page.type_valid_client_information()
    checkout_info_page.click_to_continue_with_checkout()

    checkout_overview_page = CheckoutOverviewPage(driver = checkout_info_page.driver)
    assert checkout_overview_page.verify_page_title_is("Checkout: Overview"), "Checkout Overview should be the page title"
    for item in cart_products_list:
        assert checkout_overview_page.verify_if_item_is_part_of_checkout_list(item)
    

    checkout_overview_page.click_finish_checkout()

    checkout_complete_page = CheckoutCompletePage(driver = checkout_overview_page.driver)
    checkout_complete_page.verify_page_title_is("Checkout: Complete!"), "Checkout Complete! should be the page title"
    checkout_complete_page.verify_appreciation_message_is("Thank you for your order!"), "Should have an appreciation message"

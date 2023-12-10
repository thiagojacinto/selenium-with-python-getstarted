
import pytest

from tests.pages.InventoryPage import InventoryPage

@pytest.mark.parametrize(
        (""), [
            pytest.param(id="default"), 
            pytest.param(id="firefox", marks=pytest.mark.FORCE_BROWSER("firefox")), 
            pytest.param(id="chrome", marks=pytest.mark.FORCE_BROWSER("chrome")), 
            pytest.param(id="safari", marks=pytest.mark.FORCE_BROWSER("safari"))
            ]
    )
def test_apply_low_to_high_filter_on_inventory(start_already_logged):

    inventory_page: InventoryPage = start_already_logged
    inventory_page.select_a_filter_by_type("Price (low to high)")

    assert inventory_page.is_the_low_to_high_price_filter_selected(), "Filter Price (High to low) should be selected"
    assert inventory_page.verify_items_are_ordered_by_price_low_to_high(), "Prices are NOT ordered from Higher to Lower"
    

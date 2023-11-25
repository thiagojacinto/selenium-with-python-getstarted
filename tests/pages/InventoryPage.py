

from tests.pages.BasePageObject import BasePageObject


class InventoryPage(BasePageObject):
    """Page Object representation for the Inventory Page"""

    URL = "https://www.saucedemo.com/inventory.html"

    def has_access_to_inventory(self) -> bool:
        return "inventory" in self.get_url()
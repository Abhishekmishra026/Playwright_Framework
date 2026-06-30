import os

import allure
import pytest
from dotenv import load_dotenv

from config.settings import Settings

load_dotenv()


@allure.feature("Amazon")
@allure.story("Cart")
@allure.title("Search iPhone 16 black 256 GB and add it to cart")
@pytest.mark.smoke
def test_search_and_add_to_cart(amazon_page):
    amazon_page.open_home_page()
    amazon_page.search_product(Settings.SEARCH_TERM)
    amazon_page.select_first_result()
    amazon_page.login_if_needed(Settings.USERNAME, Settings.PASSWORD)
    amazon_page.add_to_cart()

    cart_count = amazon_page.get_cart_item_count()
    assert cart_count > 0, "Expected at least one item in the cart"

    amazon_page.open_cart()
    assert amazon_page.page.locator(amazon_page.locators.ACTIVE_ITEMS).count() > 0

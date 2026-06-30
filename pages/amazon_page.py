import allure
from playwright.sync_api import Page

from pages.amazon_locators import AmazonLocators
from utils.helpers import parse_cart_count


class AmazonPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.locators = AmazonLocators

    def open_home_page(self):
        with allure.step("Open Amazon home page"):
            self.page.goto(self.base_url, wait_until="domcontentloaded")
            self.page.wait_for_load_state("networkidle", timeout=30000)

    def search_product(self, term: str):
        with allure.step(f"Search for product: {term}"):
            self.page.locator(self.locators.SEARCH_INPUT).fill(term)
            self.page.locator(self.locators.SEARCH_BUTTON).click()
            self.page.wait_for_load_state("networkidle", timeout=60000)

    def select_first_result(self):
        with allure.step("Open the first matching product"):
            self.page.locator(self.locators.RESULT_LINK).first.click()
            self.page.wait_for_load_state("domcontentloaded", timeout=60000)

    def login_if_needed(self, username: str | None, password: str | None):
        if not username or not password:
            return False

        with allure.step("Sign in if Amazon asks for authentication"):
            if self.page.locator(self.locators.LOGIN_EMAIL).count() > 0:
                self.page.fill(self.locators.LOGIN_EMAIL, username)
                self.page.locator(self.locators.LOGIN_CONTINUE).click()
                self.page.fill(self.locators.LOGIN_PASSWORD, password)
                self.page.locator(self.locators.LOGIN_SUBMIT).click()
                self.page.wait_for_load_state("networkidle", timeout=60000)
                return True

        return False

    def add_to_cart(self):
        with allure.step("Add selected product to cart"):
            if self.page.locator(self.locators.ADD_TO_CART_BUTTON).count() > 0:
                self.page.locator(self.locators.ADD_TO_CART_BUTTON).click()
            else:
                self.page.get_by_text("Add to Cart", exact=True).first.click()
            self.page.wait_for_timeout(5000)

    def open_cart(self):
        with allure.step("Open shopping cart"):
            self.page.locator(self.locators.CART_BUTTON).click()
            self.page.wait_for_load_state("domcontentloaded", timeout=60000)

    def get_cart_item_count(self) -> int:
        with allure.step("Read cart item count"):
            text = self.page.locator(self.locators.CART_COUNT).inner_text(timeout=10000)
            return parse_cart_count(text)

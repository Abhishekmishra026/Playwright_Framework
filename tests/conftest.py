import pytest
from playwright.sync_api import BrowserContext, Page

from config.settings import Settings


@pytest.fixture(scope="session")
def base_url():
    return Settings.BASE_URL


@pytest.fixture
def browser_context(browser: object) -> BrowserContext:
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    yield context
    context.close()


@pytest.fixture
def page(browser_context: BrowserContext) -> Page:
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture
def amazon_page(page: Page, base_url: str):
    from pages.amazon_page import AmazonPage

    return AmazonPage(page, base_url)

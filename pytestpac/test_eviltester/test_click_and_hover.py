import re
import time

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="A/B Testing").click()
    # page.locator("text = A/B Testing").click() //Альтернативный вариант
    page.goto("https://the-internet.herokuapp.com/hovers")
    page.hover("[alt=\"User Avatar\"]")
    time.sleep(1)
    page.get_by_role("link", name="View profile").first.click()
    time.sleep(1)



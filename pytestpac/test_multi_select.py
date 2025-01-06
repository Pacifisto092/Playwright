import re
import time

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    page.locator("select[name='Month']").select_option(['November', 'July',], label='March')
    time.sleep(2)
    page.locator("select[name='Month']").select_option(index=2, value='May', label='October')
    time.sleep(2)
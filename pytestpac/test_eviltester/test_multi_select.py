import re
import time

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    loc = page.locator("select[name='Month']")
    expect(loc).to_have_value(['November', 'July','March'])
    loc.select_option(['November', 'July'], label='March')
    time.sleep(2)
    expect(loc).to_have_value([re.compile(r"F"), re.compile(r"M"), re.compile(r"O")])
    loc.select_option(index=2, value='May', label='October')
    time.sleep(2)
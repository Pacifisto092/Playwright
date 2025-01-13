import re
import time

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    loc = page.locator("select[name='Month']")
    loc.select_option(['May', 'July', 'Sept'])
    expect(loc).to_have_values(['May', 'July', 'Sept'])
    page.wait_for_timeout(1000)
    loc.select_option(index=2, value='Ma', label='October')
    expect(loc).to_have_values([re.compile(r"F"), re.compile(r"M"), re.compile(r"O")])
    page.wait_for_timeout(1000)


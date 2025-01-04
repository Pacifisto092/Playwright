import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sso.teachable.com/secure/673/identity/login/otp")
    page.get_by_test_id("email-input").click()
    page.get_by_test_id("email-input").fill("hello@yandex.ru")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

import os

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    # 1st browser context
    context = browser.new_context()

    # 2nd browser context
    context2 = browser.new_context()

    page = context.new_page()
    page.goto("https://www.way2automation.com/lifetime-membership-club/")

    # open page in 2nd browser context
    page2 = context2.new_page()
    page2.goto("https://www.way2automation.com/soapui/rest-api-webservices-testing-training/")

    page.wait_for_timeout(10000)
    page2.wait_for_timeout(5000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
 run(playwright)
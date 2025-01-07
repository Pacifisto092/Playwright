import os

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
 browser = playwright.chromium.launch(headless=False)
 context = browser.new_context()

 page = context.new_page()
 page.goto("https://www.way2automation.com/lifetime-membership-club/")

 page.wait_for_timeout(5000)

 # ---------------------
 context.close()
 browser.close()


with sync_playwright() as playwright:
 run(playwright)
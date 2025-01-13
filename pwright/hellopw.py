from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/")
    page.get_by_test_id("email-input").click()
    page.get_by_test_id("email-input").fill("hello@yandex.ru")
    page.locator("input:above(:text(\"Login\"))").first.fill("hello playwright")

    # Stop tracing and export it into a zip archive!
    context.tracing.stop(path="trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

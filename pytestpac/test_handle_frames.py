from playwright.sync_api import Page


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/iframe")
    frame1 =  page.frame_locator("#mce_0_ifr").locator("html")
    frame1.click()
    frame1.type("Welcome to playwright")
    page.wait_for_timeout(4000)

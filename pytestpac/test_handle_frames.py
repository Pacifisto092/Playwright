from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/iframe")
    page.get_by_role("button", name="Close").click()
    frame1 =  page.frame_locator("#mce_0_ifr").locator("html")
    frame1.click()
    expect(frame1).to_have_text("Your content goes here.")
    # frame1.type("Welcome to playwright") # ввод текста, но он ломается из заограничений на кол-во ввода
    page.wait_for_timeout(1000)

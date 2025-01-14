from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/")
    page.locator("input:above(:text(\"Login\"))").first.fill("hello playwright")     #локатор выше

    page.goto("https://www.way2automation.com/angularjs-protractor/registeration/#/login")
    page.locator("input:below(:text(\"Username\"))").first.fill("hello playwright")     #локатор ниже

    page.goto("https://www.way2automation.com/way2auto_jquery/index.php")
    page.locator("select:near(:text(\"Country\"))").select_option("France")     #локатор рядом

    page.locator("select:right-of(:text(\"Country\"))").select_option("Germany")        #локатор справа

    page.goto("https://www.selenium-tutorial.com/p/selenium-training")
    page.locator("a:left-of(:text(\"Sign Up\"))").first.click()             #локатор слева

    # Stop tracing and export it into a zip archive!
    context.tracing.stop(path="trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

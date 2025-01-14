import re
import time

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://sso.teachable.com/secure/673/identity/login/otp")
    page.get_by_test_id("email-input").click()
    page.get_by_test_id("email-input").fill("hellopw@yandex.ru")
    page.get_by_test_id("btn-login").click()
    page.get_by_test_id("otp-input-0").click()
    page.get_by_test_id("otp-input-0").fill("1")
    # time.sleep(1)
    # page.reload()
    page.get_by_test_id("otp-input-1").fill("1")
    page.get_by_test_id("otp-input-2").fill("1")
    page.get_by_test_id("otp-input-3").fill("1")
    page.get_by_test_id("otp-input-4").fill("1")
    page.get_by_test_id("otp-input-5").fill("1")
    page.get_by_test_id("btn-code").click()
    page.go_back()
    # time.sleep(1)
    page.go_forward()
    # time.sleep(1)

    page.goto("https://the-internet.herokuapp.com/")
    page.locator("text=Key Presses").click()
    page.press("#target", "CapsLock")
    expect(page.locator('#result')).to_have_text("You entered: CAPS_LOCK")
    time.sleep(2)

print("test execution complete")
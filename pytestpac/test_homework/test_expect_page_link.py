from playwright.sync_api import Page, expect
from ..utils.data import *


def test_expect_header_link(page: Page) -> None:
    page.goto(URL)
    """Проверка ссылок в хедере"""
    # Переход по ссылке About
    page.get_by_role("link", name="About").click()
    expect(page.locator(".explanation")).to_contain_text("A Form with")
    # Переход по ссылке Page
    page.get_by_role("link", name="Page", exact=True).click()
    expect(page.locator(".explanation")).to_contain_text("This page has input")
    # Переход по ссылке Index
    page.get_by_role("link", name="Index").click()
    expect(page.locator(".explanation")).to_contain_text("This is a set of applications")
    print("Ссылки хедера - OK")


def test_expect_footer_link(page: Page) -> None:
    page.goto(URL)
    """Проверка ссылок в футоре"""
    #Открытие 1-ой ссылки в новом окне и проверка наличия элемента на ней
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="EvilTester.com").click()
    page1 = page1_info.value
    expect(page1.locator(".mini-image-list")).to_be_visible()

    #Открытие 2-ой ссылки в новом окне и проверка наличия элемента на ней
    with page.expect_popup() as page2_info:
        page.get_by_role("link", name="Compendium Developments").click()
    page2 = page2_info.value
    expect(page2).to_have_url("https://compendiumdev.co.uk/")
    print("Ссылки футера - OK")
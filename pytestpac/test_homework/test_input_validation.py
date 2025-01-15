from os import error

from playwright.sync_api import Page, expect
from ..utils.data import *

def test_valid_input_validation(page: Page) -> None:
    page.goto(URL)
    """Заполнение полей валидными данными и их отправка"""
    page.locator("#firstname").fill("Vasia")
    page.locator("#surname").fill("Pupkin-Lapukin")
    page.locator("#age").fill("80")
    page.locator("#country").select_option("Belarus")
    page.locator("#notes").fill("Test notes!!! !@# }{[]\n\n\nLLDM")
    page.get_by_role("button", name="Submit").click()
    print("Заполнение полей валидными данными и их отправка - OK")

    """Проверка заполненых полей в форме Input Validation Response"""
    expect(page.locator("#valid-input-value")).to_have_text("Your Input passed validation")
    expect(page.locator("#firstname-value")).to_have_text("Vasia")
    expect(page.locator("#surname-value")).to_have_text("Pupkin-Lapukin")
    expect(page.locator("#age-value")).to_have_text("80")
    expect(page.locator("#country-value")).to_have_text("Belarus")
    expect(page.locator("#notes-value")).to_have_text("Test notes!!! !@# }{[]\n\n\nLLDM")
    print("Проверка заполнения полей в форме Input Validation Response - OK")

    """Воззврат на страницу назад и проверка заголовка"""
    page.get_by_role("link", name="Back to Input Form").click()
    expect(page.locator(".explanation")).to_be_enabled()
    print("Возврат на страницу назад - OK")


def test_invalid_input_validation(page: Page) -> None:
    page.goto(URL)
    """Заполнение полей невалидными данными и проверка ошибок"""
    #Вызов ошибки поля First name
    page.locator("#age").fill("18")
    page.locator("#firstname").fill("V")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator('[name="firstnamevalidation"]')).to_be_visible()
    print("Ошибка First name - OK")

    # Вызов ошибки поля Last name
    page.locator("#surname").fill("1234567890")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator('[name="surnamevalidation"]')).to_be_visible()
    print("Ошибка Last name - OK")

    #Скрытие ошибки Last name
    page.locator("#surname").fill("12345678901")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator('[name="surnamevalidation"]')).to_be_hidden(timeout=1000)
    print("Скрытие ошибки Last name - OK")

    # #Вызов ошибки Notes
    # page.get_by_label("Notes:").fill("A" * 2001)
    # page.get_by_role("button", name="Submit").click()
    # expect(page.locator('[name="notesvalidation"]')).to_be_visible()
    # print("Ошибка Notes - OK")
    #
    # # Скрытие ошибки Notes
    # page.get_by_label("Notes:").fill("A" * 2000)
    # page.get_by_role("button", name="Submit").click()
    # page.wait_for_timeout(1000)
    # expect(page.locator('[name="notesvalidation"]')).to_be_hidden()
    # print("Скрытие ошибки Notes - OK")



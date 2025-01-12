from os import error

from playwright.sync_api import Page, expect
from ..utils.data import *

def test_valid_input_validation(page: Page) -> None:
    page.goto(URL)
    """Заполнение полей валидными данными и их отправка"""
    page.get_by_label("First name:").click()
    page.get_by_label("First name:").fill("Vasia")
    page.get_by_label("First name:").press("Tab")
    page.get_by_label("Last name:").fill("Pupkin-Lapukin")
    page.get_by_label("Last name:").press("Tab")
    page.get_by_label("Age:").fill("80")
    page.get_by_label("Age:").press("Tab")
    page.get_by_label("Country:").select_option("Belarus")
    page.get_by_label("Country:").press("Tab")
    page.get_by_label("Notes:").fill("Test notes!!! !@# }{[]\n\n\nLLDM")
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
    page.get_by_label("Age:").fill("18")
    page.get_by_label("First name:").fill("V")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator('[name="firstnamevalidation"]')).to_be_visible()
    print("Ошибка First name - OK")

    # Вызов ошибки поля Last name
    page.get_by_label("Last name:").fill("1234567890")
    page.get_by_role("button", name="Submit").click()
    error_label = page.query_selector('label[name="surnamevalidation"]')
    actual_style = error_label.get_attribute("style")
    expect(page.locator('[name="surnamevalidation"]')).to_be_visible()
    print("Ошибка Last name - OK")

    #Скрытие ошибки Last name
    page.get_by_label("Last name:").fill("12345678901")
    page.get_by_role("button", name="Submit").click()
    final_style = error_label.get_attribute("style")
    if actual_style != final_style:
        print("Скрытие ошибки Last name - OK")
    else:
        print("Ошибка поля Last name не скрыта!!!")

    #Вызов ошибки Notes
    page.get_by_label("Notes:").fill("A" * 2001)
    page.get_by_role("button", name="Submit").click()
    error_notes = page.query_selector('label[name="notesvalidation"]')
    actual_style = error_notes.get_attribute("style")
    expect(page.locator('[name="notesvalidation"]')).to_be_visible()
    print("Ошибка Notes - OK")

    # Скрытие ошибки Notes
    page.get_by_label("Notes:").fill("A" * 2000)
    page.get_by_role("button", name="Submit").click()
    final_style = error_notes.get_attribute("style")
    if actual_style != final_style:
        print("Скрытие ошибки Notes - OK")
    else:
        print("Ошибка поля Notes не скрыта!!!")



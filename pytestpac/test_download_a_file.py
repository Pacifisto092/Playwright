import os

from playwright.sync_api import Page


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as d_file:
        # page.locator("//a[text()='LambdaTest.txt']").click() #так показано в статье
        page.get_by_role("link", name="LambdaTest.txt").click()
        f_url = d_file.value.url
        print(f_url) #урла для скачивания файла
        print(d_file.value.path()) #путь сохранения файла

        current_working_dir = os.getcwd() #Сохраните путь в переменной

        file_path = os.path.join(current_working_dir, "downloads/file.txt") #Используйте  функцию join для
                                                                             # объединения двух каталогов.

        d_file.value.save_as(file_path) #сохраним файл в папке загрузок.
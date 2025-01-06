import os

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/upload")

    """создадим «текущий рабочий путь к каталогу» и соединим этот путь с файлом, который мы хотим загрузить."""
    current_working_dir = os.getcwd()
    file_path = os.path.join(current_working_dir, "downloads/file.txt")
    page.set_input_files('#file-upload', file_path)

    page.get_by_role("button", name="Upload").click()

    page.wait_for_timeout(10000)
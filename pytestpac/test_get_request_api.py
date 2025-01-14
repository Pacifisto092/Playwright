import requests
from playwright.sync_api import Playwright, sync_playwright, expect

def test_run(playwright: Playwright) -> None:

    #status code 200
    resp = requests.get("https://reqres.in/api/users/2")
    assert resp.status_code == 200
    print(resp.status_code)

    # status code 404
    resp = requests.get("https://reqres.in/api/users/23")
    assert resp.status_code == 404
    print(resp.status_code)

with sync_playwright() as playwright:
    test_run(playwright)
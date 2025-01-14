import requests

from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:

    #status code 200
    resp = requests.get("https://reqres.in/api/users/2")
    print(resp.status_code)

    # status code 404
    resp = requests.get("https://reqres.in/api/users/23")
    print(resp.status_code)

with sync_playwright() as playwright:
 run(playwright)
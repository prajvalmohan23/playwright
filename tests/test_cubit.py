from playwright.sync_api import Page, expect


BASE_URL = "http://127.0.0.1:8000/"

def test_cube(page: Page):
    page.goto(BASE_URL)
    input = page.get_by_placeholder("enter number...")
    input.fill("5")
    btn = page.get_by_role("button", name="Cube")
    btn.click()
    result = page.locator("css=p#result")

    expect(result).to_contain_text("125")

def test_empty(page: Page):
    page.goto(BASE_URL)
    input = page.get_by_placeholder("enter number...")
    input.fill("")
    btn = page.get_by_role("button", name="Cube")
    btn.click()
    result = page.locator("css=p#result")

    expect(result).to_contain_text("Enter something!")


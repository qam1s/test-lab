from playwright.sync_api import Page, expect


def test_open_page(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/docs")
    expect(page).to_have_title("App - Swagger UI")

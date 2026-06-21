import pytest
from playwright.sync_api import Page, expect

def test_github_navigation_and_search(page: Page):

    page.goto("https://github.com/")
    
    expect(page).to_have_title("GitHub · Change is constant. GitHub keeps you ahead. · GitHub")
    
    page.screenshot(path="github_home.png")
    print("\n[UI INFO] Скриншот успешно сохранен как github_home.png")
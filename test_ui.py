# import pytest
# from playwright.sync_api import Page, expect

# def test_github_navigation_and_search(page: Page):

#     page.goto("https://github.com/")
    
#     expect(page).to_have_title("GitHub · Change is constant. GitHub keeps you ahead. · GitHub")
    
#     page.screenshot(path="github_home.png")
#     print("\n[UI INFO] Скриншот успешно сохранен как github_home.png")

from playwright.sync_api import Page, expect
from pages.github_home_page import GitHubHomePage
from pages.github_login_page import GitHubLoginPage
import re

def test_hub(page: Page):
    home_page = GitHubHomePage(page=page)
    home_page.open()
    expect(page).to_have_title(re.compile("GitHub"))
    login_page = home_page.click_sign_in()
    expect(login_page.login_header).to_be_visible()
    login_page.type_username("testusername")
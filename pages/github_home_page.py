from playwright.sync_api import Page
from pages.github_login_page import GitHubLoginPage

class GitHubHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.sign_in_button = page.locator("a.HeaderMenu-link--sign-in")

    def open(self):
        self.page.goto("https://github.com/")
        return self

    def click_sign_in(self) -> GitHubLoginPage:
        self.sign_in_button.click()
        return GitHubLoginPage(self.page)
from playwright.sync_api import Page, Locator

class GitHubLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_header = page.locator('h1:has-text("Sign in to GitHub")')
    def type_username(self, username: str):
        self.page.locator("#login_field").fill(username)
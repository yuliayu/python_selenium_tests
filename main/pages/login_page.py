from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class LoginPage(BasePage):
    locators = {
        "username": "//input[@id='username']",
        "password": "//input[@id='password']",
        "login_button": "//button[@class='radius']"
    }
    def open(self):
        self.browser.get("http://the-internet.herokuapp.com/login")

# Login with username and password
    def login(self, username='', password=''):
        self.enter_text(LoginPage.locators["username"], username)
        self.enter_text(LoginPage.locators["password"], password)
        self.find(LoginPage.locators["login_button"]).click()

from selenium.webdriver.common.by import By
from .base_page_object import BasePage

class SecurePage(BasePage):
    locators = {
    "message": '//div[@id="flash"]'
    }

# Get the validation message text
    def get_message(self):
        message = self.find(SecurePage.locators['message'])
        return message.text
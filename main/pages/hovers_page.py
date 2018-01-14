from .base_page_object import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class HoversPage(BasePage):
    locators={
    "avatar1":"//div[@class='figure'][1]",
    "avatar2":"//div[@class='figure'][2]",
    "avatar3:":"//div[@class='figure'][3]",
    "user1":"//div[@class='figure'][1]/div[@class='figcaption']",
    "user2":"//div[@class='figure'][2]/div[@class='figcaption']",
    "user3":"//div[@class='figure'][3]/div[@class='figcaption']"

    }

    def open(self):
        self.browser.get("http://the-internet.herokuapp.com/hovers")

# Hover over the avatar
    def hover_item(self,id):
        value='avatar'+str(id)
        element = self.find(HoversPage.locators[value])
        ActionChains(self.browser).move_to_element(element).perform()

# Get the profile text
    def get_hover_text(self,id):
        value='user'+str(id)
        message = self.find(HoversPage.locators[value])
        return message.text

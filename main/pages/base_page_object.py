
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, browser, base_url='http://the-internet.herokuapp.com/'):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 30

# Find the element with specified xpath
    def find(self,xpath):
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.browser.find_element_by_xpath(xpath)
            return element
# Find element and enter text
    def enter_text(self, xpath, text =''):
        self.find(xpath).send_keys(text)

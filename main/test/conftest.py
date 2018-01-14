import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Firefox()
    yield browser
    browser.close()

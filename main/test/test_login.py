from selenium import webdriver
from main.pages import *

# Verify successful login scenario
def test_login_successful(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login('tomsmith','SuperSecretPassword!')
    secure_page = SecurePage(browser)
    secure_message = secure_page.get_message()
    text = 'You logged into a secure area!'
    assert (text in secure_message)

#Verify invalid username scenario
def test_wrong_username(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login('wrong','')
    secure_page = SecurePage(browser)
    secure_message = secure_page.get_message()
    text = 'Your username is invalid!'
    assert (text in secure_message)

#Verify incorrect password scenario
def test_wrong_password(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login('tomsmith','password')
    secure_page = SecurePage(browser)
    secure_message = secure_page.get_message()
    text = 'Your password is invalid!'
    assert (text in secure_message)


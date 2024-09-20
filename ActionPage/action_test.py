import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locator_page.locator_test import LoginLocator, NegativeLoginPageLocators,OpenAccountPage, AboutPage, MenuHamburger


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def click_login(self):
        click_login = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(LoginLocator.LOGIN))
        click_login.click()

    def click_personal_banking_dropdown(self):
        click_personal_banking_dropdown = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(LoginLocator.PERSONAL_BANKING_DROPDOWN))
        click_personal_banking_dropdown.click()

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(LoginLocator.LOGIN_BUTTON))
        click_login_button.click()

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.USERNAME))
        enter_username.send_keys(username)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.PASSWORD))
        enter_password.send_keys(password)

    def click_signin_button(self):
        click_signin_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.SIGNIN_BUTTON))
        click_signin_button.click()

    def get_error_message_element1(self):
        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.ERROR_MESSAGE))

        return error_message_element


class LoginPage1:
    def __init__(self, driver):
        self.driver = driver

    def login_urls(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(NegativeLoginPageLocators.USERNAME_))
        enter_username.send_keys(username)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(NegativeLoginPageLocators.PASSWORD_))
        enter_password.send_keys(password)

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(NegativeLoginPageLocators.LOGIN_BUTTON_))
        click_login_button.click()
        time.sleep(5)

    def get_error_message_element(self):
        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NegativeLoginPageLocators.ERROR_MESSAGE))

        return error_message_element


class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    def login_urls(self, url):
        self.driver.get(url)

    def click_open_account(self):
        click_open_account = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OpenAccountPage.OPEN_ACCOUNT))
        click_open_account.click()


class AboutPage1:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def click_about_page(self):
        click_about_page = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located(AboutPage.ABOUT_PAGE))
        click_about_page.click()

    def click_leadership(self):
        click_leadership = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located(AboutPage.LEADERSHIP))
        click_leadership.click()

    def click_news_center(self):
        click_news_center = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located(AboutPage.NEWS_CENTER))
        click_news_center.click()

    def click_career(self):
        click_career = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located(AboutPage.CAREERS))
        click_career.click()

    def click_community(self):
        click_community = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located(AboutPage.COMMUNITY))
        click_community.click()

    def click_our_location(self):
        click_our_location = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located(AboutPage.OUR_LOCATION))
        click_our_location.click()

    def click_contact_us(self):
        click_contact_us = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AboutPage.CONTACT_US))
        click_contact_us.click()


class MenuHamburgerPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
            self.driver.get(url)

    def click_menu(self):
        click_menu = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(MenuHamburger.MENU))
        click_menu.click()

    def click_checking_deposit(self):
        click_checking_deposit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(MenuHamburger.CHECKING_DEPOSIT))
        click_checking_deposit.click()

    def enter_search_button(self, search):
        enter_search_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(MenuHamburger.SEARCH_BUTTON))
        enter_search_button.send_keys()










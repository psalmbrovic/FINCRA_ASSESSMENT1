import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ActionPage.action_test import LoginPage, LoginPage1, AccountPage,AboutPage1, MenuHamburgerPage


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()


# @pytest.fixture(scope="module")
# def driver_setup():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(20)
#     driver.maximize_window()
#     yield driver
#     driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url("https://www.firstbankonline.com/")
    return login_page


def test_login_page_first_bank_demo_website(login):
    login.click_login()
    login.click_personal_banking_dropdown()
    login.click_login_button()
    login.enter_username("demo")
    login.enter_password("demo@123")
    login.click_signin_button()
# Verify the error message
    error_message_element1 = login.get_error_message_element1()
    error_message = error_message_element1.text
    assert "Epic sadface: Username and password do not match any user in this service" in error_message, \
        "Error message does not match expected."

    print("Negative test passed: Username and password do not match any user in this service.")


@pytest.fixture(scope="module")
def driver_setup1():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()

# @pytest.fixture(scope="module")
# def driver_setup1():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(20)
#     driver.maximize_window()
#     yield driver
#     driver.quit()


@pytest.fixture(scope="module")
def login_gbp(driver_setup1):
    driver = driver_setup1
    login_page = LoginPage1(driver)
    login_page.login_urls("https://www.firstbankonline.com/")
    return login_page


def test_negative_login_on_first_bank_demo_website(login_gbp):
    login_gbp.enter_username("")
    login_gbp.enter_password("")
    login_gbp.click_login_button()

    # Verify the error message
    error_message_element = login_gbp.get_error_message_element()
    error_message = error_message_element.text
    assert "Epic sadface: Username and password do not match any user in this service" in error_message, \
        "Error message does not match expected."

    print("Negative test passed: Username and password do not match any user in this service.")

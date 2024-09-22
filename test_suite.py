import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ActionPage.action_test import LoginPage, OverViewPage, BalancesPage, PayInsPage, RefundPage, ConversionsPage, \
    SettlementPage, UserAndRolePage, LogoutPage


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
    login_page.login_url("https://app.fincra.com/auth/login")
    return login_page


def test_login_page_fin_cra_website(login):
    login.enter_email("abatansamuel@ymail.com")
    login.enter_paasword("Fr33dom007@FINCRA")
    login.click_login_button()


# # Verify the error message
#     error_message_element1 = login.get_error_message_element1()
#     error_message = error_message_element1.text
#     assert "Epic sadface: Username and password do not match any user in this service" in error_message, \
#         "Error message does not match expected."
#
#     print("Negative test passed: Username and password do not match any user in this service.")
#

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


@pytest.fixture(scope="module")
def driver_setup_1():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


# @pytest.fixture(scope="module")
# def login(driver_setup1):
#     driver = driver_setup1
#     login_page = LoginPage(driver)
#     login_page.login_url("https://app.fincra.com/auth/login")
#     return login_page


def test_negative_test_login_page_fin_cra_website(login):
    login.enter_email("null")
    login.enter_paasword("null")
    login.click_login_button()


#
# @pytest.fixture(scope="module")
# def over_view(driver_setup):
#     driver = driver_setup
#     over_view_page = OverviewPage1(driver)
#     over_view_page.click_overview()
#     return over_view_page


def test_click_over_view_button_website(login):
    test_click_over_view_button = OverViewPage(login.driver)
    test_click_over_view_button.click_overview()


def test_click_balance(login):
    click_balance = BalancesPage(login.driver)
    click_balance.click_balance()


def test_log_out_page(login):
    click_log_out = LogoutPage(login.driver)
    click_log_out.click_logout()
    click_log_out.click_my_account()
    click_log_out.click_support()
    click_log_out.click_log_out()

    # # Verify the error message
    # error_message_element = login.get_error_message_element1()
    # error_message = error_message_element.text
    # assert "Epic sadface: Username and password do not match any user in this service" in error_message, \
    #     "Error message does not match expected."
    #
    # print("Negative test passed: Username and password do not match any user in this service.")

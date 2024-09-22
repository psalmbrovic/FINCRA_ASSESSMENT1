import os
import time


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locator_page.locator_test import LoginLocator, OverViewPages, Balance, PayIns, Refund, Conversions, Settlement, \
    UserAndRole, Logout


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.save_screenshot = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.EMAIL_ADDRESS))
        enter_email.send_keys(email)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.PASSWORD))
        enter_password.send_keys(password)

    def click_login_button(self):
        try:
            click_login_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(LoginLocator.LOG_IN))
            click_login_button.click()
            time.sleep(10)
        except Exception as e:
            # Capture screenshot when there is an exception
            screenshot_path = os.path.join(os.getcwd(), 'error_screenshot.png')
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at {screenshot_path} due to exception: {e}")
            raise e  # Re-raise the exception after taking the screenshot



class OverViewPage:
    def __init__(self, driver):
        self.driver = driver

    def click_overview(self):
        click_overview = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OverViewPages.OVER_VIEW))
        click_overview.click()
    #
    # def enter_password(self, password):
    #     enter_password = WebDriverWait(self.driver, 20).until(
    #         EC.presence_of_element_located(NegativeLoginPageLocators.PASSWORD_))
    #     enter_password.send_keys(password)
    #
    # def click_login_button(self):
    #     click_login_button = WebDriverWait(self.driver, 20).until(
    #         EC.presence_of_element_located(NegativeLoginPageLocators.LOGIN_BUTTON_))
    #     click_login_button.click()
    #     time.sleep(5)
    #
    # def get_error_message_element(self):
    #     error_message_element = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located(NegativeLoginPageLocators.ERROR_MESSAGE))
    #
    #     return error_message_element


class BalancesPage:
    def __init__(self, driver):
        self.driver = driver

    def click_balance(self):
        click_balance = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Balance.BALANCES))
        click_balance.click()


class PayInsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_pay_ins(self):
        click_pay_ins = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PayIns.PAY_INS))
        click_pay_ins.click()

    def click_history(self):
        click_history = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PayIns.PAY_INS))
        click_history.click()

    def click_virtual_account(self):
        click_virtual_account = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PayIns.VIRTUAL_ACCOUNT))
        click_virtual_account.click()

    def click_payment_link(self):
        click_payment_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PayIns.PAYMENT_LINK))
        click_payment_link.click()

    def click_charge_back(self):
        click_charge_back = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PayIns.CHARGEBACKS))
        click_charge_back.click()

    def click_refund(self):
        click_refund = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PayIns.REFUND))
        click_refund.click()


class RefundPage:
    def __init__(self, driver):
        self.driver = driver

    def click_pay_out(self):
        click_pay_out = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Refund.PAY_OUT))
        click_pay_out.click()

    def click_history(self):
        click_history = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Refund.HISTORY))
        click_history.click()

    def click_beneficiary(self):
        click_beneficiary = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Refund.BENEFICIARIES))
        click_beneficiary.click()

    def click_make_payment(self):
        click_make_payment = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Refund.MAKE_PAYMENT))
        click_make_payment.click()


class ConversionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_conversions(self):
        click_conversions = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Conversions.CONVERSIONS))
        click_conversions.click()

    def click_contact_support(self):
        click_contact_support = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Conversions.CONTACT_SUPPORT))
        click_contact_support.click()

    def click_cancel(self):
        click_cancel = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Conversions.CANCEL))
        click_cancel.click()


class SettlementPage:
    def __init__(self, driver):
        self.driver = driver

    def click_settlement(self):
        click_settlement = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Settlement.SETTLEMENT))
        click_settlement.click()

    def click_leadership(self):
        click_leadership = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Settlement.LEADERSHIP))
        click_leadership.click()

    def click_new_center(self):
        click_new_center = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Settlement.NEWS_CENTER))
        click_new_center.click()

    def click_career(self):
        click_career = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Settlement.CAREERS))
        click_career.click()

    def click_community(self):
        click_community = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Settlement.COMMUNITY))
        click_community.click()

    def click_our_location(self):
        click_our_location = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Settlement.OUR_LOCATION))
        click_our_location.click()

    def click_contact_us(self):
        click_contact_us = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Settlement.CONTACT_US))
        click_contact_us.click()


class UserAndRolePage:
    def __init__(self, driver):
        self.driver = driver

    def click_user_and_role(self):
        click_user_and_role = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(UserAndRole.USER_AND_ROLE))
        click_user_and_role.click()

    def click_manage_user(self):
        click_manage_user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(UserAndRole.MANAGE_USER))
        click_manage_user.click()

    def click_manage_role(self):
        click_manage_role = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(UserAndRole.MANAGE_ROLES))
        click_manage_role.click()

    def click_create_new_user(self):
        click_create_new_user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(UserAndRole.CREATE_NEW_USER))
        click_create_new_user.click()

    def click_back_button(self):
        click_back_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(UserAndRole.BACK_BUTTON))
        click_back_button.click()

    def click_search_button(self):
        click_search_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(UserAndRole.SEARCH_BUTTON))
        click_search_button.click()


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        #self.actions = ActionChains(self.driver)

    # def click_logout(self):
    #     click_logout = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located(Logout.LOGOUT_BUTTON))
    #     actions = ActionChains(driver)
    #     actions.move_to_element(Logout.LOGOUT_BUTTON).perform()

    def click_logout(self):
        # Wait for the logout button to be present
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Logout.LOGOUT_BUTTON)
        )

        actions = ActionChains(self.driver)

        actions.move_to_element(logout_button).click().perform()

    def click_support(self):
        click_support = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Logout.SUPPORT))
        click_support.click()

    def click_my_account(self):
        click_my_account = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Logout.MY_ACCOUNT))
        click_my_account.click()

    def click_log_out(self):
        click_log_out = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Logout.LOG_OUT))
        click_log_out.click()

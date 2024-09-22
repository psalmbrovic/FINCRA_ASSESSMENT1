from selenium.webdriver.common.by import By


class LoginLocator:
    EMAIL_ADDRESS = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    KEEP_ME_SIGNIN = (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div[2]/form/div[4]/label/span[1]')
    FORGET_LOGIN = (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div[2]/form/div[3]/a')
    LOG_IN = (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div[2]/form/button/span')
    CREATE_ACCOUNT = (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div[2]/form/div[5]/a')
    EYE_ICON = (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div[2]/form/div[2]/div[2]/img')
    SUCCESSFUL_MESSAGE = (By.LINK_TEXT, "Please verify your information and try again.")
    ERROR_MESSAGE = (By.XPATH, '')


class OverViewPages:
    OVER_VIEW = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[1]/a/span[2]/span')


class Balance:
    BALANCES = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[2]/a/span[2]/span')


class PayIns:
    PAY_INS = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[3]/div/button/span[2]')
    HISTORY = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[3]/div/a[1]/span/span')
    VIRTUAL_ACCOUNT = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[3]/div/a[2]/span/span')
    PAYMENT_LINK = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[3]/div/a[3]/span/span')
    CHARGEBACKS = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[3]/div/a[4]/span/span')
    REFUND = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[3]/div/a[5]/span/span')


class Refund:
    PAY_OUT = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[4]/div/button/span[2]')
    HISTORY = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[4]/div/a[1]/span/span')
    BENEFICIARIES = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[4]/div/a[2]/span/span')
    MAKE_PAYMENT = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[4]/div/a[3]/span/span')


class Conversions:
    CONVERSIONS = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[5]/a/span[2]/span')
    CONTACT_SUPPORT = (By.XPATH, '/html/body/div[17]/div/div/div[2]/div/div/a/button/span')
    CANCEL = (By.XPATH, '/html/body/div[17]/div/div/div[2]/div/div/button')


class Settlement:
    SETTLEMENT = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[6]/a/span[2]/span')
    LEADERSHIP = (By.XPATH, '//*[@id="main-content"]/div[2]/ul/li[2]/a')
    NEWS_CENTER = (By.XPATH, '//*[@id="main-content"]/div[2]/ul/li[3]/a')
    CAREERS = (By.XPATH, '//*[@id="main-content"]/div[2]/ul/li[4]/a')
    COMMUNITY = (By.XPATH, '//*[@id="main-content"]/div[2]/ul/li[5]/a')
    OUR_LOCATION = (By.XPATH, '//*[@id="main-content"]/div[2]/ul/li[6]/a')
    CONTACT_US = (By.XPATH, '//*[@id="main-content"]/div[2]/ul/li[7]/a')


class UserAndRole:
    USER_AND_ROLE = (By.XPATH, '//*[@id="__next"]/div/div/nav/div/ul[2]/li[7]/a/span[2]/span')
    MANAGE_USER = (By.XPATH, '//*[@id="__next"]/div/div/div/div/div[5]/div/div[2]/div/div[1]/div/div/p')
    MANAGE_ROLES = (By.XPATH, '//*[@id="__next"]/div/div/div/div/div[5]/div/div[2]/div/div[2]/div/div/div/h5')
    CREATE_NEW_USER = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[5]/div/div[2]/button')
    BACK_BUTTON = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[5]/div/div[1]/div/a/h6')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[5]/div/div[3]/div/div/div[2]/div/div[1]/div/div/span')


class Logout:
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/div/div/div[3]/div[3]/div/div[1]/div[2]/span[1]')
    SUPPORT = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[3]/div[3]/div/div[2]/div[1]/a[1]/div/span[2]')
    MY_ACCOUNT = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[3]/div[3]/div/div[2]/div[1]/a[2]/div/span[2]')
    LOG_OUT = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[3]/div[3]/div/div[2]/div[2]/button/span')

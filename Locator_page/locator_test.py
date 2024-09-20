from selenium.webdriver.common.by import By


class LoginLocator:
    LOGIN = (By.CSS_SELECTOR, "#wrap > header > ul.secondary-nav > li:nth-child(3) > button")
    PERSONAL_BANKING_DROPDOWN = (By.XPATH, '//*[@id="main-content"]/div[1]/form/select')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="main-content"]/div[1]/form/button')
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "PASSWORD")
    SIGNIN_BUTTON = (By.XPATH, '//*[@id="login-password-form"]/bannoweb-flex-wrapper[2]/div/jha-button')
    ERROR_MESSAGE = (By.LINK_TEXT, "Please verify your information and try again.")


class NegativeLoginPageLocators:
    USERNAME_ = (By.NAME, "user-name")
    PASSWORD_ = (By.NAME, "password")
    LOGIN_BUTTON_ = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, '//*[@id="login-password-form"]/bannoweb-flex-wrapper[2]/div/jha-button')


class OpenAccountPage:
    OPEN_ACCOUNT = (By.XPATH, '//*[@id="wrap"]/header/ul[1]/li[3]/a')


class AboutPage:
    ABOUT_PAGE = (By.XPATH, '//*[@id="wrap"]/header/ul[1]/li[1]/a')
    LEADERSHIP = (By.XPATH, '//*[@id="main-content"]/div[2]/ul/li[2]/a')
    NEWS_CENTER = (By.XPATH, '//*[@id="main-content"]/div[2]/ul/li[3]/a')
    CAREERS = (By.XPATH, '//*[@id="main-content"]/div[2]/ul/li[4]/a')
    COMMUNITY = (By.XPATH, '//*[@id="main-content"]/div[2]/ul/li[5]/a')
    OUR_LOCATION = (By.XPATH, '//*[@id="main-content"]/div[2]/ul/li[6]/a')
    CONTACT_US = (By.XPATH, '//*[@id="main-content"]/div[2]/ul/li[7]/a')


class MenuHamburger:
    MENU = (By.XPATH, '//*[@id="wrap"]/header/button')
    CHECKING_DEPOSIT = (By.XPATH, '//*[@id="menu-item-316"]/a')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="wrap"]/header/div/div/div/div/div/form/input')



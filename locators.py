from selenium.webdriver.common.by import By


class Locators:
    # Header
    ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")

    # Главная страница
    LOGIN_PAGE_BTN = (By.XPATH, "//button[text() = 'Войти в аккаунт']")

    # Страница входа
    LOGIN_TITLE = (By.XPATH, "//div[contains(@class, 'Auth_login')]/h2[text() = 'Вход']")
    NAME_INPUT = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")
    LOGIN_BTN = (By.XPATH, "//button[text() = 'Войти']")
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")

    # Страница регистрации
    PASSWORD_INPUT = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")
    REGISTER_BTN = (By.XPATH, "//button[text() = 'Зарегистрироваться']")

    # Личный кабинет
    PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile']")




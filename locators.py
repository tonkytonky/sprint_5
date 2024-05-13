from selenium.webdriver.common.by import By


class Locators:
    # Header
    ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text() = 'Конструктор']")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")

    # Главная страница
    LOGIN_PAGE_BTN = (By.XPATH, "//button[text() = 'Войти в аккаунт']")

    # Страница входа
    LOGIN_TITLE = (By.XPATH, "//div[contains(@class, 'Auth_login')]/h2[text() = 'Вход']")
    NAME_INPUT = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")
    LOGIN_BTN = (By.XPATH, "//button[text() = 'Войти']")
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")
    PASSWORD_RECOVER_LINK = (By.XPATH, "//a[@href='/forgot-password']")

    # Страница регистрации
    PASSWORD_INPUT = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")
    REGISTER_BTN = (By.XPATH, "//button[text() = 'Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")

    # Личный кабинет
    PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile' and text() = 'Профиль']")
    EXIT_BTN = (By.XPATH, "//button[text() = 'Выход']")

    # Конструктор
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text() = 'Соберите бургер']")

    BUN_ANCHOR = (By.XPATH, "//span[text()='Булки']")
    SOUSE_ANCHOR = (By.XPATH, "//span[text()='Соусы']")
    FILLING_ANCHOR = (By.XPATH, "//span[text()='Начинки']")

    BUN_TITLE = (By.XPATH, "//h2[text() = 'Булки']")
    SOUSE_TITLE = (By.XPATH, "//h2[text() = 'Соусы']")
    FILLING_TITLE = (By.XPATH, "//h2[text() = 'Начинки']")

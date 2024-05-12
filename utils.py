from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import settings
from locators import Locators


class Utils:
    @staticmethod
    def wait_text_to_be_present_in_element(driver, locator: tuple[str, str], text):
        WebDriverWait(driver, settings.TIMEOUT).until(
            ec.text_to_be_present_in_element(
                locator, text))

    @staticmethod
    def click_element(driver, locator: tuple[str, str]):
        element = WebDriverWait(driver, settings.TIMEOUT).until(
            ec.visibility_of_element_located(
                locator))
        element.click()

    @staticmethod
    def send_keys_to_element(driver, locator: tuple[str, str], keys):
        element = WebDriverWait(driver, settings.TIMEOUT).until(
            ec.visibility_of_element_located(
                locator))
        element.send_keys(keys)

    @staticmethod
    def get_element(driver, locator: tuple[str, str]):
        try:
            element = WebDriverWait(driver, settings.TIMEOUT).until(
                ec.visibility_of_element_located(
                    locator))
        except TimeoutException:
            element = None

        return element

    @staticmethod
    def fill_and_send_registration_form(driver, name, email, password):
        # Заполнить поля формы регистрации
        Utils.send_keys_to_element(driver, Locators.NAME_INPUT, name)
        Utils.send_keys_to_element(driver, Locators.EMAIL_INPUT, email)
        Utils.send_keys_to_element(driver, Locators.PASSWORD_INPUT, password)
        # Подтвердить регистрацию
        Utils.click_element(driver, Locators.REGISTER_BTN)

    @staticmethod
    def fill_and_send_login_form(driver, email, password):
        # Заполнить данные пользователя
        Utils.send_keys_to_element(driver, Locators.EMAIL_INPUT, email)
        Utils.send_keys_to_element(driver, Locators.PASSWORD_INPUT, password)
        # Подтвердить вход
        Utils.click_element(driver, Locators.LOGIN_BTN)

    @staticmethod
    def login(driver, email, password):
        Utils.click_element(driver, Locators.LOGIN_PAGE_BTN)
        Utils.fill_and_send_login_form(driver, email=email, password=password)

    @staticmethod
    def navigate_to_profile_page(driver):
        Utils.click_element(driver, Locators.ACCOUNT_LINK)

    @staticmethod
    def is_user_authorized(driver):
        Utils.navigate_to_profile_page(driver)
        # Дождаться ссылки на Профиль
        profile_link = Utils.get_element(driver, Locators.PROFILE_LINK)
        return bool(profile_link)

    @staticmethod
    def navigate_to_registration_page(driver):
        Utils.navigate_to_profile_page(driver)
        Utils.click_element(driver, Locators.REGISTER_LINK)

    @staticmethod
    def navigate_to_password_recover_page(driver):
        Utils.navigate_to_profile_page(driver)
        Utils.click_element(driver, Locators.PASSWORD_RECOVER_LINK)

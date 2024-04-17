from faker import Faker

from data import TestData
from locators import Locators
from utils import Utils

fake = Faker()


class TestAuthorization:

    def test_registration(self, driver):
        # Открыть страницу регистрации
        Utils.click_element(driver, Locators.ACCOUNT_LINK)
        Utils.click_element(driver, Locators.REGISTER_LINK)

        # Заполнить поля формы регистрации
        Utils.send_keys_to_element(driver, Locators.NAME_INPUT, fake.name())
        Utils.send_keys_to_element(driver, Locators.EMAIL_INPUT, fake.email())
        Utils.send_keys_to_element(driver, Locators.PASSWORD_INPUT, fake.password())

        # Подтвердить регистрацию
        Utils.click_element(driver, Locators.REGISTER_BTN)

        # Дождаться перехода на страницу входа -> Регистрация успешна
        Utils.wait_text_to_be_present_in_element(driver, Locators.LOGIN_TITLE, text="Вход")

    def test_login_via_login_page_btn(self, driver):
        # Перейти на страницу входа
        Utils.click_element(driver, Locators.LOGIN_PAGE_BTN)

        # Заполнить данные пользователя
        Utils.send_keys_to_element(driver, Locators.EMAIL_INPUT, TestData.TEST_EMAIL)
        Utils.send_keys_to_element(driver, Locators.PASSWORD_INPUT, TestData.TEST_PASSWORD)

        # Подтвердить вход
        Utils.click_element(driver, Locators.LOGIN_BTN)

        # Открыть Личный кабинет -> Вход успешен
        Utils.click_element(driver, Locators.ACCOUNT_LINK)
        Utils.wait_text_to_be_present_in_element(driver, Locators.PROFILE_LINK, text="Профиль")

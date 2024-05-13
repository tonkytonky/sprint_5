import pytest
from assertpy import assert_that
from faker import Faker

from data import TestData
from locators import Locators
from utils import Utils

fake = Faker()


class TestAuthorization:

    @pytest.mark.skip
    def test_registration(self, driver):
        """
        Успешная регистрация.
        """
        Utils.navigate_to_registration_page(driver)

        Utils.fill_and_send_registration_form(
            driver,
            name=fake.name(),
            email=fake.email(),
            password=fake.password(),
        )

        is_login_title_visible = bool(Utils.get_element(driver, Locators.LOGIN_TITLE))

        description = "Регистрация не выполнена"
        assert_that(is_login_title_visible).described_as(description).is_true()

    def test_login_via_login_page_btn(self, driver):
        """
        Вход по кнопке "Войти в аккаунт" на главной странице.
        """
        # Перейти на страницу входа по кнопке "Войти в аккаунт"
        Utils.click_element(driver, Locators.LOGIN_PAGE_BTN)
        Utils.fill_and_send_login_form(driver, email=TestData.TEST_EMAIL, password=TestData.TEST_PASSWORD)

        description = "Авторизация не удалась"
        assert_that(Utils.is_user_authorized(driver)).described_as(description).is_true()

    def test_login_via_personal_account_btn(self, driver):
        """
        Вход через кнопку "Личный кабинет".
        """
        # Перейти на страницу входа по кнопке "Личный кабинет"
        Utils.click_element(driver, Locators.ACCOUNT_LINK)
        Utils.fill_and_send_login_form(driver, email=TestData.TEST_EMAIL, password=TestData.TEST_PASSWORD)

        description = "Авторизация не удалась"
        assert_that(Utils.is_user_authorized(driver)).described_as(description).is_true()

    def test_login_via_registration_page(self, driver):
        """
        Вход через кнопку в форме регистрации.
        """
        Utils.navigate_to_registration_page(driver)

        # Перейти на страницу входа по кнопке "Войти"
        Utils.click_element(driver, Locators.LOGIN_LINK)
        Utils.fill_and_send_login_form(driver, email=TestData.TEST_EMAIL, password=TestData.TEST_PASSWORD)

        description = "Авторизация не удалась"
        assert_that(Utils.is_user_authorized(driver)).described_as(description).is_true()

    def test_login_via_password_recover_page(self, driver):
        """
        Вход через кнопку в форме восстановления пароля.
        """
        Utils.navigate_to_password_recover_page(driver)

        # Перейти на страницу входа по кнопке "Войти"
        Utils.click_element(driver, Locators.LOGIN_LINK)
        Utils.fill_and_send_login_form(driver, email=TestData.TEST_EMAIL, password=TestData.TEST_PASSWORD)

        description = "Авторизация не удалась"
        assert_that(Utils.is_user_authorized(driver)).described_as(description).is_true()

    def test_logout_via_exit_btn(self, driver):
        """
        Выход по кнопке "Выйти" в личном кабинете.
        """
        Utils.login(driver, email=TestData.TEST_EMAIL, password=TestData.TEST_PASSWORD)
        Utils.navigate_to_profile_page(driver)

        # Нажать на кнопку "Выйти"
        Utils.click_element(driver, Locators.EXIT_BTN)

        description = "Выход не был совершён"
        assert_that(Utils.is_user_authorized(driver)).described_as(description).is_false()

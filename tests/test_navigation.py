import pytest
from assertpy import assert_that

from data import TestData
from locators import Locators
from utils import Utils


class TestNavigation:

    def test_navigate_to_profile_page(self, driver):
        """
        Переход в Личный кабинет по клику на "Личный кабинет".
        """
        Utils.login(driver, email=TestData.TEST_EMAIL, password=TestData.TEST_PASSWORD)

        # Перейти в Личный кабинет
        Utils.click_element(driver, Locators.ACCOUNT_LINK)

        is_profile_link_visible = bool(Utils.get_element(driver, Locators.PROFILE_LINK))
        description = "Перейти в Личный кабинет не удалось"
        assert_that(is_profile_link_visible).described_as(description).is_true()

    @pytest.mark.parametrize(
        "constructor_locator",
        [
            Locators.CONSTRUCTOR_LINK,
            Locators.LOGO,
        ]
    )
    def test_navigate_from_profile_page_to_constructor(self, driver, constructor_locator):
        """
        Переход по клику на "Конструктор" и на логотип Stellar Burgers.
        """
        Utils.login(driver, email=TestData.TEST_EMAIL, password=TestData.TEST_PASSWORD)
        Utils.navigate_to_profile_page(driver)

        # Перейти в Конструктор
        Utils.click_element(driver, constructor_locator)

        is_constructor_header_visible = bool(Utils.get_element(driver, Locators.CONSTRUCTOR_TITLE))
        description = "Перейти в Конструктор не удалось"
        assert_that(is_constructor_header_visible).described_as(description).is_true()

from time import sleep

from assertpy import assert_that

from locators import Locators
from utils import Utils


class TestConstructor:

    def test_ingredients_navigation(self, driver):
        """
        Переходы к разделам:
            "Булки",
            "Соусы",
            "Начинки".
        """
        ingredients = (
            (Locators.FILLING_ANCHOR, Locators.FILLING_TITLE, "Начинки"),
            (Locators.SOUSE_ANCHOR, Locators.SOUSE_TITLE, "Соусы"),
            (Locators.BUN_ANCHOR, Locators.BUN_TITLE, "Булки"),
        )
        for ingredient in ingredients:
            ingredient_anchor, ingredient_title, ingredient_name = ingredient

            # Перейти к разделу определённых ингредиентов
            Utils.click_element(driver, ingredient_anchor)
            sleep(2)
            is_first_ingredient_visible = bool(Utils.get_element(driver, ingredient_title))

            description = f'Перейти к разделу ингредиентов "{ingredient_name}" не удалось'
            assert_that(is_first_ingredient_visible).described_as(description).is_true()

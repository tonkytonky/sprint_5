from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

import settings


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

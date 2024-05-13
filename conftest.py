import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import settings


@pytest.fixture(scope='function')
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service)
    chrome_driver.get(settings.URL)

    yield chrome_driver

    chrome_driver.quit()

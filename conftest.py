import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from flows import Flows
from pages import Pages
from utils.elements import ElementsUtils
from consts.env_consts import EnvConstants


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def elements(driver):
    return ElementsUtils(driver=driver)


@pytest.fixture(scope="function")
def pages(elements, driver):
    return Pages(elements=elements, driver=driver)


@pytest.fixture(scope="function")
def flows(elements, driver):
    return Flows(elements=elements, driver=driver)


@pytest.fixture(scope="function")
def navigate_to_checkout_page(pages, driver, elements):
    driver.get(EnvConstants.ADD_TO_CART)
    try:
        pages.add_to_cart.email_address
    except Exception as err:
        raise Exception(f"failed to properly load desried-screen\n{err}")
    yield

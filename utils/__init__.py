from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ElementsUtils:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_clickable(self, locator_type, locator_value):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
        except Exception as err:
            raise Exception(f"failed to properly wait for element-clickable: {err}")

        return element

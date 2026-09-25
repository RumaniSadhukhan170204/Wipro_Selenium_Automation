import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):

    SEARCH_BOX = "//input[@name='search']"
    SEARCH_BUTTON = "//button[contains(@class,'btn-default')]"
    PRODUCT_RESULTS = "//div[contains(@class,'product-thumb')]"

    def search_product(self, product_name):

        self.driver.find_element(
            By.XPATH,
            self.SEARCH_BOX
        ).send_keys(product_name)

        time.sleep(2)

        self.driver.find_element(
            By.XPATH,
            self.SEARCH_BUTTON
        ).click()

        time.sleep(3)

    def verify_product_displayed(self):

        try:

            return self.driver.find_element(
                By.XPATH,
                self.PRODUCT_RESULTS
            ).is_displayed()

        except:

            return False
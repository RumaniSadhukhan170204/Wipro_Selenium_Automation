from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, xpath):
        self.driver.find_element(
            By.XPATH,
            xpath
        ).click()

    def enter_text(self, xpath, text):
        self.driver.find_element(
            By.XPATH,
            xpath
        ).send_keys(text)

    def get_text(self, xpath):
        return self.driver.find_element(
            By.XPATH,
            xpath
        ).text

    def is_element_displayed(self, xpath):
        try:
            return self.driver.find_element(
                By.XPATH,
                xpath
            ).is_displayed()

        except:
            return False
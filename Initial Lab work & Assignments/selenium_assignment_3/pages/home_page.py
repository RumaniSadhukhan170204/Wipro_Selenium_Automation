from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open_website(self):
        self.driver.get(
            "https://testautomationpractice.blogspot.com/"
        )

    def enter_name(self, name):
        self.driver.find_element(
            By.XPATH,
            "//input[@id='name']"
        ).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(
            By.XPATH,
            "//input[@id='email']"
        ).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(
            By.XPATH,
            "//input[@id='phone']"
        ).send_keys(phone)

    def get_name(self):
        return self.driver.find_element(
            By.XPATH,
            "//input[@id='name']"
        ).get_attribute("value")

    def select_country(self, country):
        dropdown = self.driver.find_element(
            By.XPATH,
            "//select[@id='country']"
        )

        select = Select(dropdown)

        select.select_by_visible_text(country)

    def get_selected_country(self):
        dropdown = self.driver.find_element(
            By.XPATH,
            "//select[@id='country']"
        )

        select = Select(dropdown)

        return select.first_selected_option.text

    def hover_mouse(self):

        mouse_hover = self.driver.find_element(
            By.XPATH,
            "//button[contains(text(),'Point Me')]"
        )

        ActionChains(
            self.driver
        ).move_to_element(
            mouse_hover
        ).perform()

    def click_mobiles(self):

        mobiles = self.driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Mobiles')]"
        )

        mobiles.click()
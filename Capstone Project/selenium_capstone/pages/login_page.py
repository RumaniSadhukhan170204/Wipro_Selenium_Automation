import time

from pages.base_page import BasePage


class LoginPage(BasePage):

    MY_ACCOUNT = "//a[@title='My Account']"
    LOGIN_LINK = "//a[text()='Login']"
    EMAIL = "//input[@id='input-email']"
    PASSWORD = "//input[@id='input-password']"
    LOGIN_BUTTON = "//input[@value='Login']"
    ACCOUNT_HEADER = "//h2[text()='My Account']"

    def open_login_page(self):

        self.click_element(self.MY_ACCOUNT)

        time.sleep(2)

        self.click_element(self.LOGIN_LINK)

        time.sleep(2)

    def enter_email(self, email):

        self.enter_text(self.EMAIL, email)

        time.sleep(1)

    def enter_password(self, password):

        self.enter_text(self.PASSWORD, password)

        time.sleep(1)

    def click_login(self):

        self.click_element(self.LOGIN_BUTTON)

        time.sleep(3)

    def login(self, email, password):

        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def verify_login(self):

        return self.is_element_displayed(
            self.ACCOUNT_HEADER
        )
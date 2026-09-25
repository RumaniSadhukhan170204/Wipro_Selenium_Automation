import pytest

from pages.login_page import LoginPage

from utilities.config_reader import ConfigReader
from utilities.logger import Logger


class TestLogin:

    logger = Logger.get_logger()

    @pytest.mark.login
    def test_valid_login(self, driver):

        self.logger.info(
            "Starting Login Test"
        )

        config = ConfigReader()

        # Open website
        driver.get(
            config.get_value(
                "DEFAULT",
                "base_url"
            )
        )

        # Create Login Page object
        login_page = LoginPage(driver)

        # Open Login page
        login_page.open_login_page()

        # Get email and password from config.ini
        email = config.get_value(
            "LOGIN",
            "email"
        )

        password = config.get_value(
            "LOGIN",
            "password"
        )

        # Login
        login_page.login(
            email,
            password
        )

        # Verify Login
        assert login_page.verify_login()

        self.logger.info(
            "Login Test Passed"
        )
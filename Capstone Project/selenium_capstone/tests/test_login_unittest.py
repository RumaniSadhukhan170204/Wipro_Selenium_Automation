import unittest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage

from utilities.config_reader import ConfigReader


class TestLoginUnittest(
    unittest.TestCase
):

    def setUp(self):

        config = ConfigReader()

        browsername = config.get_value(
            "DEFAULT",
            "browser"
        )

        if browsername.lower() == "chrome":

            self.driver = webdriver.Chrome(
                service=ChromeService(
                    ChromeDriverManager().install()
                )
            )

        else:

            raise Exception(
                "Only Chrome is configured for Unittest"
            )

        self.driver.maximize_window()

        # Open website
        self.driver.get(
            config.get_value(
                "DEFAULT",
                "base_url"
            )
        )

    def test_valid_login(self):

        config = ConfigReader()

        # Create Login Page object
        login_page = LoginPage(
            self.driver
        )

        # Open Login page
        login_page.open_login_page()

        # Get email and password
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
        self.assertTrue(
            login_page.verify_login()
        )

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":

    unittest.main()
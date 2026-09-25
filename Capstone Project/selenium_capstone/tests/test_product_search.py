import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage

from utilities.csv_reader import CSVReader
from utilities.config_reader import ConfigReader
from utilities.logger import Logger


class TestProductSearch:

    logger = Logger.get_logger()

    @pytest.mark.search
    def test_product_search(self, driver):

        self.logger.info(
            "Starting Product Search Test"
        )

        config = ConfigReader()

        # Open website
        driver.get(
            config.get_value(
                "DEFAULT",
                "base_url"
            )
        )

        # Read test data from CSV
        data = CSVReader.read_csv(
            "test_data.csv"
        )[0]

        # Get email, password and product
        email = data["email"]

        password = data["password"]

        product = data["product"]

        # Create Login Page object
        login_page = LoginPage(driver)

        # Open Login page
        login_page.open_login_page()

        # Login
        login_page.login(
            email,
            password
        )

        # Verify Login
        assert login_page.verify_login()

        # Create Product Page object
        product_page = ProductPage(driver)

        # Search product
        product_page.search_product(
            product
        )

        # Verify product
        assert product_page.verify_product_displayed()

        self.logger.info(
            "Product Search Test Passed"
        )
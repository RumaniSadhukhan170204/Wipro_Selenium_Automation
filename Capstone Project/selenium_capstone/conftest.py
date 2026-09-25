import os
import pytest

from datetime import datetime

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utilities.config_reader import ConfigReader


@pytest.fixture
def driver():

    config = ConfigReader()

    browsername = config.get_value(
        "DEFAULT",
        "browser"
    )

    if browsername.lower() == "chrome":

        driver = webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager().install()
            )
        )

    elif browsername.lower() == "firefox":

        driver = webdriver.Firefox(
            service=FirefoxService(
                GeckoDriverManager().install()
            )
        )

    else:

        raise Exception(
            "Invalid browser name"
        )

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
        item,
        call
):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            screenshot_folder = os.path.join(
                os.path.dirname(__file__),
                "screenshots"
            )

            os.makedirs(
                screenshot_folder,
                exist_ok=True
            )

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            screenshot_name = (
                item.name
                + "_"
                + timestamp
                + ".png"
            )

            screenshot_path = os.path.join(
                screenshot_folder,
                screenshot_name
            )

            driver.save_screenshot(
                screenshot_path
            )

            print(
                "\nScreenshot saved:",
                screenshot_path
            )
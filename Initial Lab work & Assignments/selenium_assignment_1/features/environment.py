import os
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    context.driver.maximize_window()


def after_scenario(context, scenario):

    os.makedirs("../screenshots", exist_ok=True)

    safe_name = re.sub(
        r'[^A-Za-z0-9_-]',
        '_',
        scenario.name
    )

    screenshot_path = os.path.join(
        "../screenshots",
        safe_name + ".png"
    )

    context.driver.save_screenshot(screenshot_path)

    context.driver.quit()
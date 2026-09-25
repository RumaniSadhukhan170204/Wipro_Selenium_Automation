from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.passthenote.com/app/chaos")

time.sleep(2)

# Switch to outer iframe
driver.switch_to.frame(0)

# Switch to inner iframe
driver.switch_to.frame(0)

# Perform action
driver.find_element(
    By.ID,
    "nested-button"
).click()

time.sleep(3)

# Come back to main page
driver.switch_to.default_content()

driver.quit()
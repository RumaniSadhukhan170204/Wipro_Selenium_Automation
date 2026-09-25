from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

# First URL
driver.get("https://testautomationpractice.blogspot.com/")

parent_window = driver.current_window_handle

# Open new tab
driver.find_element(
    By.XPATH,
    "//button[contains(text(),'New Tab')]"
).click()

windows = driver.window_handles

# Move to second tab
for window in windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break

# Second URL
driver.get("https://www.wikipedia.org/")

time.sleep(2)

# Perform activity on second URL
driver.find_element(
    By.XPATH,
    "//a[contains(@href,'en.wikipedia.org')]"
).click()

time.sleep(2)

# Right-click on a particular link
element = driver.find_element(
    By.XPATH,
    "//a[contains(@href,'wiki')]"
)

action = ActionChains(driver)

action.context_click(element).perform()

time.sleep(2)

# Close second tab
driver.close()

# Come back to first tab
driver.switch_to.window(parent_window)

# Enter your name
driver.find_element(
    By.XPATH,
    "//input[@id='name']"
).send_keys("Rumani")

time.sleep(3)

driver.quit()
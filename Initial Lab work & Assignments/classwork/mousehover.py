from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Locate Point Me button
point_me = driver.find_element(By.XPATH, "//button[text()='Point Me']")

# Hover over Point Me
act = ActionChains(driver)
act.move_to_element(point_me).perform()

time.sleep(2)

# Find visible Mobiles option
mobiles = driver.find_elements(By.XPATH, "//a[text()='Mobiles']")

for mobile in mobiles:
    if mobile.is_displayed():
        mobile.click()
        break

time.sleep(3)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("https://text-compare.com/")
driver.maximize_window()

# Scroll to bottom
act = ActionChains(driver)
act.send_keys(Keys.END).perform()

time.sleep(2)

# Click About
driver.find_element(By.XPATH, "//a[text()='About']").click()

time.sleep(3)
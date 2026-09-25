from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Locate draggable box
source = driver.find_element(By.XPATH, "//div[@id='draggable']")

# Locate drop area
target = driver.find_element(By.XPATH, "//div[@id='droppable']")

# Drag and drop
act = ActionChains(driver)
act.drag_and_drop(source, target).perform()

time.sleep(3)

driver.quit()
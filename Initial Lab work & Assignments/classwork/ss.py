from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.save_screenshot("screenshot.png")

time.sleep(2)

driver.quit()
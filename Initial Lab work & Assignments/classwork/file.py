from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

# Upload file
file_input = driver.find_element(
    By.XPATH,
    "//input[@id='singleFileInput']"
)

file_input.send_keys(
    r"C:\Users\Asus\Downloads\Rumani_Sadhukhan_CV_FINAL.pdf"
)

# Click Upload Single File
driver.find_element(
    By.XPATH,
    "//form[@id='singleFileForm']//button"
).click()

time.sleep(3)

driver.quit()
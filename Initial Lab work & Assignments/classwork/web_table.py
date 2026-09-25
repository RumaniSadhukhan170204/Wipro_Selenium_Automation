from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

# Navigate to Pagination Web Table
table = driver.find_element(
    By.XPATH,
    "//h2[text()='Pagination Web Table']"
)

driver.execute_script(
    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
    table
)

time.sleep(2)

# Select checkbox of first row
driver.find_element(
    By.XPATH,
    "//table[@id='productTable']//tbody/tr[1]/td[4]/input"
).click()

time.sleep(2)

driver.quit()
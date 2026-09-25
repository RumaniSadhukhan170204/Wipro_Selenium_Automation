from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://text-compare.com/")
driver.maximize_window()


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(2)


driver.find_element(By.XPATH, "//a[text()='About']").click()

time.sleep(3)

driver.quit()
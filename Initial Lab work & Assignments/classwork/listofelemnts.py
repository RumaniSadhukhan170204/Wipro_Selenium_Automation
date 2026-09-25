from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(3)
links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links:", len(links))
for link in links:
    print(link.text)
driver.quit()
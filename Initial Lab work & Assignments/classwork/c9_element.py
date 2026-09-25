from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    text_box = driver.find_element(By.NAME, "my-text")
    text_box.send_keys("Umani")

    print("Element found and interaction successful.")

finally:
    driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browsername = "chrome"

if browsername.lower() == "chrome":
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

elif browsername.lower() == "firefox":
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )

driver.get("https://testautomationpractice.blogspot.com")

driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Rumani")



time.sleep(3)


driver.find_element(
    By.XPATH, "//button[contains(text(),'Simple Alert')]"
).click()

time.sleep(2)

alert = driver.switch_to.alert


print("Alert message:", alert.text)


alert.accept()


time.sleep(3)



driver.quit()


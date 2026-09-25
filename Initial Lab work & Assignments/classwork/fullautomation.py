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
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test@example.com")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9876543210")
driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("Kolkata, India")
driver.find_element(By.XPATH, "//input[@id='female']").click()
driver.find_element(By.XPATH, "//input[@id='monday']").click()
driver.find_element(By.XPATH, "//option[@value='india']").click()
driver.find_element(By.XPATH, "//option[@value='red']").click()
driver.find_element(By.XPATH, "//option[@value='cat']").click()
driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("08/31/2026")
driver.find_element(By.XPATH, "//input[@id='txtDate']").send_keys("31/08/2026")
driver.find_element(By.XPATH, "//input[@id='start-date']").send_keys("08/25/2026")
driver.find_element(By.XPATH, "//input[@id='end-date']").send_keys("08/31/2026")
time.sleep(3)


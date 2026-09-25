from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://text-compare.com/")
driver.maximize_window()

act = ActionChains(driver)
act.send_keys(Keys.END).perform()

time.sleep(2)


driver.find_element(By.XPATH, "//a[text()='About']").click()

time.sleep(3)
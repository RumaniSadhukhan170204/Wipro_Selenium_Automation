from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://text-compare.com/")
driver.maximize_window()

left = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
right = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

act = ActionChains(driver)

# Type text in left box
act.click(left).send_keys("Welcome to Selennium")

# Select all and copy
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL)

# Click right box and paste
act.click(right)
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL)

act.perform()

# Print what was pasted
print("Text pasted in right box:", right.get_attribute("value"))

time.sleep(3)
driver.quit()
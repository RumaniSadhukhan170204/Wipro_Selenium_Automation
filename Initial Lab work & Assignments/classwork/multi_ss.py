from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

# Screenshot 1
driver.save_screenshot("homepage.png")

# Scroll down
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);"
)

time.sleep(2)

# Screenshot 2
driver.save_screenshot("bottom.png")

# Scroll to top
driver.execute_script(
    "window.scrollTo(0, 0);"
)

time.sleep(2)

# Screenshot 3
driver.save_screenshot("top.png")

driver.quit()
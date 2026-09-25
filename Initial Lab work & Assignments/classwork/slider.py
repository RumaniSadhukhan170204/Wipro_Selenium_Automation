from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

# ---------------- SLIDER ----------------

slider = driver.find_element(By.ID, "slider-range")

driver.execute_script(
    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
    slider
)

time.sleep(1)

min_slider = driver.find_element(
    By.XPATH,
    "//*[@id='slider-range']/span[1]"
)

max_slider = driver.find_element(
    By.XPATH,
    "//*[@id='slider-range']/span[2]"
)

actions = ActionChains(driver)

# Automatically move MIN
actions.drag_and_drop_by_offset(min_slider, 40, 0).perform()

time.sleep(1)

# Automatically move MAX
actions.drag_and_drop_by_offset(max_slider, -40, 0).perform()

time.sleep(1)

# Get slider value
price_range = driver.find_element(
    By.ID,
    "amount"
).get_attribute("value")

# Example: "$75 - $214"
min_price = price_range.split("-")[0].strip()
max_price = price_range.split("-")[1].strip()

print("MIN:", min_price)
print("MAX:", max_price)


# ---------------- DATE PICKER ----------------

current_date = datetime.now()
future_date = current_date + timedelta(days=5)

current_day = str(current_date.day)
future_day = str(future_date.day)

# Date Picker 1 - Current Date
date_picker_1 = driver.find_element(
    By.ID,
    "datepicker"
)

driver.execute_script(
    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
    date_picker_1
)

time.sleep(1)

# Open calendar
date_picker_1.click()

time.sleep(1)

# Click current date
driver.find_element(
    By.XPATH,
    f"//div[@id='ui-datepicker-div']//a[text()='{current_day}']"
).click()

print("Selected Current Date:", date_picker_1.get_attribute("value"))

time.sleep(2)


# Date Picker 2 - Future Date
date_picker_2 = driver.find_element(
    By.ID,
    "txtDate"
)

driver.execute_script(
    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
    date_picker_2
)

time.sleep(1)

# Open calendar
date_picker_2.click()

time.sleep(1)

# Click future date
driver.find_element(
    By.XPATH,
    f"//div[@id='ui-datepicker-div']//a[text()='{future_day}']"
).click()

print("Selected Future Date:", date_picker_2.get_attribute("value"))
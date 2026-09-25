from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    yield driver
    driver.quit()


def test_page_title(driver):
    assert "Automation Testing Practice" in driver.title


def test_name_field(driver):
    name = driver.find_element(By.ID, "name")
    assert name.is_displayed()


def test_email_field(driver):
    email = driver.find_element(By.ID, "email")
    assert email.is_displayed()


def test_phone_field(driver):
    phone = driver.find_element(By.ID, "phone")
    assert phone.is_displayed()


def test_static_web_table(driver):
    table = driver.find_element(By.ID, "productTable")
    assert table.is_displayed()


def test_slider(driver):
    slider = driver.find_element(By.ID, "slider-range")
    assert slider.is_displayed()


def test_date_picker(driver):
    date_picker = driver.find_element(By.ID, "datepicker")
    assert date_picker.is_displayed()


def test_upload_file(driver):
    upload = driver.find_element(By.ID, "singleFileInput")
    assert upload.is_displayed()
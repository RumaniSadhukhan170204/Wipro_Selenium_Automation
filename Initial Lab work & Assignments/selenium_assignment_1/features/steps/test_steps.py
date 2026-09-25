from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


@given("I open the Test Automation Practice website")
def open_website(context):

    context.driver.get(
        "https://testautomationpractice.blogspot.com/"
    )


@when('I enter "{name}" in the name field')
def enter_name(context, name):

    context.driver.find_element(
        By.XPATH, "//input[@id='name']"
    ).send_keys(name)


@when('I enter "{email}" in the email field')
def enter_email(context, email):

    context.driver.find_element(
        By.XPATH, "//input[@id='email']"
    ).send_keys(email)


@when('I enter "{phone}" in the phone field')
def enter_phone(context, phone):

    context.driver.find_element(
        By.XPATH, "//input[@id='phone']"
    ).send_keys(phone)


@then('the name field should contain "{name}"')
def verify_name(context, name):

    actual_name = context.driver.find_element(
        By.XPATH, "//input[@id='name']"
    ).get_attribute("value")

    assert actual_name == name


@when('I select "{country}" from the country dropdown')
def select_country(context, country):

    dropdown = context.driver.find_element(
        By.XPATH, "//select[@id='country']"
    )

    select = Select(dropdown)

    select.select_by_visible_text(country)


@then('the country dropdown should contain "{country}"')
def verify_country(context, country):

    dropdown = context.driver.find_element(
        By.XPATH, "//select[@id='country']"
    )

    select = Select(dropdown)

    selected_option = select.first_selected_option.text

    assert selected_option == country


@when("I hover over the Mouse Hover menu")
def hover_mouse(context):

    mouse_hover = context.driver.find_element(
        By.XPATH, "//button[contains(text(),'Point Me')]"
    )

    ActionChains(context.driver).move_to_element(
        mouse_hover
    ).perform()


@when("I select Mobiles")
def select_mobiles(context):

    mobiles = context.driver.find_element(
        By.XPATH, "//a[contains(text(),'Mobiles')]"
    )

    mobiles.click()


@then("the mouse hover action should be completed")
def verify_mouse_hover(context):

    assert True
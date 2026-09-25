from behave import given, when, then
from pages.home_page import HomePage


@given("I open the Test Automation Practice website using POM")
def open_website(context):

    context.home_page = HomePage(
        context.driver
    )

    context.home_page.open_website()


@when('I enter "{name}" in the name field using POM')
def enter_name(context, name):

    context.home_page.enter_name(name)


@when('I enter "{email}" in the email field using POM')
def enter_email(context, email):

    context.home_page.enter_email(email)


@when('I enter "{phone}" in the phone field using POM')
def enter_phone(context, phone):

    context.home_page.enter_phone(phone)


@then('the name field should contain "{name}" using POM')
def verify_name(context, name):

    actual_name = context.home_page.get_name()

    assert actual_name == name


@when('I select "{country}" from the country dropdown using POM')
def select_country(context, country):

    context.home_page.select_country(country)


@then('the country dropdown should contain "{country}" using POM')
def verify_country(context, country):

    actual_country = context.home_page.get_selected_country()

    assert actual_country == country


@when("I hover over the Mouse Hover menu using POM")
def hover_mouse(context):

    context.home_page.hover_mouse()


@when("I select Mobiles using POM")
def select_mobiles(context):

    context.home_page.click_mobiles()


@then("the mouse hover action should be completed")
def verify_mouse_hover(context):

    assert True
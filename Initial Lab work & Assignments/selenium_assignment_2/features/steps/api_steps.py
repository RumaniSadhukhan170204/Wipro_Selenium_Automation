from behave import given, then
import requests


@given('I send a GET request for user "{user_id}"')
def send_get_request(context, user_id):

    url = "https://reqres.in/api/users/" + user_id

    context.response = requests.get(url)


@then("the response status code should be {expected_status:d}")
def verify_status_code(context, expected_status):

    assert context.response.status_code == expected_status


@then("the response should contain user data")
def verify_user_data(context):

    response_json = context.response.json()

    assert "data" in response_json
    assert "id" in response_json["data"]
    assert "email" in response_json["data"]


@then("the response time should be less than 5 seconds")
def verify_response_time(context):

    assert context.response.elapsed.total_seconds() < 5
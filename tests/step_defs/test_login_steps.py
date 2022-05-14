import pytest
import requests

from .conftest import LOGIN_ENDPOINT, REFRESH_TOKEN_ENDPOINT, get_authorization_headers
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/login.feature')


@pytest.fixture
def context():
    return {}


# Given Steps

@given(parsers.parse('an existing user with the username "{username}" and password "{password}"'))
@given(parsers.parse('a non existent user with the username "{username}" and password "{password}"'))
@given(parsers.parse('the username "{username}" and password "{password}"'))
def user_credentials(context, username, password):
    context['username'] = username if username != "N/A" else None
    context['password'] = password if password != "N/A" else None


# When Steps

@when('I send a POST request with the username and password')
def api_post_request(context):
    body = {'username': context['username'], 'password': context['password']}
    response = requests.post(LOGIN_ENDPOINT, data=body)
    context['response'] = response


@when('I send a GET request to refresh token with an authenticated user')
def api_get_request(context):
    response = requests.get(REFRESH_TOKEN_ENDPOINT, headers=get_authorization_headers())
    context['response'] = response


# Then Steps

@then(parsers.parse('the response does not contain the property "{access_token}"'))
def api_response_access_token(context, access_token):
    response_json = context['response'].json()
    assert access_token not in response_json

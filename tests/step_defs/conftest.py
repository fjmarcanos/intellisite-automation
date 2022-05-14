import requests

from pytest_bdd import then, parsers

# This file contains shared constants and functions across all test suites

INTELLISITE_BASE_URL = 'http://localhost:8080'

# API Endpoints

LOGIN_ENDPOINT = INTELLISITE_BASE_URL + '/auth/token'

REFRESH_TOKEN_ENDPOINT = INTELLISITE_BASE_URL + '/auth/refresh'

DETECTIONS_ENDPOINT = INTELLISITE_BASE_URL + '/detections'


# Shared functions

# Logs in a user and returns the header Authorization with the access_token to be used in tests cases
# where the user needs to be authenticated.
def get_authorization_headers():
    body = {'username': 'user', 'password': 'pass1234'}
    response = requests.post(LOGIN_ENDPOINT, data=body)
    access_token = response.json()['access_token']
    return {'Authorization': 'Bearer ' + access_token}


# Shared then

# Verifies that the response contains a specific status code
@then(parsers.parse('the response status code is "{code:d}"'))
def api_response_code(context, code):
    assert context['response'].status_code == code


# Verifies that the response body contains a JSON property.
@then(parsers.parse('the response contains the property "{property_name}"'))
def api_response_contains_property(context, property_name):
    response_json = context['response'].json()
    assert property_name in response_json
    assert response_json[property_name]


# Verifies each element of an array of objects contains a particular JSON property.
@then(parsers.parse('the response elements contains the property "{property_name}"'))
def api_response_contains_property(context, property_name):
    response_json = context['response'].json()
    for detection in response_json:
        assert detection[property_name]
import requests

from pytest_bdd import then, parsers

# Shared Constants

INTELLISITE_BASE_URL = 'http://localhost:8080'

LOGIN_ENDPOINT = INTELLISITE_BASE_URL + '/auth/token'

DETECTIONS_ENDPOINT = INTELLISITE_BASE_URL + '/detections'


def get_authorization_headers():
    body = {'username': 'user', 'password': 'pass1234'}
    response = requests.post(LOGIN_ENDPOINT, data=body)
    access_token = response.json()['access_token']
    return {'Authorization': 'Bearer ' + access_token}


# Shared then

@then(parsers.parse('the response status code is "{code:d}"'))
def api_response_code(context, code):
    assert context['response'].status_code == code


@then(parsers.parse('the response contains the property "{property_name}"'))
def api_response_contains_property(context, property_name):
    response_json = context['response'].json()
    assert property_name in response_json
    assert response_json[property_name]


@then(parsers.parse('the response elements contain the property "{property_name}"'))
def api_response_contains_property(context, property_name):
    response_json = context['response'].json()
    for detection in response_json:
        assert detection[property_name]
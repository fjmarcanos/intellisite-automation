import requests

from pytest_bdd import then, parsers

# Constants

INTELLISITE_BASE_URL = 'http://localhost:8080'

LOGIN_ENDPOINT = INTELLISITE_BASE_URL + '/auth/token'

DETECTIONS_ENDPOINT = INTELLISITE_BASE_URL + '/detections'


def get_authorization_headers():
    body = {'username': 'user', 'password': 'pass1234'}
    response = requests.post(LOGIN_ENDPOINT, data=body)
    access_token = response.json()['access_token']
    return {'Authorization': 'Bearer ' + access_token}


@then(parsers.parse('the response status code is "{code:d}"'))
def api_response_code(context, code):
    assert context['response'].status_code == code
import pytest
import requests

from .conftest import DETECTIONS_ENDPOINT, get_authorization_headers
from pytest_bdd import scenarios, given, when, then, parsers


scenarios('../features/detections.feature')


@pytest.fixture
def context():
    return {}


# Given Steps


@given(parsers.parse('I want to get a number of "{detections_number}" detections'))
def skip_detections(context, detections_number):
    context['detections_number'] = detections_number


# When Steps

@when('I send a GET request with the number of detections to limit')
def api_get_request_limit(context):
    params = {'limit': context['detections_number']}
    response = requests.get(DETECTIONS_ENDPOINT, params=params, headers=get_authorization_headers())
    context['response'] = response


@when('I send a GET request to detections')
def api_get_request(context):
    response = requests.get(DETECTIONS_ENDPOINT, headers=get_authorization_headers())
    context['response'] = response


# Then Steps


@then(parsers.parse('the number of detections is equal to "{detections_received:d}"'))
def api_response_detections(context, detections_received):
    response_json = context['response'].json()
    assert len(response_json) == detections_received

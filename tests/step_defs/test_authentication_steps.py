import pytest
import requests

from .conftest import INTELLISITE_BASE_URL
from pytest_bdd import scenarios, when, parsers

scenarios('../features/authentication.feature')


@pytest.fixture
def context():
    return {}


# When Steps


@when(parsers.parse('I send a "{http_verb}" request to the endpoint "{endpoint}"'))
def api_request(context, http_verb, endpoint):
    url = INTELLISITE_BASE_URL + endpoint
    if 'GET' == http_verb:
        context['response'] = requests.get(url)
    if 'POST' == http_verb:
        context['response'] = requests.post(url)
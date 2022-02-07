import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed
import json


@pytest.fixture
def home_response(client):
    return client.get(reverse("cryptocurrencyapi:api"))


class TestCryptoApiView:
    def test_reverse_resolve(self):
        assert reverse("cryptocurrencyapi:api") == "/crypto/api/"
        assert resolve("/crypto/api/").view_name == "cryptocurrencyapi:api"

    def test_status_code(self, home_response):
        assert home_response.status_code == 200

    def test_template(self, home_response):
        assertTemplateUsed(home_response, "list-crypto.html")

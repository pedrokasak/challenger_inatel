import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def home_response(client):
    return client.get(reverse("imports:import-and-read"))

class TestCryptoApiView:
    def test_reverse_resolve(self):
        assert reverse("imports:import-and-read") == "/"
        assert resolve("/").view_name == "imports:import-and-read"

    def test_status_code(self, home_response):
        assert home_response.status_code == 200

    def test_template(self, home_response):
        assertTemplateUsed(home_response, "import.html")
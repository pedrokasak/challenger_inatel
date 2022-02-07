import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed



@pytest.fixture
def home_response(client):
    return client.get(reverse("users:login"))


class TestUsersLoginView:
    def test_reverse_resolve(self):
        assert reverse("users:login") == "/"
        assert resolve("/").view_name == "users:login"

    def test_status_code(self, home_response):
        assert home_response.status_code == 200

    def test_template(self, home_response):
        assertTemplateUsed(home_response, "login.html")


      
class TestUsersLogoutView:
    def test_reverse_resolve(self):
        assert reverse("users:logout") == "/logout/"
        assert resolve("/logout/").view_name == "users:logout"

    def test_status_code(self, home_response):
        assert home_response.status_code == 200

    # def test_template(self, home_response):
    #     assertTemplateUsed(home_response, "logout.html")
    
    
   
class TestUsersSignUpView:
    def test_reverse_resolve(self):
        assert reverse("users:register") == "/register/"
        assert resolve("/register/").view_name == "users:register"

    def test_status_code(self, home_response):
        assert home_response.status_code == 200

    #def test_template(self, home_response):
        #assertTemplateUsed(home_response, "register.html")    
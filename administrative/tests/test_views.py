import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def home_response(client):
    return client.get(reverse("administrative:index"))

class TestAdministrativeView:
    def test_reverse_resolve(self):
        assert reverse("administrative:index") == "/dashboard/index/"
        assert resolve("/dashboard/index/").view_name == "administrative:index"

    def test_status_code(self, home_response):
        assert home_response.status_code == 200

    def test_template(self, home_response):
        assertTemplateUsed(home_response, "index.html")

# class TestModels(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.index = resolve('/')
        
#     def test_status_code(self):
        
#         response = self.client.get(self.index)
        
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'index.html')
       # self.assertContains(response, 'Challenger Inatel')
    
    
    #resp = client.get('/index')
    #assert resp.status_code == 200

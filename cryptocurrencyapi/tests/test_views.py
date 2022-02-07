from django.urls import resolve, reverse
from django.test import Client, TestCase
from ..views import index


class TestModels(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = resolve('/')
        
    def test_status_code(self):
        
        response = self.client.get(self.index)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Challenger Inatel')

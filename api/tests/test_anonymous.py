from django.test import TestCase

# Create your tests here.
from django.test import Client


class ApiTestCase1(TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_echo_anonymous(self):
        response = self.client.get('/api/v1/echo/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'hello, AnonymousUser', response.content)

    def tearDown(self):
        pass

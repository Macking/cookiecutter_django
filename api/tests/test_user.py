from django.test import TestCase

# Create your tests here.
from django.test import Client
from redpulse_rpx.users.models import User


class ApiTestCase1(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='john', email='john@test.com', password='johnpassword')
        self.client.login(username='john', password='johnpassword')

    def test_api_echo_anonymous(self):
        response = self.client.get('/api/v1/echo/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'hello, john', response.content)

    def tearDown(self):
        pass

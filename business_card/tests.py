from django.test import TestCase, Client

# Create your tests here.

class ClientTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_status_code(self):
        response = self.client.get('/example/')
        self.assertEqual(response.status_code, 200)

    def test_return_value(self):
        response = self.client.get('/example/')
        self.assertEqual(response.content, b'Hello man')



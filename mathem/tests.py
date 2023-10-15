from rest_framework.test import APIClient, APITestCase


class RegistrationTestCase(APITestCase):
    
    def setUp(self):
        self.client = APIClient()

    def test_succesful(self):
        data = {'string': '((A + B) * [C / D])/{W + K}'}
        response = self.client.post('/check/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': True})

    def test_unsuccesful(self):
        data = {'string': ')((A + B) * [C / D])/{W + K}'}
        response = self.client.post('/check/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': False})
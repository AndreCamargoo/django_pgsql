from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dataSuccess = {
            'name': 'André Camargo',
            'email': 'andre.camargo@msn.com',
            'subject': 'Subject',
            'message': 'Message'
        }

        self.dataError = {
            'name': 'André Camargo',
            'email': 'andre.camargo@msn.com'
        }

        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dataSuccess)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dataError)
        self.assertEqual(request.status_code, 200)

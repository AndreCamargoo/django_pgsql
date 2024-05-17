from django.test import TestCase
from core.forms import ContactForm


class ContactTestCase(TestCase):
    def setUp(self):
        self.name = 'André Camargo'
        self.email = 'andre.camargo@msn.com'
        self.subject = 'Subject'
        self.message = 'Message'

        self.dataForm = {
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message
        }

        # ContactForm(request.POST)
        self.form = ContactForm(data=self.dataForm)

    def test_send_mail(self):
        form1 = ContactForm(data=self.dataForm)
        form1.is_valid()
        response1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        response2 = form2.send_mail()

        self.assertEqual(response1, response2)

from django.test import TestCase, Client


class ViewTest(TestCase):

    def testView(self):
        """Тест главной станицы"""
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

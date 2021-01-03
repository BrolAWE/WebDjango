from django.test import TestCase


class HomePageTest(TestCase):
    """Тест домашней страницы"""

    def test_uses_home_template(self):
        """Используется шаблон домашней страницы"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

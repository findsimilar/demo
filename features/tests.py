from django.test import TestCase
from django.urls import reverse


class TestIndexView(TestCase):

    def setUp(self):
        self.url = '/'
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_for_simple(self):
        simple_url = reverse('features:simple')
        self.assertContains(self.response, f'href="{simple_url}"')


class TestFindSimilarSimpleView(TestCase):

    def setUp(self):
        self.url = '/simple/'
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_form_in_context(self):
        self.assertIn('form', self.response.context)

    def test_post(self):
        data = {
            'text': 'the same',
            'texts': 'the same,the other'
        }
        response = self.client.post(self.url, data=data)
        expected_url = '/simple/result/?text=the same&texts=the same=1.0,the other=0.5'
        self.assertRedirects(response, expected_url, 302)


class TestFindSimilarSimpleResultView(TestCase):

    def setUp(self):
        self.url = '/simple/result/?text=the same&texts=the same=1.0,the other=0.5'
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_content_and_context(self):
        text_list = ['the same', 'the other', '1.0', '0.5']
        for text in text_list:
            self.assertContains(self.response, text)




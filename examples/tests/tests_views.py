from copy import deepcopy

from rest_framework.test import APITestCase
from examples.models import Example


class TestExampleViewSet(APITestCase):
    def setUp(self):
        self.example_dict = {
            'text': 'one two',
            'texts': ['one', 'two']
        }
        self.example_name = 'some_name'
        self.example = Example.load_from_dict(self.example_name, self.example_dict)

    def test_status_code(self):
        response = self.client.get(f"/api/examples/{self.example_name}/")
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(f"/api/examples/{self.example_name}/")
        expected_dict = deepcopy(self.example_dict)
        expected_dict.update(
            {'name': 'some_name'}
        )
        self.assertEqual(response.json(), expected_dict)

    def test_list_response(self):
        response = self.client.get('/api/examples/')
        self.assertEqual(response.json(), [{'name': self.example_name}])

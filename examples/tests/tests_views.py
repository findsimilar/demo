from rest_framework.test import APITestCase
from examples.models import Example


class TestExampleViewSet(APITestCase):
    def setUp(self):
        self.example_dict = {
            'text': 'one two',
            'texts': ['one', 'two']
        }
        example_name = 'some_name'
        self.example = Example.load_from_dict(example_name, self.example_dict)
        self.response = self.client.get(f"/api/examples/{example_name}/")

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response(self):
        self.assertEqual(self.response.json(), self.example_dict)


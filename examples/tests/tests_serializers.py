from rest_framework.test import APITestCase
from examples.serializers import ExampleSerializer
from examples.models import Example


class TestExampleSerializer(APITestCase):
    def setUp(self):
        self.example_dict = {
            'text': 'one two',
            'texts': ['one', 'two']
        }
        self.example = Example.load_from_dict('some_name', self.example_dict)

    def test_serializer(self):
        serializer = ExampleSerializer(self.example)
        self.assertEqual(serializer.data, self.example_dict)

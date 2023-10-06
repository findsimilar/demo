from copy import deepcopy
from rest_framework.test import APITestCase
from examples.serializers import ExampleSerializer, ExampleNameSerializer
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
        expected_dict = deepcopy(self.example_dict)
        expected_dict.update(
            {'name': 'some_name'}
        )
        self.assertEqual(serializer.data, expected_dict)


class TestExampleNameSerializer(APITestCase):
    def setUp(self):
        self.example_dict = {
            'text': 'one two',
            'texts': ['one', 'two']
        }
        self.example_name = 'some_name'
        self.example = Example.load_from_dict('some_name', self.example_dict)

    def test_serializer(self):
        serializer = ExampleNameSerializer(self.example)
        self.assertEqual(serializer.data, {'name': self.example_name})

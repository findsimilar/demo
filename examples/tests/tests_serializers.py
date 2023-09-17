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
        self.assertEqual(serializer.data, self.example_dict)


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

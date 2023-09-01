from rest_framework.test import APISimpleTestCase
from features.serializers import FindSimilarSerializer, TokenTextSerializer
from find_similar import TokenText


class TestFindSimilarSerializer(APISimpleTestCase):

    def setUp(self):
        self.valid_data = {
            'text_to_check': 'one two',
            'texts': ['one', 'two', 'one two'],
            'language': 'russian',
            'count': 10,
            # 'dictionary': {'some': 'analog'} # https://github.com/findsimilar/find-similar/issues/7
        }

    def test_create(self):
        serializer = FindSimilarSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        result = serializer.save()
        self.assertEqual(len(result), 3)
        one, two, three = result
        self.assertEqual(one.cos, 1.0)
        self.assertTrue(two.cos < 1)

    def test_valid_serializer(self):
        serializer = FindSimilarSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        invalid_data_list = [
                {},
                {
                    'text_to_check': 'one two',
                    'texts': 'one two',
                },
                {
                    'text_to_check': 'one two',
                    'texts': ['one two'],
                    'count': 'abc',
                }
            ]
        for invalid_data in invalid_data_list:
            serializer = FindSimilarSerializer(data=invalid_data)
            self.assertFalse(serializer.is_valid())


class TestTextTokenSerializer(APISimpleTestCase):

    def test_serialize(self):
        token_text = TokenText(text='one two')
        serializer = TokenTextSerializer(token_text)
        self.assertEqual(serializer.data, {'text': 'one two', 'cos': None})
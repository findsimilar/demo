from rest_framework.test import APISimpleTestCase
from rest_framework.serializers import ValidationError
from find_similar import TokenText
from features.serializers import FindSimilarSerializer, TokenTextSerializer


class TestFindSimilarSerializer(APISimpleTestCase):
    def setUp(self):
        self.valid_data = {
            "text_to_check": "one two",
            "texts": ["one", "two", "one two"],
            "language": "russian",
            "count": 10,
            # 'dictionary': {'some': 'analog'} https://github.com/findsimilar/find-similar/issues/7
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
            {},  # empty
            {
                "text_to_check": "one two",
                "texts": "one two",  # not list
            },
            {
                "text_to_check": "one two",
                "texts": ["one two"],
                "count": "abc",  # not int
            },
        ]
        for invalid_data in invalid_data_list:
            serializer = FindSimilarSerializer(data=invalid_data)
            with self.subTest(msg=str(invalid_data)):
                self.assertFalse(serializer.is_valid())

    def test_invalid_language(self):
        valid_data = {
            "text_to_check": "one two",
            "texts": ["one", "two", "one two"],
            "language": "unexpected language",
            "count": 10,
        }

        serializer = FindSimilarSerializer(data=valid_data)
        serializer.is_valid(raise_exception=True)

        with self.assertRaises(ValidationError):
            serializer.save()


class TestTextTokenSerializer(APISimpleTestCase):
    def test_serialize(self):
        token_text = TokenText(text="one two")
        serializer = TokenTextSerializer(token_text)
        self.assertEqual(serializer.data, {"text": "one two", "cos": None})

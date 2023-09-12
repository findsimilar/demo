from django.test import TestCase, SimpleTestCase
from examples.models import Text, Example
from find_similar.examples import get_example, examples_set


class TestText(SimpleTestCase):

    def test_str(self):
        some_text = 'one two'
        text = Text(text=some_text)
        assert str(text) == some_text


class TestExample(TestCase):

    def test_load_from_dict(self):
        some_text = 'one two'
        some_text_list = ['one', 'two']
        example = Example.load_from_dict(
            'some_name',
            {
                'text': some_text,
                'texts': some_text_list
             }
        )
        self.assertEqual(example.text.text, some_text)
        for some_item_text in some_text_list:
            with self.subTest(msg=some_item_text):
                self.assertTrue(example.texts.filter(text=some_item_text).exists())
        self.assertEqual(example.texts.count(), len(some_text_list))

    def test_load_from_find_similar(self):
        lib_examples = examples_set()
        examples = Example.load_from_find_similar()
        self.assertEqual(examples.count(), len(lib_examples))
        self.assertTrue(examples.filter(name='mock').exists())
        # load again to test delete
        examples = Example.load_from_find_similar()
        self.assertEqual(examples.count(), len(lib_examples))
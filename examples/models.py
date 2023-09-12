from django.db import models
from find_similar.examples import examples_set, get_example


class Text(models.Model):
    text = models.CharField(max_length=1024, unique=True)

    def __str__(self):
        return self.text


class Example(models.Model):
    name = models.CharField(max_length=32, unique=True)
    text = models.ForeignKey(Text, on_delete=models.CASCADE, related_name='text_examples')
    texts = models.ManyToManyField(Text)

    @classmethod
    def load_from_dict(cls, name, example_dict):
        text = example_dict['text']
        text_obj, _ = Text.objects.get_or_create(text=text)
        example = cls.objects.create(name=name, text=text_obj)
        texts = example_dict['texts']
        for text in texts:
            text_obj, _ = Text.objects.get_or_create(text=text)
            example.texts.add(text_obj)
        example.save()
        return example

    @classmethod
    def load_from_find_similar(cls):
        cls.objects.all().delete()
        lib_examples = examples_set()
        for lib_example in lib_examples:
            example_dict = get_example(lib_example)
            cls.load_from_dict(lib_example, example_dict)
        return Example.objects.all()

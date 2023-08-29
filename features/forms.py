from django import forms
from django.conf import settings

DEFAULT_SEPARATOR = ','
TEXT_FILM_EXAMPLE = 'Люди и глаза'
TEXTS_FILM_EXAMPLE = [
    'Титаник',
    'Матрица',
    'Форрест Гамп',
    'Терминатор 2',
    'Гаттака',
    'С широко закрытыми глазами',
    'Основной инстинкт',
    'Молчание ягнят',
    'Зеленая миля',
    'Достучаться до небес',
    'Пятый элемент',
    'Побег из Шоушенка',
    'Телохранитель',
    'Люди в черном',
    'Бойцовский клуб',
    'Один дома',
    'Бетховен',
    'Криминальное чтиво',
    'Умница Уилл Хантинг',
    'Маска',
    'Знакомьтесь, Джо Блэк',
    'День сурка',
    'Большой Лебовски',
    'Леон',
    'Американский пирог',
    'Шоу Трумана',
    'Красотка',
    'Адвокат дьявола',
]

class FindSimilarSimpleForm(forms.Form):

    text = forms.CharField(
        max_length=settings.MAX_TEXT_LENGTH,
        label=f'Input text to search',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                f'placeholder': f'For example: {TEXT_FILM_EXAMPLE}'
            }
        )
    )

    new_separator = f'{DEFAULT_SEPARATOR}\n'

    texts = forms.CharField(
        max_length=settings.TEXT_LIST_LENGTH_LENGTH,
        label=f'Input texts to find similars through the separator (default ,)',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                f'placeholder': f'For example: {DEFAULT_SEPARATOR.join(TEXTS_FILM_EXAMPLE)}'
            }
        )
    )
    separator = forms.CharField(
        max_length=3,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': f'Separator. Default {DEFAULT_SEPARATOR}'
            }
        ),
        initial=DEFAULT_SEPARATOR,
    )
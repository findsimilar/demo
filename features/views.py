from django.views.generic import TemplateView, FormView
from .forms import FindSimilarSimpleForm, TEXTS_FILM_EXAMPLE, TEXT_FILM_EXAMPLE, DEFAULT_SEPARATOR
from find_similar import find_similar


class IndexView(TemplateView):
    template_name = 'features/index.html'


class FindSimilarSimpleView(FormView):
    template_name = 'features/simple.html'
    form_class = FindSimilarSimpleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example_text'] = TEXT_FILM_EXAMPLE
        context['example_texts'] = DEFAULT_SEPARATOR.join(TEXTS_FILM_EXAMPLE)
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        self.separator = data.get('separator')
        text = data.get('text')
        self.text = text
        texts = data.get('texts')
        text_list = texts.split(self.separator)
        self.result = find_similar(self.text, text_list, count=100)
        return super().form_valid(form)

    def get_success_url(self):
        redirect_url = '/simple/result/'
        redirect_url = f'{redirect_url}?text={self.text}'
        pairs = []
        for item in self.result:
            pair = f'{item.text}={item.cos}'
            pairs.append(pair)
        pairs_text = ','.join(pairs)
        redirect_url = f'{redirect_url}&texts={pairs_text}'
        return redirect_url


class FindSimilarSimpleResultView(TemplateView):
    template_name = 'features/simple_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_params = self.request.GET
        text = url_params.get('text')
        context['text'] = text
        texts = url_params.get('texts')
        pair_list = texts.split(',')
        texts = []
        for pair in pair_list:
            result_text, cos = pair.split('=')
            texts.append({'text': result_text, 'cos': cos})
        context['texts'] = texts
        return context

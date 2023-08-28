from django.views.generic import TemplateView, FormView
from .forms import FindSimilarSimpleForm
from find_similar import find_similar


class IndexView(TemplateView):
    template_name = 'features/index.html'


class FindSimilarSimpleView(FormView):
    template_name = 'features/simple.html'
    form_class = FindSimilarSimpleForm

    def form_valid(self, form):
        data = form.cleaned_data
        text = data.get('text')
        self.text = text
        texts = data.get('texts')
        text_list = texts.split(',')
        self.result = find_similar(self.text, text_list)
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

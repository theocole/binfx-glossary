from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from words.models import Word
from words.forms import AddWordForm

# Create your views here.
class IndexView(View):
    def get(self, request):
        form = AddWordForm()
        context = {'add_word_form': form}
        success = True

        return render(request, 'words/index.html', context)

    def post(self, request):
        success = False
        form = AddWordForm(request.POST)
        print(form.cleaned_data)
        if form.is_valid():
            success = True
        print(success)

        blank_form = AddWordForm()
        context = {'add_word_form': blank_form}

        return render(request, 'words/index.html', context)

class WordsView(View):
    def get(self, request):

        words = Word.objects.all()
        word_list = []
        for word in words:
            word_list.append(
                {
                    'category': str(word.category),
                    'title': word.word,
                    'definition': word.definition
                }
            )

        results = {"results": word_list}
        return JsonResponse(results)

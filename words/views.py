from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from words.models import Word

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'words/index.html')

class WordsView(View):
    def get(self, request):
        words = Word.objects.all()
        word_list = []
        for word in words:
            word_list.append(
                {
                    'category': str(word.category),
                    'title': word.word,
                }
            )

        results = {"results": word_list}
        return JsonResponse(results)

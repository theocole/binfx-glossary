from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from words.forms import AddWordForm
from words.forms import AddCategoryForm
from words.models import Category
from words.models import Word

# Create your views here.
class IndexView(View):
    def get(self, request):
        context = {}
        add_word_form = AddWordForm()
        context['add_word_form'] = add_word_form
        success = True

        add_category_form = AddCategoryForm()
        context['add_category_form'] = add_category_form

        return render(request, 'words/index.html', context)

    def post(self, request):
        context = {}
        success = False
        word_form = AddWordForm(request.POST)
        category_form = AddCategoryForm(request.POST)

        if word_form.is_valid():
            success = True
            word_form.save()

        if category_form.is_valid():
            success = True
            category_form.save()

        add_word_form = AddWordForm()
        context['add_word_form'] = add_word_form

        add_category_form = AddCategoryForm()
        context['add_category_form'] = add_category_form

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

class CategoriesView(View):
    def get(self, request):
        context = {}

        add_word_form = AddWordForm()
        context['add_word_form'] = add_word_form

        add_category_form = AddCategoryForm()
        context['add_category_form'] = add_category_form

        categories = Category.objects.all()
        words_by_category = {
            category: Word.objects.filter(category=category)
            for category in categories
        }
        context['words_by_category'] = words_by_category
        return render(request, 'words/categories.html', context)

from django.urls import path

from words.views import IndexView
from words.views import CategoriesView
from words.views import WordsView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('words', WordsView.as_view(), name='words'),
    path('categories', CategoriesView.as_view(), name='categories'),
]

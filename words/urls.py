from django.urls import path

from words.views import IndexView
from words.views import WordsView


urlpatterns = [
    path('', IndexView.as_view()),
    path('words', WordsView.as_view()),
]

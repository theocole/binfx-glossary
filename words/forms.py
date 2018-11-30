from django.forms import ModelForm
from words.models import Category
from words.models import Word

class AddWordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'category', 'definition']

class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

from django.forms import ModelForm
from words.models import Word

class AddWordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'category', 'definition']

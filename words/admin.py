from django.contrib import admin

# Register your models here.
from words.models import Word, Category

admin.site.register(Word)
admin.site.register(Category)

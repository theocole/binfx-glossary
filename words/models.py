from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

class Word(models.Model):
    word = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    definition = models.TextField()

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (word, category)

    def __str__(self):
        return str(self.word)

    def __repr__(self):
        return str(self.word)



from django.db import models

# Create your models here.
class BooksModel(models.Model):
    bookname = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.FloatField()
    
    def __str__(self):
        return self.bookname
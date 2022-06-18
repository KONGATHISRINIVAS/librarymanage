from django.db import models
# Create your models here.
from django.db import models
#from django.contrib.auth.models import use
from datetime import datetime,timedelta
from django.urls import reverse
from django.db.models.signals import post_save
# Create your models here.
class Genre(models.Model):
    name=models.CharField(max_length=200,help_text="enter a book genre(e.g science fiction,french poetry etc.)")

    def __str__(self):
        return self.name
class Language(models.Model):
    name=models.CharField(max_length=200,help_text="enter the book natural languge (e.g English,french,japanese ect.)")

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=200)
    authour=models.CharField(max_length=200)
    summary=models.TextField(max_length=1000,help_text="Enter a brief description of the book")
    isbn=models.CharField('ISBN',max_length=13,
                           help_text='13 character <a herf="http:isbn-international.org/content/what-isbn">ISBN number</a>')
    genre=models.ManyToManyField(Genre,help_text="Select a genre for this book")
    languaage=models.ForeignKey('Language',on_delete=models.SET_NULL,null=True)
    total_copies=models.IntegerField()
    Available_copies=models.IntegerField()
    Pic=models.ImageField(blank=True,null=True,upload_to='book_image')

    def get_absolute_url(self):
        return reverse('book-detail',args=[str(self.id)])
    def __str__(self):
        return self.title
def create_user(sender,*args,**kwargs):
    if kwargs['created']:
        user=user.object.create(username=kwargs['instance'],password="dummypass")

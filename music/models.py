from django.db import models

class Post(models.Model):
   author = models.CharField(max_length=250)
   age = models.CharField(max_length=10)
   gender = models.CharField(max_length=500)
   Born_in = models.CharField(max_length=250)
   abt_author = models.CharField(max_length=1000)

   def __str__(self):
   	 return self.author

class Book(models.Model):
   author = models.ForeignKey(Post,on_delete=models.CASCADE)
   Book_name = models.CharField(max_length=10)
   isbn = models.CharField(max_length=20)
   desp = models.CharField(max_length=100)

   def __str__(self):
   	 return self.Book_name
from django.db import models

# Create your models here.
class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    def __str__(self):
        return self.full_name

class Friend(models.Model):
    full_name = models.TextField()
    def __str__(self):
       return self.full_name    

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()
    copy_count = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish = models.ForeignKey('Publish', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    friend = models.ForeignKey('Friend', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.title

class Publish(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name


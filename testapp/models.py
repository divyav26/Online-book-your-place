from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    description = models.TextField(max_length=100)

class State(models.Model):
    title=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural='State'

    def __str__(self):
        return self.title

# News Model
class Place(models.Model):
    category=models.ForeignKey(State,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='imgs/')
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural='Place'

    def __str__(self):
        return self.title

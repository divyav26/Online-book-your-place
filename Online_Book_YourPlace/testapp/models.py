from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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


class Customer(models.Model):
    customer = models.CharField(max_length=100)
    customer_email = models.EmailField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    date = models.DateField()
    message = models.TextField(default= "this is a default message.")
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return str(self.customer)

    def get_status(self):
        return self.status

    # def save(self, *args, **kwargs):
        # if not self.id:
        #     self.due_date = datetime.datetime.now()+ datetime.timedelta(days=15)
        # return super(Invoice, self).save(*args, **kwargs)

class LineItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    age =  models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.customer)




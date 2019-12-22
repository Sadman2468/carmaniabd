from django.db import models
from users.models import User_profile
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=50,blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField()

    def __str__(self):

        return self.name

class Giverent_field(models.Model):

    car_name = models.CharField(max_length=50)
    car_type = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/images')
    seat_capacity = models.IntegerField()
    contact_number = models.IntegerField()
    location = models.CharField(max_length=250)

class car_choose(models.Model):
    car_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    client = models.CharField(max_length=20)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='media/car_profile')

class sell_car_post(models.Model):

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    car_name = models.CharField(max_length=100)
    engine_capacity = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    seat_capacity = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    image = models.ImageField(default='default.jpg',upload_to='pictures/')

    def get_absolute_url(self):
        return reverse('blog:buycar')
class User_rent_form(models.Model):

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    rent_date = models.DateField()
    duration = models.CharField(max_length=50)
    upload_lic = models.ImageField(upload_to='media/license')

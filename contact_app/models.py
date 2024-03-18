from django.db import models
from django.forms import ModelForm

# Create your models here.

class user(models.Model):
     name = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     password = models.CharField(max_length=100)

class UserForm(ModelForm):
     class Meta:
          model = user
          fields = ["name","email","password"]

class contacts(models.Model):
     name = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     password = models.CharField(max_length=100)
     contact = models.BigIntegerField()
     user_id = models.IntegerField(default=1,blank=True,null=True)

class ContactForm(ModelForm):
     class Meta:
          model = contacts
          fields = ["name","email","password","contact","user_id"]



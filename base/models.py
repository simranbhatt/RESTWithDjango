from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    premium = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


""" after making changes in this file, to persist: """
#python manage.py makemigrations
#python manage.py migrate
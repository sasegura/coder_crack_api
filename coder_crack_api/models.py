from django.db import models


# Create your models here.
class EmailSubscription(models.Model):
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['email']


class UserMessage(models.Model):
    name = models.CharField(max_length=256)
    lastname = models.CharField(max_length=512)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    message = models.TextField()

    class Meta:
        ordering = ['name', 'lastname']

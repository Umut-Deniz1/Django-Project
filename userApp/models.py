from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    tcIdentity = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)

    def __str__(self):
        return self.name


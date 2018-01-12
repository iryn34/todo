from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=50)

    def __str__(self):
        return self.name

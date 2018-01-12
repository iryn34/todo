from django.db import models
from contacts.models import Contact


class List(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from django.db import models
from lists.models import Contact, List


class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    assignee_id = models.IntegerField() 
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.title

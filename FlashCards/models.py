from django.db import models
from django.contrib.auth.models import User


class Cards(models.Model):
    subject = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

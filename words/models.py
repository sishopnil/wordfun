from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class  Word(models.Model):
    word = models.CharField(max_length=225)
    meaning = models.TextField()
    usedinsen = models.TextField()
    maker = models.hunter = models.ForeignKey(User, on_delete=models.CASCADE)

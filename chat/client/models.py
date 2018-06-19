from django.db import models

class Message(models.Model):
    text = models.CharField(max_length=1000)
    sender = models.CharField(max_length=32)
    receiver = models.CharField(max_length=32)
    is_read = models.IntegetField(default=0)
    date = models.DateTimeField('date wrote')

class Client(models.Model):
    nickname = models.CharField(max_length=32)


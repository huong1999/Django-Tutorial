from django.db import models

# Create your models here.
class Question(models.Model):
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "%s"%self.votes
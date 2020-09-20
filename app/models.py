from django.db import models

# Create your models here.
class QuizSource(models.Model):
    """ Default user model """
    quiz = models.CharField(max_length=100, default='')
    degree = models.IntegerField(default='0')

    def __str__(self):
        return f"{self.quiz}"

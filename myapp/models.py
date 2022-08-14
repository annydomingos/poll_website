from pyexpat import model
from secrets import choice
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
class Question(models.Model):
  question_text = models.CharField('Question', max_length=200)
  pub_date = models.DateTimeField('Published')

  def __str__(self):
    return self.question_text

  def was_published_recently(self):
    #function to know if the question was publish in less than a day
    return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField('Choice', max_length=150)
  votes = models.IntegerField('Votes', default=0)

  def __str__(self) -> str:
    return f' {self.choice_text}'

# q2 = Question(question_text='Você gosta de python? ', pub_date=timezone.now())
# print(q2.was_published_recently())


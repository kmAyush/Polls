import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse

class Question(models.Model):
    question_text= models.CharField(max_length=500)
    pub_date= models.DateTimeField('date published',null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True
    was_published_recently.short_description='Published recently?'    

    def get_absolute_url(self):
        return reverse('polls:detail', kwargs={'pk':self.pk})

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

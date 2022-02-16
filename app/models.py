from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name
    
class ExerciseQuestions(models.Model):
    head = models.CharField(max_length=50, default='')
    topic_tag = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.head

class Questions(models.Model):
    heading = models.ForeignKey(ExerciseQuestions, on_delete=models.CASCADE)
    text = models.TextField(max_length=10000, default='')


class Blog(models.Model):
    title = models.CharField(max_length=100,  default='')
    img = models.URLField(max_length=300,  default='')
    text = models.TextField(blank=True)
    date_publish = models.DateTimeField()
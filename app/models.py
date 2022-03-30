from django.db import models
from django.db.models.signals import pre_save
from blog.utils import unique_slug_generator

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
    
# class ExerciseQuestions(models.Model):
#     head = models.CharField(max_length=50, default='')
#     topic_tag = models.CharField(max_length=100, default='')

#     def __str__(self):
#         return self.head

class Questions(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    topic_tag = models.ManyToManyField(Topic)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    text = models.TextField(max_length=10000, default='')

    def __str__(self):
        return self.title

    def topics(self):
        return ", ".join([str(p) for p in self.topic_tag.all()])

    def slug_generator(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)


class Blog(models.Model):
    title = models.CharField(max_length=100,  default='', null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    img = models.URLField(max_length=300,  default='')
    text = models.TextField(blank=True)
    date_publish = models.DateTimeField()

    def __str__(self):
        return self.title

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Blog)
pre_save.connect(slug_generator, sender=Questions)
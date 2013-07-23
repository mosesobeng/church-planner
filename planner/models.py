from django.db import models
from django.contrib import admin


class Calendar(models.Model):
    id = models.CharField(primary_key=True,max_length=10)


class Church(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=200)
    calendar = models.ForeignKey(Calendar)
    def __unicode__(self):
        return self.name



class Task(models.Model):
    time = models.TimeField()
    day = models.DateField()
    calendar = models.ForeignKey(Calendar)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=600)
    def __unicode__(self):
        return self.title

class Member(models.Model):
    username = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=10)
    church = models.ForeignKey(Church , related_name='church')
    def __unicode__(self):
        return self.name




admin.site.register(Church)
admin.site.register(Member)
admin.site.register(Calendar)
admin.site.register(Task)


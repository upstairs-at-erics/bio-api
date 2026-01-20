from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    name        = models.CharField(max_length=100)
    title       = models.CharField(max_length=200)
    location    = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return f"{self.name} - {self.title} "

class Expertise(models.Model):
    label = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.label} "
    class Meta:
        verbose_name_plural = "Expertise"


class Project(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return f"{self.title} "

class Skill(models.Model):
    label = models.CharField(max_length=100)
    value = models.IntegerField()  
    def __str__(self):
        return f"{self.label} - {self.value}% "

class Focus(models.Model):
    item       = models.CharField(max_length=200)
    enabled    = models.BooleanField(default=True)          
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)       

    def __str__(self):
        return f"{self.item} ({'enabled' if self.enabled else 'disabled'})"
    class Meta:
        verbose_name_plural = "Focus"



class Career(models.Model):
    period      = models.CharField(max_length=50)
    role        = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.period}  {self.role}"


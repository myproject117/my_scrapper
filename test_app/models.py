from django.db import models

# Create your models here.

class LatestData(models.Model):
    image = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200)
    url = models.TextField()

    def __str__(self):
        return self.title
class LatestExten(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField()

    def __str__(self):
        return self.title



class SportData(models.Model):
    image = models.URLField(null=True, blank=True)
    title=models.CharField(max_length=200)
    url=models.TextField()

    def __str__(self):
        return self.title

class SportExten(models.Model):
    title=models.CharField(max_length=100)
    url=models.TextField()

    def __str__(self):
        return self.title



class EntertainData(models.Model):
    image = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200)
    url = models.TextField()

    def __str__(self):
        return self.title

class EntertainExten(models.Model):
    title=models.CharField(max_length=100)
    url=models.TextField()

    def __str__(self):
        return self.title



class Polity(models.Model):
    image = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200)
    url = models.TextField()

    def __str__(self):
        return self.title

class PolityExten(models.Model):
    title=models.CharField(max_length=100)
    url=models.TextField()

    def __str__(self):
        return self.title




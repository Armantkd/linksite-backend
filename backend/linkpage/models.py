from django.db import models

class Creator(models.Model):
    name = models.CharField(max_length=255)
    views = models.IntegerField()
    replies = models.IntegerField()
    blink = models.SlugField(max_length=255)
    class Meta:
        ordering = ['-views']
        db_table = "creator"


class Rentry(models.Model):
    creator = models.ForeignKey('Creator', on_delete = models.CASCADE)
    link = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = "rentry"
    
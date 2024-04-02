from django.db import models

# Create your models here.

class Table(models.Model):
    word = models.CharField(max_length=30)
    tf = models.FloatField()
    idf = models.FloatField()
    count = models.IntegerField()

    def __str__(self):
        return self.word
    
    class Meta:
        ordering = ['-tf']
from django.db import models
from datetime import datetime

Movie_Choice = (
    ('Kabir_Singh','Kabir_Singh'),
    ('Bharat', 'Bharat'),
    ('Avengers','Avengers')
)

class Mood(models.Model):
    movie = models.CharField(max_length=100, choices= Movie_Choice, default='Select')
    name1 = models.CharField(max_length=20)
    name2 = models.CharField(max_length=100)
    name3 = models.CharField(max_length=100)
    name4 = models.CharField(max_length=100)
    name5 = models.CharField(max_length=100)
    result = models.IntegerField()
    star = models.IntegerField()
    opinion = models.CharField(max_length=100)

    class Meta:  
        db_table = "mood"
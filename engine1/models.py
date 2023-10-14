from django.db import models
from datetime import date

class CCB(models.Model):
    filing_date:date = models.DateField()
    crime_date:date = models.DateField()
    state:str = models.CharField(max_length=25)
    district:str = models.CharField(max_length=25)
    respondent:list = models.CharField(max_length=150)
    category:str = models.CharField(max_length=25)
    sub_category:str = models.CharField(max_length=25)
    police_station:str = models.CharField(max_length=25)
    fir_number:str = models.CharField(max_length=25)
    year:date.year = models.IntegerField()
    court_type = models.CharField(max_length=20)

class petitioner(models.Model):
    name:str = models.CharField(max_length=25)
    fir_number:int = models.ForeignKey(CCB, on_delete=models.CASCADE)

class respondent(models.Model):
    name:str = models.CharField(max_length=25)
    fir_number:int = models.ForeignKey(CCB, on_delete=models.CASCADE)

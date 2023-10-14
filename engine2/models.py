from django.db import models
from engine1.models import CCB
from judgehandle.models import Judges
from lawyerhandle.models import Laywers

class Assigened(models.Model):
    pre_id = models.AutoField(primary_key=True)
    ccb = models.OneToOneField(CCB, on_delete=models.CASCADE)  # Changed field name to 'ccb'
    priority = models.IntegerField()
    judge = models.ForeignKey(Judges, on_delete=models.CASCADE)  # Changed field name to 'judge'
    lawyer = models.ForeignKey(Laywers, on_delete=models.CASCADE)  # Changed field name to 'lawyer'
    
    def __str__(self) -> str:
        return f"{self.ccb}"   

class Priority(models.Model):
    fir_id = models.AutoField(primary_key=True)
    fir_number = models.CharField(max_length=20)
    case_type = models.CharField(max_length=75)
    priority = models.IntegerField()
    sub_priority = models.FloatField()
    emergency_tag = models.FloatField()
    
    def __str__(self) -> str:
        return f"{self.fir_number}"

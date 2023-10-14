from django.db import models
from engine1.models import CCB
from judgehandle.models import Judges
from lawyerhandle.models import Laywers

class Assigened(models.Model):
    pre_id = models.AutoField(primary_key=True)
    ccb_id = models.OneToOneField(CCB, on_delete=models.CASCADE)
    ccb_id = models.CharField(max_length=150)
    priority = models.IntegerField()
    judge_id = models.ForeignKey(Judges, on_delete=models.CASCADE)
    lawyer_id = models.ForeignKey(Laywers, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.ccb_id}"   






class Priority(models.Model):
    fir_id = models.AutoField(primary_key=True)
    fir_number = models.CharField(max_length=20)
    case_type = models.CharField(max_length=75)
    priority = models.IntegerField()
    sub_priority = models.FloatField()
    emergency_tag = models.FloatField()
    
    def __str__(self) -> str:
        return f"{self.fir_number}"


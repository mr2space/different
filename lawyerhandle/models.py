from django.db import models
from judgehandle.models import JudgeAppoinments, Judges
class Laywers(models.Model):
    laywer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField()
    date_of_birth = models.DateField()
    bio = models.TextField()
    specialization_area = models.CharField(max_length=24)

class LawyerHearing(models.Model):
    Laywer_id = models.ForeignKey(Laywers, on_delete=models.CASCADE)
    appoinments_id = models.OneToOneField(JudgeAppoinments, on_delete=models.CASCADE)
    judge_id = models.OneToOneField(Judges, on_delete=models.CASCADE)
    schedule = models.DateTimeField(null=False)
    end_schedule = models.DateTimeField(null=False)




from django.db import models
from django.contrib.auth.models import User


class Judges(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    judge_id = models.AutoField(primary_key=True) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField()
    date_of_birth = models.DateField()
    bio = models.TextField()

    # Judge's professional information
    case_count = models.IntegerField()
    case_count_priority = models.IntegerField()
    court_name = models.CharField(max_length=100)
    court_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Appoinments(models.Model):
    appoinments_id = models.AutoField(primary_key=True)
    cnr_number = models.CharField(max_length=150,unique=True)


class Hearing(models.Model):
    appoinments_id = models.OneToOneField(Appoinments, on_delete=models.CASCADE)
    judge_id = models.OneToOneField(Judges, on_delete=models.CASCADE)
    schedule = models.DateTimeField(null=False)
    end_schedule = models.DateTimeField(null=False)


class JudgeCalander(models.Model):
    appoinmets_id = models.OneToOneField(Appoinments, on_delete=models.CASCADE)
    hearing_id = models.OneToOneField(Hearing, on_delete=models.CASCADE)

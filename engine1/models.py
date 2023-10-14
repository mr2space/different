from django.db import models

STATE_CHOICES = (
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CG', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TS', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),
    )


class CCB(models.Model):
    filing_date = models.DateField()
    crime_date = models.DateField()
    state = models.CharField(max_length=25)
    district = models.CharField(max_length=25)
    respondent = models.CharField(max_length=150)  # Change from list to CharField
    category = models.CharField(max_length=25)
    sub_category = models.CharField(max_length=25)
    police_station = models.CharField(max_length=25)
    fir_number = models.CharField(max_length=25)  # Changed from int to CharField
    year = models.IntegerField()
    court_type = models.CharField(max_length=20)

class Petitioners(models.Model):  # Capitalized the class name
    name = models.CharField(max_length=25)
    fir_number = models.ForeignKey(CCB, on_delete=models.CASCADE)

class Respondents(models.Model):  # Capitalized the class name
    name = models.CharField(max_length=25)
    fir_number = models.ForeignKey(CCB, on_delete=models.CASCADE)

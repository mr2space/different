from django.shortcuts import render
from .models import Judges
from django.db.models import Min

def returnAvailableJudge(court_type:str):
    judge = Judges.objects.filter(court_type=court_type).order_by("case_count_priority").first()
    return judge


def assignCase(ccb_id, priority, scheduled, end_scheduling, **kwargs):
    # update the assignements
    # increase the judge value
    # update hearing
    ...
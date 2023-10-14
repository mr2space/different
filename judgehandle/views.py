from django.shortcuts import render
from .models import Judges, JudgeAppoinments
from django.db.models import Min
from engine1.models import CCB

def returnAvailableJudge(court_type:str):
    judge = Judges.objects.filter(court_type=str(court_type).lower()).order_by("case_count_priority").first()
    return judge


def assignCase(ccb_id, priority, judge:Judges):
    # update the assignements
    # increase the judge value
    try:
        judge = Judges.objects.filter(judge).update(case_count = judge.case_count + 1, case_count_priority = judge.case_count_priority + priority)
    except Exception as e:
        print(f'Error in update {e}')
    try:
        appoin = JudgeAppoinments(
            cnr_number = CCB.objects.get(ccb_id)
        )
    except Exception as e:
        print(f"Error in new {e}")
    appoin.save()
    return appoin
    
    ...
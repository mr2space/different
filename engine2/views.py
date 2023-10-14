from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Assigened, Priority
from judgehandle.views import returnAvailableJudge
from engine1.models import CCB
from django.core import serializers


def getTotalPriority(fir_list:list[str]):
    try:
        firs = fir_list
        total_priority = 0

        for fir in firs:
            priority_data = Priority.objects.filter(fir_number=fir).first()
            if priority_data:
                total_priority += priority_data.priority
                total_priority += priority_data.sub_priority
                total_priority += priority_data.emergency_tag

        return total_priority
    except Exception as e:
        # Handle the exception as needed, e.g., log it or return a default value
        return 0  # Return 0 as a default value

@csrf_exempt
def receiver(ccb_id:int, court_type:str, lawyer_id:int, fir_list:list, temp_json ):
    try:

        # Get the available judge
        judge_id = returnAvailableJudge(court_type)

        # Calculate the priority
        priority = getTotalPriority(fir_list)
        ccb = CCB.objects.get(id=ccb_id)
        # Create a PostAssigened object
        post_assigned = Assigened(
            ccb_id=ccb,
            judge_id=judge_id,
            lawyer_id=lawyer_id,
            priority=priority
        )
        post_assigned.save()

        # Serialize the object to JSON
        result = serializers.serialize('json', [post_assigned])
        temp_json = result

        return JsonResponse(result, safe=False)
    except Exception as e:
        # Handle the exception as needed, e.g., log it or return an error response
        return JsonResponse({'error': 'An error occurred'}, status=500)
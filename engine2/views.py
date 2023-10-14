from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Assigened, Priority
from lawyerhandle.models import Laywers
from judgehandle.models import Judges
from judgehandle.views import returnAvailableJudge
from engine1.models import CCB
from django.core import serializers
import ast


def getTotalPriority(fir_list:list[str]):
    try:
        firs = [fir_list]
        output_list = ast.literal_eval(firs[0])
        print(output_list,"hello")
        # If needed, you can further clean the list to remove the extra quotes
        if len(output_list) == 1:
            output_list = ast.literal_eval(output_list[0])

        firs = output_list
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
def receiver(request, ccb_id: int, court_type: str, lawyer_id: int, fir_list: list, temp_json):
    try:
        # Get the available judge
        judge_id = returnAvailableJudge(court_type)

        # Calculate the priority
        priority = getTotalPriority(fir_list)
        ccb = CCB.objects.get(ccb_id)
        print(lawyer_id , judge_id)
        # Get the lawyer and judge objects by their IDs

        # Create an Assigened object
        post_assigned = Assigened.objects.create(
            ccb_id=ccb,
            judge_id=judge_id,  # Use '_id' to assign by ID directly
            lawyer_id=lawyer_id,  # Use '_id' to assign by ID directly
            priority=priority
        )

        # Return a JSON response with the object details
        result = {
            'id': post_assigned.id,
            'ccb_id': post_assigned.ccb_id.id,
            'judge_id': post_assigned.judge_id_id,
            'lawyer_id': post_assigned.lawyer_id_id,
            'priority': post_assigned.priority
        }

        return JsonResponse(result)
    except Exception as e:
        # Handle the exception and provide an error response
        return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)





@csrf_exempt
def receiver_web(request):
    try:
        ccb_id = request.POST.get("ccb_id")
        court_type = request.POST.get("court_type")
        lawyer_id = request.POST.get("lawyer_id")

        # Get the available judge
        judge = returnAvailableJudge(court_type)
        lawyer = Laywers.objects.get(int(lawyer_id))
        # Calculate the priority
        priority = getTotalPriority(request.GET.get("firs"))

        # Create a PostAssigened object
        post_assigned = Assigened(
            ccb_id=ccb_id,
            judge=judge,
            lawyer=lawyer,
            priority=priority
        )
        post_assigned.save()

        # Serialize the object to JSON
        result = serializers.serialize('json', [post_assigned])

        return JsonResponse(result, safe=False)
    except Exception as e:
        # Handle the exception as needed, e.g., log it or return an error response
        return JsonResponse({'error': f'An error occurred {e=}'}, status=500)
from django.shortcuts import render
from django.http import JsonResponse
from models import CCB, Section, Petitioner, Respondent
from lawyerhandle.models import Laywers
import threading
from engine2.views import receiver
from docquery import document, pipeline

querrys:list = ["Date when reported", "Date of Occurence", "State", "District", "Crime", "Sub-Category", "Police Station", "FIR Number", "Year", "Section Numbers", "Name of reporter", "Name of criminal"]


def interface(request):
    if request != 'POST':
        error_data = {
        'error': 'An error occurred.',
        'status': 'error',
    }   
        return JsonResponse(error_data, status=400)
    
    document = request.POST.get('fir')
    answers:list = []
    answer_pipe = pipeline('document-question-answering')
    
    for query in querrys:
        answers.append(answer_pipe(question=query, **document.context)[0]['answers'].trim())
    
    ccb_obj = CCB(
        filing_date = answers[0],
        crime_date = answers[1],
        state = answers[2],
        district = answers[3],
        category = answers[4],
        sub_category = answers[5],
        police_station = answers[6],
        fir_number = answers[7],
        year = int(answers[8])
        court_type = request.GET.get("court_type", "district"),
    )
    ccb_obj.save()
    resp = {
        'body': "file uploaded and scheduling",
        'status':"ok"
    }
    temp_json = {}
    try:
        lawyer = Laywers.objects.get(id=request.GET.get("lawyer_id"))
    except:
        print("lawyer not found")
    #ccb_id:int, court_type:str, lawyer_id:int, fir_list:list
    engine2_thread = threading.Thread(target=receiver, args=(
        ccb_id = ccb_obj,
        court_type = ccb_obj.court_type,
        lawyer_id = request.GET.get("lawyer_id"),
        fir_list = request.GET.get("fir_list"),
        temp_json = temp_json
        ))
    engine2_thread.start()
    engine2_thread.join()
    return JsonResponse(temp_json, status=200)
    return JsonResponse(resp, status=200)
    
    
    






















































# def first_req(request):
#     pipe = pipeline('document-question-answering')
#     #need path

#     doc = document.load_document("/path/to/document.pdf")
#     l = list()
#     for q in ["Date when reported", "Date of Occurence", "State", "District", "Crime", "Sub-Category", "Police Station", "FIR Number", "Year", "Section Numbers", "Name of reporter", "Name of criminal"]:
#         l.append(pipe(question=q, **doc.context)[0]['answers'].trim())
#     c = CCB(
#         filing_date = l[0]
#         crime_date = l[1]
#         state = l[2]
#         district = l[3]
#         category = l[4]
#         sub_category = l[5]
#         police_station = l[6]
#         fir_number = l[7]
#         year = int(l[8])
#     )
#     c.save()
#     for i in l[].split(','): 
#         p = Section(
#             section_num = int(i)
#             fir_number = l[7]
#         )
#         p.save()
#     for i in l[].split(','): 
#         p = Petitioner(
#             name = i
#             fir_number = l[7]
#         )
#         p.save()
#     for i in l[].split(','):
#         r = Respondent(
#             name = i
#             fir_number = l[7]
#             )
#     r.save()

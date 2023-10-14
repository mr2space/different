from django.urls import path
from .views import receiver_web



"""

        ccb_id = ccb_obj,
        court_type = ccb_obj.court_type,
        lawyer_id = request.GET.get("lawyer_id"),
        fir_list = request.GET.get("fir_list"),
        temp_json = temp_json
"""
urlpatterns = [
    path("r/", view=receiver_web)
]
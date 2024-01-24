from django.shortcuts import render
from django.views.generic import ListView
from .models import Facility

# Create your views here.
class ListFacilityView(ListView):
    template_name = "facility_list.html"
    model = Facility  

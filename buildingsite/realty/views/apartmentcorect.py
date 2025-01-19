from realty.models import Apartment
from django.shortcuts import render, get_object_or_404

def apartment_correct(request):

    return render(request, 'apartmentcorrect.html')

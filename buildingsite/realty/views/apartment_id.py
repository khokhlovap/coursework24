from realty.models import Apartment
from django.shortcuts import render, get_object_or_404

def apartment_id(request, apartment_id):
    # Получаем квартиру по её ID или возвращаем 404, если не найдена
    apartment = get_object_or_404(Apartment, id=apartment_id)

    context = {
        'apartment': apartment,
    }
    return render(request, 'apartmentid.html', context)

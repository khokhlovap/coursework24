"""Вьюшка для отражения всех свободных апартаментов + удаления выбранного апартамента"""

from django.shortcuts import render, redirect, get_object_or_404
from realty.models import Apartment, StatusApartment, InfoBuilding

def apartment_correct(request):
    # Получаем все апартаменты, исключая определенные статусы
    apartments = Apartment.objects.exclude(
        statusapartment__status_apartment__in=['sold', 'booked', 'consideration']
    ).select_related('code_building').order_by('id').distinct()

    # Формируем полное адресное поле для каждого апартамента
    for apartment in apartments:
        apartment.full_address = f"{apartment.code_building.street}, {apartment.code_building.number_building}"

    context = {
        'apartments': apartments,
    }

    return render(request, 'apartmentcorrect.html', context)


def delete_apartment(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    apartment.delete()
    return redirect('apartment_correct')

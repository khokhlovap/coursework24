"""Вьюшка для апартамента по id
    Форма с информацией + редактирование цены + сохранение в бд"""

from django.shortcuts import render, get_object_or_404, redirect
from realty.models import Apartment, InfoBuilding

def apartment_id(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    info_building = apartment.code_building  # Получаем информацию о здании

    if request.method == 'POST':
        price = request.POST.get('price')
        if price:
            Apartment.objects.filter(id=apartment_id).update(price=price)
            return redirect('apartment_id', apartment_id=apartment.id)  # Переход на страницу с деталями

    context = {
        'apartment': apartment,
        'info_building': info_building
    }

    return render(request, 'apartmentid.html', context)

"""Вьюшка для главной страницы"""

from django.db.models import Avg
from realty.models import Apartment, StatusApartment, InfoBuilding, ApplicationWebsite
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect
from realty.forms.form_application import ApplicationWebsiteForm


def apartment(request):
    # Получаем все апартаменты, исключая те, которые имеют статус "продано" и "на рассмотрении" и "забронировано", фильтрация по возрастанию кол-ва комнат
    apartments = Apartment.objects.exclude(id__in=StatusApartment.objects.filter(status_apartment__in=['sold', 'consideration', 'booked']).values_list(
        'id_apartment', flat=True)).order_by('number_rooms')
    print(apartments)

    # Обработка поиска по количеству комнат
    room_count = request.GET.get('room_count')
    if room_count:
        apartments = apartments.filter(number_rooms=room_count)

    # Пагинация
    page = request.GET.get('page', 1)
    paginator = Paginator(apartments, 3)  # 3 на странице
    apartments_page = paginator.get_page(page)

    # Сообщение об отсутствии результатов
    not_found_message = None
    if room_count and not apartments.exists():
        not_found_message = "Апартаменты с введенным количеством комнат не найдены."

    # Получаем здания, которые находятся в Москве + фотографии
    buildings = InfoBuilding.objects.filter(city='Москва').prefetch_related('photos')

    # Словарь для уникальных комплексов
    unique_complexes = {}

    for building in buildings:
        # Формируем уникальный идентификатор для комбинации улицы и номера дома
        key = (building.street, building.number_building)

        if key not in unique_complexes:
            # Сохраняем первое здание, которое соответствует уникальному ключу
            unique_complexes[key] = {
                'street': building.street,
                'number_building': building.number_building,
                'image': building.photos.first().image.url if building.photos.exists() else None,
            }

        # Добавляем данные с формы
        if request.method == 'POST':
            form = ApplicationWebsiteForm(request.POST)
            if form.is_valid():
                application = form.save(commit=False)
                application.status_application = 'accepted'  # или любое другое значение по умолчанию
                application.save()
                return redirect('apartment')
        else:
            form = ApplicationWebsiteForm()


    context = {
        'complexes': unique_complexes.values(),
        'apartments': apartments_page,
        'not_found_message': not_found_message,
        'form': form,
    }

    return render(request, 'homepage.html', context)

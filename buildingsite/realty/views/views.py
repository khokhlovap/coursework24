from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from realty.models import Apartment, RegularCustomers
from django.db.models import Avg

def apartment_list(request):
    # Получаем данные из базы данных
    apartments = Apartment.objects.filter(price__gt=973374.340).exclude(number_rooms=3).order_by('-code_building')
    # Получаем сегодняшнюю дату
    today = timezone.now().date()  # Обновляем дату каждый раз при запросе

    print("Сегодняшняя дата:", today)



    # Логирование для проверки
    print(apartments.query)  # Выводим SQL-запрос для проверки

    # Вариант 2: обращение к связанной таблице через deal2
    customers_with_expensive_aparts = RegularCustomers.objects.filter(
        deal2__price__gt=1000000,
        deal2__code_building__city='Москва'
    )

    # Получить среднюю цену квартир в Москве
    avg_moscow_price = Apartment.objects.filter(code_building__city='Москва').aggregate(avg_price=Avg('price'))['avg_price']


    context = {
        'apartments': apartments,
        'today': today,
        'customers': customers_with_expensive_aparts,
        'avg_moscow_price': avg_moscow_price,
    }

    return render(request, 'apartment_list.html', context)



def apartment_detail(request, apartment_id):
    # Получаем квартиру по её ID или возвращаем 404, если не найдена
    apartment = get_object_or_404(Apartment, id=apartment_id)

    context = {
        'apartment': apartment,
    }
    return render(request, 'apartment_detail.html', context)

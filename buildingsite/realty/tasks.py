from datetime import date
from celery import shared_task
from .models import Apartment  # Убедитесь, что импортируете правильную модель

@shared_task
def decrease_apartment_prices():
    """
    Периодическая задача, снижающая цену апартаментов на 5%
    каждый 11 числа месяца.
    """
    today = date.today()
    eleventh_day = date(today.year, today.month, 26)

    # Проверяем, если сегодня 11 число
    if today == eleventh_day:
        apartments = Apartment.objects.all()
        for apartment in apartments:
            if apartment.price > 0:  # Убедиться, что цена положительная
                current_price = float(apartment.price)
                discount = current_price * 0.05  # Скидка 5%
                new_price = current_price - discount
                apartment.price = new_price
                apartment.save()
                print(f"Цена для апартамента {apartment.apartment_code} снижена до {apartment.price}")

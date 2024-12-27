"""
Периодические задачи celery
"""
from datetime import date
from celery import shared_task
from django.core.mail import send_mail

from .models import Apartment, RegularCustomers


@shared_task
def decrease_apartment_prices():
    """
    Периодическая задача, снижающая цену апартаментов на 5%
    каждый 26 числа месяца.
    """
    today = date.today()
    eleventh_day = date(today.year, today.month, 27)

    # Проверяем, если сегодня 26 число
    if today == eleventh_day:
        apartments = Apartment.objects.all()
        for apartment in apartments:
            if apartment.price > 0:  # Убедиться, что цена положительная
                current_price = float(apartment.price)
                discount = current_price * 0.05  # Скидка 5%
                new_price = current_price - discount
                apartment.price = new_price
                apartment.save()
                print(f"Цена для апартамента {apartment.apartment_code} "
                      f"снижена до {apartment.price}")


@shared_task
def send_email_january(recipient_email, subject, message):
    """
    Периодическая задача, отправляющая письма всем постоянным клиентам 31 декабря.

    Отправка письма с помощью Celery.
    Args:
        recipient_email (str): Адрес получателя письма.
        subject (str): Тема письма.
        message (str): Содержимое письма.

    """

    send_mail(
        subject,
        message,
        'hpolina852@gmail.com',
        [recipient_email],
        fail_silently=False,
    )

    return f"Письмо отправлено на {recipient_email}"

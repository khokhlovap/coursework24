"""
Модели бд приложения realty
"""

from django.db import models
from simple_history.models import HistoricalRecords
from django.utils import timezone
from django.db.models import Avg
from django.urls import reverse

class InfoBuilding(models.Model):
    """
    Таблица Информация  о здании
    """
    code_building = models.IntegerField(default=0, verbose_name="Код дома")
    city = models.CharField(max_length=200, verbose_name= "Город")
    street = models.CharField(max_length=200, verbose_name="Название улицы")
    number_building = models.CharField(max_length=200, verbose_name="№ дома")
    updated = models.DateTimeField(auto_now=True)
    file_document = models.FileField(upload_to='documents/', blank=True, null=True, verbose_name="Документ")
    website_url = models.URLField(blank=True, null=True, verbose_name="Сайт")
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.code_building}"

    class Meta: # pylint: disable=too-few-public-methods
        """
        Название тпблицы
        """
        verbose_name = 'Информация о ЖК'
        verbose_name_plural = 'Информация о ЖК'


class ApartmentManager(models.Manager):
    def avg_price_by_city(self, city):
        """Средняя цена квартир в указанном городе"""
        return self.filter(
            code_building__city=city
        ).aggregate(avg_price=Avg('price'))

        
class Apartment (models.Model):
    """
    Таблица Апартаменты
    """
    number_rooms = models.SmallIntegerField\
        (verbose_name="Количество комнат")
    number_floor = models.SmallIntegerField\
        (verbose_name="Номер этажа")
    square = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Площадь, кв.м")
    price = models.DecimalField(max_digits=12, decimal_places=3, verbose_name="Стоимость")
    code_building = models.ForeignKey(InfoBuilding, verbose_name="Код здания",
                                      on_delete=models.CASCADE)
    apartment_code = models.CharField(null=True, blank=True, max_length=50, unique=True,
                                      verbose_name='Код апартамента')
    objects = ApartmentManager()
    history = HistoricalRecords()
    class Meta: # pylint: disable=too-few-public-methods
        """
        Название таблицы
        """
        verbose_name = 'Апартаменты'
        verbose_name_plural = 'Апартаменты'
        ordering = ['-code_building']
    def __str__(self):
        return f"{self.apartment_code}"

    def get_absolute_url(self):
        return reverse('apartment_detail', args=[str(self.id)])

    def building_info(self):
        """
        Отображение строки с информацией о местоположении и идентификаторах здания,
        включая город, улицу и номер здания
        """
        return (f"{self.code_building.city}, {self.code_building.street} "
                f"{self.code_building.number_building}")  # pylint: disable=no-member

    building_info.short_description = 'Информация о здании'

class ApartmentPhoto(models.Model):
    """
    Таблица Фото апартаментов
    """
    apartment = models.ForeignKey(Apartment, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/apartment/', verbose_name="Фото апартамента")
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание фото")
    history = HistoricalRecords()
    class Meta: # pylint: disable=too-few-public-methods
        """
        Название тпблицы
        """
        verbose_name = 'Фото апартамента'
        verbose_name_plural = 'Фото апартаментов'
    def __str__(self):
        return f"Фото для {self.apartment.apartment_code}"  # pylint: disable=no-member

class RegularCustomers(models.Model):
    """
    Таблица Постоянные клиенты
    """
    name_client=models.CharField(max_length=200, verbose_name="Имя")
    surname_client=models.CharField(max_length=200, verbose_name="Фамилия")
    number_phone=models.CharField(max_length=20, verbose_name="Номер телефона")
    email_client=models.EmailField(max_length=255, null=False, blank=False, verbose_name="Почта")
    deal2=models.ManyToManyField(Apartment, through="Deal2", related_name='aparts')
    history = HistoricalRecords()
    def __str__(self):
        return f"{self.id}"  # pylint: disable=no-member
    class Meta: # pylint: disable=too-few-public-methods
        """
        Название тпблицы
        """
        verbose_name = 'Постоянные клиенты'
        verbose_name_plural = 'Постоянные клиенты'

class StatusApartment(models.Model):
    """
    Таблица Статус апартаментов
    """
    APPLICATION_STATUS_APARTMENT = [
        ('sold', 'Продано'),
        ('booked', 'Забронировано'),
        ('consideration', 'На рассмотрении'),
    ]
    id_apartment=models.ForeignKey(Apartment, on_delete=models.CASCADE,
                                   verbose_name="Код Апартамента")
    status_apartment=models.CharField(max_length=200, verbose_name="Статус апартамента",
                                      choices=APPLICATION_STATUS_APARTMENT)
    data_change=models.DateField(null=True, blank=True,
                                 verbose_name="Дата изменения статуса")
    id_client = models.ForeignKey(RegularCustomers, on_delete=models.CASCADE,
                                  verbose_name="Клиент", null=True, blank=True)
    history = HistoricalRecords()
    class Meta: # pylint: disable=too-few-public-methods
        """
        Название тпблицы
        """
        verbose_name = 'Статус Апартаментов'
        verbose_name_plural = 'Статус Апартаментов'

    def __str__(self):
        return f"Квартира {self.id_apartment.number_rooms}, этаж {self.id_apartment.number_floor}"  # pylint: disable=no-member

class Deal2(models.Model):
    """
    Таблица Сделки, в таблице отражаюся только проданные апартаменты
    """
    apartment=models.ForeignKey(Apartment, on_delete=models.CASCADE,
                                verbose_name="Код Апартамента", related_name='deals')
    client=models.ForeignKey(RegularCustomers, on_delete=models.CASCADE,
                             verbose_name="ID Клиента", related_name="deals")
    data_deal=models.DateField(null=True, blank=True, verbose_name="Дата сделки")
    history = HistoricalRecords()
    class Meta: # pylint: disable=too-few-public-methods
        """
        Название тпблицы
        """
        verbose_name = 'Сделка - продано'
        verbose_name_plural = 'Сделка - продано'

class ApplicationWebsite(models.Model):
    """
    Таблица Заявки с сайта
    """
    APPLICATION_STATUS_CHOICES = [
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено'),
    ]
    name_client=models.CharField(max_length=200, verbose_name="Имя")
    number_phone=models.CharField(max_length=20, verbose_name="Номер телефона")
    status_application=models.CharField(max_length=200, verbose_name="Статус заявки",
                                        choices=APPLICATION_STATUS_CHOICES)
    # date_create2 = models.DateTimeField(auto_now=True)
    date_create3 = models.DateTimeField(auto_now=True, verbose_name="Дата создания заявки")
    history = HistoricalRecords()
    class Meta: # pylint: disable=too-few-public-methods
        """
        Название тпблицы
        """
        verbose_name = 'Заявки с сайта'
        verbose_name_plural = 'Заявки с сайта'



# Старая моодель
# class Deal(models.Model):
#     id_apartment=models.ForeignKey(Apartment, on_delete=models.CASCADE,
#                                    verbose_name="ID Апартамента")
#     id_client=models.ForeignKey(RegularCustomers, on_delete=models.CASCADE,
#                                 verbose_name="ID Клиента")
#     data_deal=models.DateField(null=True, blank=True, verbose_name="Дата сделки")
#     class Meta:
#         verbose_name = 'Сделка - продано'
#         verbose_name_plural = 'Сделка - продано'

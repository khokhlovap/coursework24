from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.
class InfoBuilding(models.Model):
    code_building = models.IntegerField(default=0, verbose_name=u"Код дома")
    city = models.CharField(max_length=200, verbose_name= u"Город")
    street = models.CharField(max_length=200, verbose_name=u"Название улицы")
    number_building = models.CharField(max_length=200, verbose_name=u"№ дома")
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.code_building}"

    class Meta:
        verbose_name = 'Информация о ЖК'
        verbose_name_plural = 'Информация о ЖК'
    
class Apartment (models.Model):
    number_rooms = models.SmallIntegerField(verbose_name=u"Количество комнат")
    number_floor = models.SmallIntegerField(verbose_name=u"Номер этажа")
    square = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=u"Площадь, кв.м")
    price = models.DecimalField(max_digits=12, decimal_places=3, verbose_name=u"Стоимость")
    code_building = models.ForeignKey(InfoBuilding, verbose_name=u"Код здания", on_delete=models.CASCADE)
    apartment_code = models.CharField(null=True, blank=True, max_length=50, unique=True, verbose_name='Код апартамента')
    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Апартаменты'
        verbose_name_plural = 'Апартаменты'

    def __str__(self):
        return f"{self.apartment_code}"
    
    def building_info(self):
        return f"{self.code_building.city}, {self.code_building.street} {self.code_building.number_building}"
    building_info.short_description = 'Информация о здании'

class ApartmentPhoto(models.Model):
    apartment = models.ForeignKey(Apartment, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/apartment/', verbose_name=u"Фото апартамента")
    description = models.CharField(max_length=255, blank=True, verbose_name=u"Описание фото")
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Фото апартамента'
        verbose_name_plural = 'Фото апартаментов'

    def __str__(self):
        return f"Фото для {self.apartment.apartment_code}"
    
class RegularCustomers(models.Model):
    name_client=models.CharField(max_length=200, verbose_name=u"Имя")
    surname_client=models.CharField(max_length=200, verbose_name=u"Фамилия")
    number_phone=models.CharField(max_length=20, verbose_name=u"Номер телефона")
    email_client=models.EmailField(max_length=255, null=False, blank=False, verbose_name=u"Почта")
    deal2=models.ManyToManyField(Apartment, through="Deal2", related_name='aparts')
    history = HistoricalRecords()
    def __str__(self):
        return f"{self.id}"
   
    class Meta:
        verbose_name = 'Постоянные клиенты'
        verbose_name_plural = 'Постоянные клиенты'

class StatusApartment(models.Model):
    APPLICATION_STATUS_APARTMENT = [
        ('sold', 'Продано'),
        ('booked', 'Забронировано'),
        ('consideration', 'На рассмотрении'),
    ]
    id_apartment=models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name=u"Код Апартамента")
    status_apartment=models.CharField(max_length=200, verbose_name=u"Статус апартамента", choices=APPLICATION_STATUS_APARTMENT)
    data_change=models.DateField(null=True, blank=True, verbose_name=u"Дата изменения статуса")
    id_client = models.ForeignKey(RegularCustomers, on_delete=models.CASCADE, verbose_name=u"Клиент", null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Статус Апартаментов'
        verbose_name_plural = 'Статус Апартаментов'

    def __str__(self):
        return f"Квартира {self.id_apartment.number_rooms}, этаж {self.id_apartment.number_floor}"
    

class Deal2(models.Model):
    apartment=models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name=u"Код Апартамента", related_name='deals')
    client=models.ForeignKey(RegularCustomers, on_delete=models.CASCADE, verbose_name=u"ID Клиента", related_name="deals")
    data_deal=models.DateField(null=True, blank=True, verbose_name=u"Дата сделки")
    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Сделка - продано'
        verbose_name_plural = 'Сделка - продано'

class ApplicationWebsite(models.Model):
    APPLICATION_STATUS_CHOICES = [
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено'),
    ]
    name_client=models.CharField(max_length=200, verbose_name=u"Имя")
    number_phone=models.CharField(max_length=20, verbose_name=u"Номер телефона")
    status_application=models.CharField(max_length=200, verbose_name=u"Статус заявки", choices=APPLICATION_STATUS_CHOICES)
    # date_create2 = models.DateTimeField(auto_now=True)
    date_create3 = models.DateTimeField(auto_now=True, verbose_name=u"Дата создания заявки")
    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Заявки с сайта'
        verbose_name_plural = 'Заявки с сайта'



# Старая моодель
class Deal(models.Model):
    id_apartment=models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name=u"ID Апартамента")
    id_client=models.ForeignKey(RegularCustomers, on_delete=models.CASCADE, verbose_name=u"ID Клиента")
    data_deal=models.DateField(null=True, blank=True, verbose_name=u"Дата сделки")
   
    class Meta:
        verbose_name = 'Сделка - продано'
        verbose_name_plural = 'Сделка - продано'
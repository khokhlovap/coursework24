from django.db import models

# Create your models here.
class InfoBuilding(models.Model):
    code_building = models.IntegerField(default=0, verbose_name=u"Код дома")
    city = models.CharField(max_length=200, verbose_name=u"Город")
    street = models.CharField(max_length=200, verbose_name=u"Название улицы")
    number_building = models.CharField(max_length=200, verbose_name=u"№ дома")
    
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
    
    class Meta:
        verbose_name = 'Апартаменты'
        verbose_name_plural = 'Апартаменты'

    def __str__(self):
        return f"{self.id}"
    
    def building_info(self):
        return f"{self.code_building.city}, {self.code_building.street} {self.code_building.number_building}"
    building_info.short_description = 'Информация о здании'

class StatusApartment(models.Model):
    id_apartment=models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name=u"ID Апартамента")
    status_apartment=models.CharField(max_length=200, verbose_name=u"Статус апартамента")
    data_change=models.DateField(null=True, blank=True, verbose_name=u"Дата изменения статуса")
    
    class Meta:
        verbose_name = 'Статус Апартаментов'
        verbose_name_plural = 'Статус Апартаментов'

    def __str__(self):
        return f"Квартира {self.id_apartment.number_rooms}, этаж {self.id_apartment.number_floor}"
    
class RegularCustomers(models.Model):
    name_client=models.CharField(max_length=200, verbose_name=u"Имя")
    surname_client=models.CharField(max_length=200, verbose_name=u"Фамилия")
    number_phone=models.CharField(max_length=20, verbose_name=u"Номер телефона")
    email_client=models.EmailField(max_length=255, null=False, blank=False, verbose_name=u"Почта")
    deal2=models.ManyToManyField(Apartment, through="Deal2", related_name='aparts')
   
    def __str__(self):
        return f"{self.id}"
   
    class Meta:
        verbose_name = 'Постоянные клиенты'
        verbose_name_plural = 'Постоянные клиенты'

class Deal2(models.Model):
    apartment=models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name=u"ID Апартамента", related_name='deals')
    client=models.ForeignKey(RegularCustomers, on_delete=models.CASCADE, verbose_name=u"ID Клиента", related_name="deals")
    data_deal=models.DateField(null=True, blank=True, verbose_name=u"Дата сделки")
   
    class Meta:
        verbose_name = 'Сделка - продано'
        verbose_name_plural = 'Сделка - продано'

class ApplicationWebsite(models.Model):
    name_client=models.CharField(max_length=200, verbose_name=u"Имя")
    number_phone=models.CharField(max_length=20, verbose_name=u"Номер телефона")
    status_application=models.CharField(max_length=200, verbose_name=u"Статус заявки")
    
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
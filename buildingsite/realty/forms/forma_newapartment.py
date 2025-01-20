"""Форма для создания нового апартамента + вьюшка"""

from django.shortcuts import render, redirect
from realty.models import Apartment, InfoBuilding, ApartmentPhoto
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['number_rooms', 'number_floor', 'square', 'price', 'code_building']
        widgets = {
            'number_rooms': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'number_floor': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'square': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'code_building': forms.Select(attrs={'class': 'form-select'}),
        }

def add_apartment(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        photo_form = ApartmentPhotoForm(request.POST, request.FILES)  # Обработка файлов
        if form.is_valid() and photo_form.is_valid():
            apartment = form.save()
            apartment_photo = photo_form.save(commit=False)
            apartment_photo.apartment = apartment
            apartment_photo.save()
            return HttpResponseRedirect(reverse('apartment_correct'))
            # return redirect('apartment_correct')
    else:
        form = ApartmentForm()
        photo_form = ApartmentPhotoForm()

    return render(request, 'add_apartment.html', {'form': form, 'photo_form': photo_form})


class ApartmentPhotoForm(forms.ModelForm):
    class Meta:
        model = ApartmentPhoto
        fields = ['image', 'description']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

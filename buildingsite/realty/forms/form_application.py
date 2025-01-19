"""Форма для сайта (собираем заявки)"""

from django import forms
from realty.models import ApplicationWebsite

class ApplicationWebsiteForm(forms.ModelForm):
    class Meta:
        model = ApplicationWebsite
        fields = ['name_client', 'number_phone']

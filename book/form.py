from crispy_forms.bootstrap import FormActions
from django import forms
from book.models import Contacts
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
# from crispy_forms.layout import *

class ContactsForm(forms.ModelForm):
    firstName = forms.CharField(label='Adı')
    lastName = forms.CharField(label='Soyadı')
    companyName = forms.CharField(label='Firma Adı')
    email = forms.EmailField(label='E-Posta')
    phoneNumber1 = forms.CharField(label='1. Telefon Numarası')
    phoneNumber2 = forms.CharField(label='2. Telefon Numarası')
    address = forms.CharField(label='Adres:')

    class Meta:
        model = Contacts
        fields = [
            'firstName',
            'lastName',
            'companyName',            
            'email',
            'phoneNumber1',
            'phoneNumber2',
            'address',
        ]
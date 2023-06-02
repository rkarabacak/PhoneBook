from crispy_forms.bootstrap import FormActions
from django.core import validators
# from django.utils.translation import ugettext_lazy as _
from django import forms
from book.models import Contacts
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
# from crispy_forms.layout import *

class ContactsForm(forms.ModelForm):
    

    def __init__(self, getNumber, *args, **kwargs): 
        # self.getNumber = kwargs.pop('getNumber')
        # print(self.getNumber)       
        super(ContactsForm, self).__init__(*args, **kwargs)
        self.fields['phoneNumber1'].widget = forms.TextInput(attrs={'value':getNumber})
        self.fields['companyName'].required = False
        self.fields['email'].required = False
        self.fields['phoneNumber2'].required = False
        self.fields['address'].required = False

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

    # def clean_companyName(self): # uniq alanlar için kod taraflı doğrulama
    #     companyName = self.cleaned_data['companyName']
    #     if Contacts.objects.filter(companyName=companyName).exists():
    #         raise forms.ValidationError(_('Bu firma adı sistemde kayıtlı'), code='invalid')
    #     return companyName
    
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if Contacts.objects.filter(email=email).exists():
    #         raise forms.ValidationError(_('Bu E-Posta adresi sistemde kayıtlı'), code='invalid')
    #     return email

    # def clean_phoneNumber2(self):
    #     phoneNumber2 = self.cleaned_data['phoneNumber2']
    #     if Contacts.objects.filter(phoneNumber2=phoneNumber2).exists():
    #         raise forms.ValidationError(_('Bu telefon numarası sistemde kayıtlı'), code='invalid')
    #     return phoneNumber2
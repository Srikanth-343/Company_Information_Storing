from django.forms import ModelForm
from django import forms
from webapp.models import Company_detailes
from .utils import OptionalChoiceField

class companyForm(ModelForm):
    Company = OptionalChoiceField(choices=(("Rapid Technologies LLC", "Rapid Technologies LLC"), ("Rapid Group of Companies", "Rapid Group of Companies"),("", "others")))

    class Meta:
        model = Company_detailes
        fields = '__all__'
        widgets={
            'Phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'Fax': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Optional'}),
            'Industry':forms.TextInput(attrs={'class': 'form-control'}),
            'Website': forms.TextInput(attrs={'class': 'form-control','placeholder':'www.abc.com'}),
            'NAICS_codes':forms.TextInput(attrs={'class': 'form-control'}),
            'Revenue': forms.NumberInput(attrs={'class': 'form-control'}),
            'EstimatedPayroll': forms.NumberInput(attrs={'class': 'form-control'}),
            'Number_of_Employees': forms.NumberInput(attrs={'class': 'form-control'}),
            'Number_of_Internal_Employees': forms.NumberInput(attrs={'class': 'form-control'}),
            'Number_of_consultants_on_OPT': forms.NumberInput(attrs={'class': 'form-control'}),
            'Number_of_consultants_on_CPT': forms.NumberInput(attrs={'class': 'form-control'}),
            'Number_of_consultants_on_H1B': forms.NumberInput(attrs={'class': 'form-control'}),
            'Number_of_card_consultants': forms.NumberInput(attrs={'class': 'form-control'}),
            'Number_of_US_Citizens': forms.NumberInput(attrs={'class': 'form-control'}),
            'Number_of_consultants_on_other_visa': forms.NumberInput(attrs={'class': 'form-control'}),
            'AddressLine1': forms.TextInput(attrs={'class': 'form-control'}),
            'AddressLine2': forms.TextInput(attrs={'class': 'form-control'}),
            'City': forms.TextInput(attrs={'class': 'form-control'}),
            'Zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'FederalID_EIN': forms.TextInput(attrs={'class': 'form-control'}),
            'GST_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'AddadditionalInformation': forms.TextInput(attrs={'class': 'form-control'}),
        }

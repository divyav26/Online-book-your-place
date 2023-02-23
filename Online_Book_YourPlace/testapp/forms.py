from django import forms
from django.contrib.auth.models import User
from django import forms
from django.forms import formset_factory
from .models import Contact

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']




class InvoiceForm(forms.Form):

        # fields = ['customer', 'message']
    customer = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            'rows':1
        })
    )
    customer_email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'email@company.com',
            'rows':1
        })
    )
    billing_address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Address',
            'rows':1
        })
    )
    message = forms.CharField(
        label='Remark',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Remark',
            'rows':1
        })
    )

class LineItemForm(forms.Form):

    service = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Name'
        })
    )
    quantity = forms.IntegerField(
        label='Fair',
        widget=forms.TextInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Age'
        }) #quantity should not be less than one
    )
    rate = forms.DecimalField(
        label='Age',
        widget=forms.TextInput(attrs={
            'class': 'form-control input rate',
            'placeholder': 'Price'
        })
    )
    amount = forms.DecimalField(
        disabled = True,
        label='Amount $',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
        })
    )

LineItemFormset = formset_factory(LineItemForm, extra=1)

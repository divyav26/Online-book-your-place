from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import Contact
from django.forms import formset_factory

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','contact','description']
        labels = {'name':'Enter Name',
                  'email':'Email',
                  'Contact':'Contact No',
                  'description':'Description'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'})
        }
class InvoiceForm(forms.Form):

        # fields = ['customer', 'message']
    customer = forms.CharField(
        label='Cusomter',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Customer/Company Name',
            'rows':1
        })
    )
    customer_email = forms.CharField(
        label='Customer Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'customer@company.com',
            'rows':1
        })
    )
    billing_address = forms.CharField(
        label='Billing Address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'rows':1
        })
    )
    message = forms.CharField(
        label='Message/Note',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'message',
            'rows':1
        })
    )

class LineItemForm(forms.Form):

    service = forms.CharField(
        label='Service/Product',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Service Name'
        })
    )
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Enter Book Name here',
            "rows":1
        })
    )
    quantity = forms.IntegerField(
        label='Qty',
        widget=forms.TextInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Quantity'
        }) #quantity should not be less than one
    )
    rate = forms.DecimalField(
        label='Rate $',
        widget=forms.TextInput(attrs={
            'class': 'form-control input rate',
            'placeholder': 'Rate'
        })
    )
    # amount = forms.DecimalField(
    #     disabled = True,
    #     label='Amount $',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control input',
    #     })
    # )

LineItemFormset = formset_factory(LineItemForm, extra=1)

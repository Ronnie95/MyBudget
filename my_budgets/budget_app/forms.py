from django import forms
from .models import Transactions, Income, Reminders, Goals
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['amount', 'date', 'description', 'category']
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class TransaForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ('amount', 'date', 'description', 'category')

    widgets = {
        'amount': forms.TextInput(attrs={'class': 'form-control'}),
        'date': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.TextInput(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'})
    }
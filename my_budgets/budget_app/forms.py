from django import forms
from .models import Transactions, Income, Reminders, Goals


class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['amount', 'date', 'description', 'category']
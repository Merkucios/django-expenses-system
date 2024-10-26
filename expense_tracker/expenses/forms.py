from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'currency', 'description', 'date', 'receipt', 'is_recurring']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

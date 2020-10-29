from django import forms

from expenses_tracker.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        labels = {
            'image_url': "Link to Image",
        }

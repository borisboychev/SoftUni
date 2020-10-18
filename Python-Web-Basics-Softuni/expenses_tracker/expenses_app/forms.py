from django import forms


class ExpensesForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    title = forms.CharField(max_length=50)
    image_url = forms.URLField()
    description = forms.Textarea()
    price = forms.FloatField()


class ProfileForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    budget = forms.IntegerField()

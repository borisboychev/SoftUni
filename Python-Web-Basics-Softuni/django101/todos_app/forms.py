from django import forms
from django.forms import HiddenInput

from todos_app.models import Todo


def min_validator(value):
    if not value or len(value) < 10:
        raise forms.ValidationError(f'Value should be more than 10, now it is {len(value)}')


class MyTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description']


class TodoForm(forms.Form):
    title = forms.CharField(max_length=30,
                            label='Title', )
    description = forms.CharField(required=False,
                                  label='Description',
                                  validators=(min_validator,))

    bot_catcher = forms.CharField(widget=HiddenInput, required=False,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            if 'class' in field.widget.attrs:
                value = field.widget.attrs['class'] + ' form-control'
            else:
                value = 'form-control'
            field.widget.attrs['class'] = value

    def clean_bot_catcher(self):
        if self.cleaned_data['bot_catcher']:
            raise forms.ValidationError("This is a bot")


    # email = forms.EmailField(label='Email',)
    # password = forms.CharField(widget=forms.PasswordInput)

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
    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'neshto-si',
            }
        )
    )
    description = forms.CharField()

    bot_catcher = forms.CharField(widget=HiddenInput, required=False, )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            if 'class' in field.widget.attrs:
                value = field.widget.attrs['class'] + ' form-control'
            else:
                value = 'form-control'
            field.widget.attrs['class'] = value

    def clean_bot_catcher(self):
        if len(self.cleaned_data['bot_catcher']):
            raise forms.ValidationError("This is a bot")


class TodoFormFull(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False,
        label="The Desc",
    )
    my_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    size = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'type': 'range',
                'class': 'form-control'
            },
        ),
    )

from django import forms

from .models import City, ProgrammingLanguage


class FindForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        required=False,
        to_field_name='slug',
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Город',
        empty_label='Не выбрано',
    )

    language = forms.ModelChoiceField(
        queryset=ProgrammingLanguage.objects.all(),
        required=False,
        to_field_name='slug',
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Язык программирования',
        empty_label='Не выбрано',
    )

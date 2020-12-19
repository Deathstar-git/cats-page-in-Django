from .models import Cat
from django.forms import ModelForm, TextInput


class CatForm(ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'age', 'color']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Введите имя'}),
            'age': TextInput(attrs={'class': 'form-control',
                                    'placeholder': 'Введите возраст'}),
            'color': TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Введите цвет'}),
        }

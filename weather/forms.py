from django.forms import ModelForm, TextInput
from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'City Name',
                       'aria-label': 'Enter email address...',
                       'data-sb-validations': "required,email",
                       }
            )
        }

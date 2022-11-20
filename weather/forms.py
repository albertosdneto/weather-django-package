from django.forms import ModelForm, TextInput, MultiWidget
from .models import City
from captcha.fields import CaptchaField, CaptchaTextInput


class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = 'weather/custom_field.html'


class CityForm(ModelForm):
    captcha = CaptchaField(widget=CustomCaptchaTextInput, label='Please enter the characters in the image')

    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(
                attrs={'class': 'form-control mb-2',
                       'placeholder': 'City Name',
                       'aria-label': 'Enter email address...',
                       'data-sb-validations': "required,email",
                       }
            )
        }

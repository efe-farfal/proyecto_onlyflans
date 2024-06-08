from django import forms
from .models import Contacto

class TextInputWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'type': 'text'}
        super().__init__(*args, **kwargs)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields =  ['costumer_name', 'costumer_email', 'message']
        widgets = {
            'costumer_email': TextInputWidget(),
        }
from datetime import datetime
from django.forms import *
from APP.admins.models import Productos

class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Productos
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Tu lógica personalizada aquí
        if commit:
            instance.save()
        return instance
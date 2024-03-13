from datetime import datetime
from django.forms import *
from APP.admins.models import Productos, Clientes

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

class ClientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = "form-control"
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Clientes
        exclude = ['vendedor']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:  # Verificamos si el usuario fue proporcionado
            instance.vendedor = self.user  # Asignamos el usuario logueado como vendedor
        if commit:
            instance.save()
        return instance
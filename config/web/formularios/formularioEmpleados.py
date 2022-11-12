from logging import PlaceHolder
from django import forms

class FormularioRegistroEmpleados(forms.Form):

    EMPLEADOS=(
        (1, 'Cocina'),
        (2, 'Mesa'),
        (3, 'Admon'),
        (4, 'Servicio')
    )

    nombreEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label='Nombre:'
    )
    apellidoEmpleado=forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required=True,
        label='Apellido:'
    )
    direccionEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=200,
        required=True,
        label='Dirección:'
    )
    documentoEmpleado=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        label='Documento:'

    )
    rolEmpleado=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-control mb-3"}),
        choices=EMPLEADOS
    )

    
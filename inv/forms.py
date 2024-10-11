from django import forms        # Importa el módulo de formularios de Django.
from .models import Categoria   # Importa el modelo 'Categoria' desde el archivo 'models.py'.


class CategoriaForm(forms.ModelForm):   # Define una clase de formulario que hereda de 'forms.ModelForm'.
    
    class Meta:  # Define la metadata del formulario.
        model = Categoria   # Asocia este formulario con el modelo 'Categoria'.
        fields = ['descripcion', 'estado']   # Especifica qué campos del modelo serán incluidos en el formulario.
        labels = {'descripcion': 'Descripción de la Categoría', 'estado': 'Estado'}
        # Define etiquetas personalizadas para los campos 'descripcion' y 'estado'.

        widgets = {'descripcion': forms.TextInput()}
        # Asocia un widget específico (en este caso, un campo de texto) para el campo 'descripcion'.
    
    def __init__(self, *args, **kwargs):  # Sobrescribe el método de inicialización de la clase.
        super().__init__(*args, **kwargs)   # Llama al constructor del formulario original para inicializarlo
    
        for field in iter(self.fields):  # Itera sobre todos los campos definidos en el formulario.
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            # Actualiza los atributos del widget de cada campo, agregando la clase 'form-control' (de Bootstrap)
            # para estilizar los campos del formulario.

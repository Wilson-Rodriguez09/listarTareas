from.models import Tareas
from django.forms import ModelForm

class TareaForm(ModelForm):
    class Meta:
        model = Tareas
        fields = '__all__'
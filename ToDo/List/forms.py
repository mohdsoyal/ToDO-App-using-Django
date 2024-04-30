from django.forms import ModelForm
from .models import ToDOclass

class FormModel(ModelForm):
    class Meta:
        model = ToDOclass
        fields="__all__"



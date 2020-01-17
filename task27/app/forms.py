from django import forms
from .models import cpu_ram_model
class cpu_ram_form(forms.ModelForm):
    class Meta:
        fields='__all__'
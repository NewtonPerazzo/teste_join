from app import models
from django import forms

class AlvoForm(forms.ModelForm):

    class Meta():
        model = models.Alvo
        fields = ('nome', 'dt_expiracao', 'latitude', 'longitude')
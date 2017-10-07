from django import forms
from .models import Contacte

class ContacteForm(forms.ModelForm):
    class Meta:
        model = Contacte
        fields = ('nom','prenom','telephone','ville','rue','numero_de_la_voie','code_postal' ,'mail' ,'message')

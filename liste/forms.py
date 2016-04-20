from django import forms
from django.forms import ModelForm
from liste.models import Personne

class PersonneForm(ModelForm):
    class Meta:
        model = Personne
        fields = ['prenom', 'nom', 'phone', 'email']
    def clean_nom(self):
        nom = self.cleaned_data['nom']
        return nom.upper()
    def clean_prenom(self):
        prenom = self.cleaned_data['prenom']
        return prenom.title()
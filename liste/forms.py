from django.forms import ModelForm
from liste.models import Personne

class PersonneForm(ModelForm):
    class Meta:
        model = Personne
        fields = ['prenom', 'nom', 'phone', 'email']
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from liste.models import Personne
from liste.forms import PersonneForm

def personne(request):
    if request.method == 'POST':
        form = PersonneForm(request.POST)
        
        if form.is_valid():
            prenom = form.cleaned_data['prenom']
            nom = form.cleaned_data['nom']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            
            form.save()
        
    else:
        form = PersonneForm()
            
    return render(request, 'liste/form.html', locals())
    
def liste(request):
    personnes = Personne.objects.all().order_by('nom')
    return render(request, 'liste/liste.html', {'personnes': personnes})

def info(request, id):
    personne = get_object_or_404(Personne, id=id)
    return render(request, 'liste/personne.html', {'personne': personne})

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = 'Montez en voiture'
    return HttpResponse(text)

# Create your views here.

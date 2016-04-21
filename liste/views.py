from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from liste.forms import PersonneForm
from liste.models import Personne

def formulaire(request):
    if request.method == 'POST':
        form = PersonneForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/home/')
        
    else:
        form = PersonneForm()
            
    return render(request, 'liste/form.html', locals())
    
def home(request):
    personnes = Personne.objects.all().order_by('nom')
    return render(request, 'liste/liste.html', {'personnes': personnes})

def delete(request, id):
    personne = get_object_or_404(Personne, id=id)
    personne.delete()
    return redirect('/home/')

def edit(request, id):
    if request.method == 'POST':
        form = PersonneForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/home/')
        
    else:
        personne = get_object_or_404(Personne, id=id)
        form = PersonneForm(initial = {
            'prenom':personne.prenom,
            'nom':personne.nom,
            'phone':personne.phone,
            'email':personne.email
        })
        personne.delete()

    return render(request, 'liste/form.html', locals())

# Create your views here.

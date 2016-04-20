from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from liste.forms import PersonneForm
from liste.models import Personne

def formulaire(request):
    if request.method == 'POST':
        form = PersonneForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
        
    else:
        form = PersonneForm()
            
    return render(request, 'liste/form.html', locals())
    
def home(request):
    personnes = Personne.objects.all().order_by('nom')
    return render(request, 'liste/liste.html', {'personnes': personnes})

# Create your views here.

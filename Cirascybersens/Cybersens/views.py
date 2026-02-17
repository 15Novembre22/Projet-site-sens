from django.shortcuts import render, redirect
from .models import CyberHygiene
from django.contrib import messages
from incident.forms import IncidentForm

# Create your views here.
def  Accueil_view(request):
    conseils = CyberHygiene.objects.all().order_by('-date_pub')
   

    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre signalement a été envoyé avec succès.")

            # Redirige vers l'ancre #signaler pour rester sur le bon onglet
            return redirect('/#signaler') 
    else:
        # On crée le formulaire vide pour l'affichage initial
        form = IncidentForm()

    # On envoie tout au template unique 'welcome.html'
    context = {
        'all_conseils': conseils,
        'incident_form': form # On le passe ici
    }
    
    return render(request, 'welcome.html', context)


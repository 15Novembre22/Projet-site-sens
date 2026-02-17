from django.shortcuts import render, redirect
from .forms import IncidentForm

# Vue pour signaler un incident
def signaler_incident(request):
    if request.method == 'POST':
        # On donne toutes les données (POST et fichiers) au formulaire
        form = IncidentForm(request.POST, request.FILES)

        # Django vérifie si les champs sont valides
        if form.is_valid():
            # Sauvegarde de l'objet Incident en base
            form.save()

            # On renvoie un formulaire vide avec un message de succès
            return render(request, 'welcome.html', {
                'form': IncidentForm(),
                'success': True
            })
    else:
        # Si ce n'est pas un POST, on affiche un formulaire vide
        form = IncidentForm()

    # Affichage du formulaire (avec erreurs si POST invalide)
    return render(request, 'welcome.html', {'form': form})
from django.shortcuts import render
from .models import CyberHygiene

# Create your views here.
def  Accueil_view(request):
    conseils = CyberHygiene.objects.all().order_by('-date_pub')
    return render(request, 'welcome.html', {'all_conseils': conseils})


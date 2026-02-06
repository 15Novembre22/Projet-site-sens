from django.shortcuts import render

# Create your views here.
def  Accueil_view(request):
    return render(request, 'welcome.html')
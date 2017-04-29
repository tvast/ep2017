# coding: utf-8

from django.shortcuts import render,redirect
from .forms import FormSimulateur2017
# from .donnees import Algo_simu_EP2017_v2 as algo

def accueil(request):
#     sauvegarde = False
#     form = EntreePourcentages(request.POST or None)
#     if form.is_valid():
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = FormSimulateur2017(request.POST or None)
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        val_abs_NDA = form.cleaned_data['abs_NDA']/100
        val_mac_NDA = form.cleaned_data['mac_NDA']/100
        donnees={"H4":val_abs_NDA,"J4":val_mac_NDA}
        resultats=algo.get_resultat_simu(donnees) # envoie un dictionnaire à simuler_resultat
        # Transférer les données pour traitement à Python
        return render(request,'simulateurelections2017/resultats.html',{'pv_mac':resultats["pv_mac"],'pv_lp':resultats["pv_lp"]})
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'simulateurelections2017/index.html', locals())

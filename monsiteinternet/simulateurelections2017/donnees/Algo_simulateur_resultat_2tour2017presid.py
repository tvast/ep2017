# Algorithme en python de résultat aux élections présidentielles

# Données
from openpyxl import load_workbook

wb=load_workbook("Simulateur_deuxieme_tour_EP2017FR.xlsx")






import csv

def importer_tab_csv(nom_csv):
	"""
	Importe un fichier csv sous forme de tableau.
	Pour accéder à un élément, faire tab[numligne][numcolonne] avec tab l'instance
	"""
	with open(nom_csv) as f_obj:
		tab=[]
		reader=csv.reader(f_obj, delimiter=";")
		for row in reader:
			tab.append(row)
	return tab

stat_premier_tour_global=importer_tab_csv("stat_premier_tour_global.csv")
resultat_premier_tour=importer_tab_csv("resultat_premier_tour.csv")
pronostic_deuxieme_tour=importer_tab_csv("pronostic_deuxieme_tour.csv")
stat_deuxieme_tour=importer_tab_csv("stat_deuxieme_tour.csv")
resultat_deuxieme_tour=importer_tab_csv("resultat_deuxieme_tour.csv")

# On récupère les entrées de notre formulaire depuis le POST

def recup_colonne (tab,c,l1,l2):
	return [ligne[c] for ligne in pronostic_deuxieme_tour[l1:l2]]

def recup_partie_tab(tab,c1,c2,l1,l2):
	"""
	Renvoie une partie du tableau, les colonnes étant en ligne
	"""
	tab=[]
	for num_colonne in range(c1,c2+1):
		tab.append(recup_colonne(tab,num_colonne,l1,l2))
	return tab

pourc_abst_2 = recup_colonne(pronostic_deuxieme_tour,1,2,13) #ok
pourc_votes_macron_2= recup_colonne(pronostic_deuxieme_tour,3,2,13)





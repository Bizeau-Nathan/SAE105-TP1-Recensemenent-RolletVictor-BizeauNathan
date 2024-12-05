import csv
import matplotlib.pyplot as plt


# Importation des métadonnées de communes sous forme de liste

communes = []
with open('metadonnees_communes.csv', newline='') as csvcommunes:
    reader = csv.reader(csvcommunes, delimiter=';')
    for row in reader:
        communes.append(row)


# Importation des données de 2008 sous forme de liste

liste_2008 = []
with open('donnees_2008.csv', newline='') as csv2008:
    reader = csv.reader(csv2008, delimiter=',')
    for row in reader:
        liste_2008.append(row)


# Importation des données de 2016 sous forme de liste

liste_2016 = []
with open('donnees_2016.csv', newline='') as csv2016:
    reader = csv.reader(csv2016, delimiter=',')
    for row in reader:
        liste_2016.append(row)


# Importation des données de 2021 sous forme de liste

liste_2021 = []
with open('donnees_2021.csv', newline='') as csv2021:
    reader = csv.reader(csv2021, delimiter=';')
    for row in reader:
        liste_2021.append(row)


# Importation des données de 2023 sous forme de liste

liste_2023 = []
with open('donnees_2023.csv', newline='') as csv2023:
    reader = csv.reader(csv2023, delimiter=';')
    for row in reader:
        liste_2023.append(row)


# Importation des données de 2023 sous forme de liste

nb_communes = []
with open('departements-france.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        nb_communes.append(row)


# Entrée de la ville à étudier ar l'utilisateur

departement = input("Quel département souhaitez-vous étudier ? (entrez son numéro) ")


# Initialisation d'une liste pour regrouper les données de chaque années

populations = []


# Récupération du nom de la commune

nom_dep = ""

for i in nb_communes:
    if departement in i[0]:
        nom_dep = i[1]

print("Nom département =", nom_dep)


# Calcul de la population de 2008

pop_2008 = 0

for i in liste_2008:
    if departement in i[2]:
        pop_2008 += int(i[9])

print("Pop. 2008 =", pop_2008)
populations.append(pop_2008)


# Calcul de la population de 2016

pop_2016 = 0

for i in liste_2016:
    if departement in i[2]:
        pop_2016 += int(i[9])

print("Pop. 2016 =", pop_2016)
populations.append(pop_2016)


# Calcul de la population de 2021

pop_2021 = 0

for i in liste_2021:
    if departement in i[1]:
        pop_2021 += int(i[5])

print("Pop. 2021 =", pop_2021)
populations.append(pop_2021)


# Calcul de la population de 2023

pop_2023 = 0

for i in liste_2023:
    if departement in i[2]:
        pop_2023 += int(i[10])

print("Pop. 2023 =", pop_2023)
populations.append(pop_2023)


# Création du graphique

x = [2008, 2016, 2021, 2023]
y = populations

plt.plot(x, y)
plt.title("Evolution de la population de " + nom_dep)
plt.scatter(x, y)
plt.show()
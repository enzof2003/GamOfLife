# Pour gérer les tableaux à 2 dimension, numpy possède des matrices, plus lisible et avec des fonction pratique
import numpy as np

# Fonction permettant à l'utilisateur d'entrer un chiffre (avec vérification)
# avec la possibilité de mettre un message customisé
def intInput(message="Un chiffre : ") -> int:
    num = input(message)
    try:
        num = int(num)
        return num
    except ValueError:
        print("La valeur n'est pas un chiffre")
        quit(-1000)


def configInit(tableauInput):
    # initialisation aléatoire des valeurs de chaque cellules
    tailleTableau = tableau.shape[1]
    # On va parcourir chaque cellule (mais pas celles des bordures)
    # puis leur attribuer soit 1 ou 0 de manière aléatoire
    for i in range(tailleTableau-2):
        for j in range(tailleTableau-2):
            tableauInput[i+1,j+1]=np.random.randint(2)

    # Puis on continue la configuration
    nombreEtapes = intInput("Nombre d'etapes pour le Conway : ")
    for iteration in range(nombreEtapes):
        changeEtat(tableauInput)
        print("================== Etape numéro",iteration+1,"==================")
        imprime(tableauInput)


def changeEtat(tableauInput):
    #On réutilise le code de configInit pour parcourir le tableau
    tailleTableau = tableau.shape[1]
    for i in range(tailleTableau - 2):
        for j in range(tailleTableau - 2):
            # Et on vérifie grâce à la fonction nbVoisin le nouvel état de la cellule
            nbVoisinCelluleCourante = nbVoisin(i+1,j+1,tableauInput)
            if nbVoisinCelluleCourante == 1 or nbVoisinCelluleCourante >= 4:
                tableau[i+1,j+1]=0
            elif nbVoisinCelluleCourante == 2 or nbVoisinCelluleCourante == 3:
                tableau[i+1,j+1]=1
            # Sinon, on ne fait rien


#Autre mode d'affichage plus joli avec des carrés
def imprime(tableauInput):
    tailleTableau = tableau.shape[1]
    # On initialise la string d'affichage
    ligneActuelle = ""
    for i in range(tailleTableau - 2):
        for j in range(tailleTableau - 2):
            # Puis selon le contenue de la cellule, on met un carré pleins ou vide
            if tableau[i+1,j+1] == 1:
                ligneActuelle += "▣"
            else:
                ligneActuelle += "□"
        ligneActuelle+="\n"
    print(ligneActuelle)

def imprimeDifference(tableauBase, nouveauTableau):
    tailleTableau = tableau.shape[1]
    #On crée un tableau contenant la différence (0 / 1 avec resultat du changement, 2 si rien ne c'est passé
    tableauDifference = np.zeros((tailleTableau,tailleTableau),dtype=int)
    # On initialise la string d'affichage
    ligneActuelle = ""
    for i in range(tailleTableau - 2):
        for j in range(tailleTableau - 2):
            if tableauBase[i+1,j+1]!=nouveauTableau[i+1,j+1]:
                tableauDifference[i+1,j+1] = nouveauTableau[i+1,j+1]
            else:
                tableauDifference[i + 1, j + 1] = 2

    #PARTIE AFFICHAGE (similaire à imprime()
    for i in range(tailleTableau - 2):
        for j in range(tailleTableau - 2):
            # Puis selon le contenue de la cellule, on met un carré pleins ou vide
            if tableauDifference[i+1,j+1] == 1:
                ligneActuelle += "▣"
            elif tableauDifference[i+1,j+1] == 2:
                ligneActuelle += "□"
            else:
                ligneActuelle += "▨"
        ligneActuelle+="\n"
    print(ligneActuelle)




def nbVoisin(posX, posY,tableauInput)->int:

    # On va faire l'addition de toutes les cellules autours de la cellule actuel
    # Dans le sens horaire en partant de celle au dessus
    nombreVoisin = int(tableauInput[posX,posY-1]+
                       tableauInput[posX+1,posY-1]+
                       tableauInput[posX+1,posY]+
                       tableauInput[posX+1,posY+1]+
                       tableauInput[posX,posY+1]+
                       tableauInput[posX-1,posY+1]+
                       tableauInput[posX-1,posY]+
                       tableauInput[posX-1,posY-1])
    return nombreVoisin


# On ne prend pas en compte la bordure des 0 dans cette constante
TAILLE_TABLEAU_UTILISABLE = 4


tableau = np.zeros((TAILLE_TABLEAU_UTILISABLE+2, TAILLE_TABLEAU_UTILISABLE+2), dtype=int)

configInit(tableau)

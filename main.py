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
        print('The provided value is not a number')
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
        imprime(tableauInput)


def changeEtat(tableauInput):
    print("a")


def imprime(tableauInput):
    print(tableauInput)


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
TAILLE_TABLEAU_UTILISABLE = 5


tableau = np.zeros((TAILLE_TABLEAU_UTILISABLE+2, TAILLE_TABLEAU_UTILISABLE+2), dtype=int)

configInit(tableau)

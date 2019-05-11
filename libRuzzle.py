""" bibliothèque de fonctions pour le
            projet Ruzzle
            par jacques Pichon
            mai 2019           """

import unidecode
import random
import tkinter as tk
# Preparation du fichier dico.txt
# On définit une variable fichierLu qui est associée
# au fichier de nom 'dico.txt' est qui est ouvert en lecture (r)ead
# au format (t)exte.
def preparationDico (fichier):
    fichierLu= open(fichier, 'rt', encoding="utf-8")

    # On lit toutes les lignes de ce fichier et on les place dans une liste
    # de nom lignesLues
    lignesLues= fichierLu.readlines()

    # On ferme le fichier
    fichierLu.close()
    
    # traitement des lignes par des "lists comprehension"
    #on retire les commentaires
    lignesLues = [x for x in lignesLues if x[0] != '%']
    # on retire les lignes vide
    lignesLues = [x for x in lignesLues if x != '\n']
    # on enleve les retours de fin de ligne
    lignesLues = [x[0:-1] for x in lignesLues if x[-1] == '\n']
    #codage des accents
    lignesLues = [unidecode.unidecode(x) for x in lignesLues]
    return lignesLues

# recherche d'un mot dans le dico

def recherche (mot, listdico):
    if mot in listdico:
        return True
    else:
        return False
    
# generatino aleatoire de lettre pour la grille   
def generationLettre():
    alphabet =  ["A", "B" , "C" , "D" , "E" , "F", "G", "H" , "I" , "J" , "K", "L" , "M", "N", "O", "P", "Q", "R", "S" , "T" , "U", "V" , "W" , "X" , "Y", "Z"] 
    i = random.randint(0,len(alphabet)-1)
    return alphabet[i]

# constuction des boutons
# grille de 4 x 4
def genGrille ( buttons, fen ):
    for i in range(0,16):
        buttons.append( tk.Button(fen, width = 5, text=generationLettre()) ) # commande a definir dans une fontion
    return buttons

# affichage de la grille de bouton avec les lettres
def afficheGrille (buttons):
    grow=1
    gcolumn=0
    for bout in buttons:
        bout.grid(row=grow,column=gcolumn)
        gcolumn = gcolumn+1
        if gcolumn > 3:
            gcolumn = 0
            grow = grow + 1

# recherche dans dico
# fonction qui rcherche un mot dans un dictionnaire

def estDansDico (mot , dico ) :
    if mot in dico:
        return True
    else :
        return False
    


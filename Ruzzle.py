"""  Programme principal du projet
        RUZZLE
        Jacques Pichon
        mai 2019
        formation DIU
"""
import libRuzzle as ruz
import tkinter as tk
# preparartion du dico
lesMots = ruz.preparationDico("dico.txt")
dico=set(lesMots)

# affichage de l'interface graphique
mot="test"
fenetre= tk.Tk("Ruzzle DIU")
fenetre.geometry("400x300")

# gestion du jeu avec les recherches sur les propositions du joueur
# test de la presence du mot dans le dico puis dans la grille
#gestion du bouton de validation du mot
def validationCallBack(m, dic,resultat) :
    if len(m)==0:
        res="le mot est vide ..."
       
    else:
        print("validation et test du mot") 
        if ruz.estDansDico(m , dic):     # recherche dans dico  !!! ajouter recherche dans la grille
            res="bien"
        else:
            res="mot refusé !"


titrelabel= tk.Label(fenetre, text="Projet Ruzzle - DIU")
motlabel= tk.Label(fenetre, text="Mot:")
proposition = tk.Label(fenetre, text = "bonjour")

res="les tests ici"
resultat = tk.Label(fenetre, text=res)
btnValidation = tk.Button(fenetre, bg = "red",  text= "proposer le mot", command = validationCallBack(proposition.cget("text"),dico, res) )

# generation des cases et affichage de la grille de lettres de Ruzzle
boutons = []
ruz.afficheGrille(ruz.genGrille(boutons, fenetre))

# disposition des elements dans une grille
titrelabel.grid(row=0,column=8)
motlabel.grid(row=1,column=8)
proposition.grid(row=1,column=9)
btnValidation.grid(row=2 , column = 8)
resultat.grid(row = 3 , column= 8)
fenetre.mainloop()







# bilan de la partie , car un jeu à obligatoirement une fin ...
print(ruz.recherche(mot, dico))
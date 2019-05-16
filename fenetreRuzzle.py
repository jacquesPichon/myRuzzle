import tkinter as tk
import libRuzzle as ruz

# affichage de l'interface graphique
mot="test"
fenetre= tk.Tk()
fenetre.title("RUZZLE TEST")
fenetre.geometry("600x300")
label= tk.Label(fenetre, text="Mot:")
affichage= tk.Label(fenetre, text="")
resultat= tk.Label(fenetre,text="Saisir un mot de 4 lettres")


grille= [["A","B","C","D"],["D","E","F","D"],["G","H","I","R"], ["G","H","I","R"]]
grille = ruz.genGrille()

# preparartion du dico 
lesMots = ruz.preparationDico("dico.txt")  # les mots sont prepares et ranges dans une liste
dico = set(lesMots)

score = 0
# affichage du score
labelScore = tk.Label(fenetre, text = "votre score")
champsScore = tk.Label(fenetre, text = score)

listMots=[]

# On définit l'action (paramétrée) qui modifie le texte associé 
# au label "affichage"
def action( c): 
    affichage['text']= affichage['text']+c
    

# On définit la fonction construisant la fonction associée
# Voir plus bas pour la justification (*)
def buildAction( c ):
    print(c)
    return lambda: action(c)
    
    
# Constuction du tableau de boutons
tableauBoutons=[[None] * len(grille)] * len(grille)    # on l'initialise avec None

# On le le remplit avec les boutons
for i in range(0,len(grille)):
    for j in range(0,len(grille[0])):
        print(i,",",j)
        
        tableauBoutons[i][j]= tk.Button(fenetre, width = '5', text= grille[i][j], command= buildAction(grille[i][j]))
        print(tableauBoutons[i][j])
        # placement des boutons sur la fenêtre
        tableauBoutons[i][j].grid(row=i,column=j)

def actionTest():
    global score
    global dico
    global grille
    global listeMots
    mot=affichage.cget('text')
    affichage["text"]=""
    if len(mot)<2:
        print("le mot est trop court")
        resultat.config(text="le mot est trop court ...")
        resultat.config(bg='red')
    else:
        print("on test le mot : {}".format(mot))
        if ruz.estDansDico (mot , dico ) :    #champScore
            resultat.config(bg='green', fg='white', text="mot validé")
            score= score+len(mot)
            listMots.append(mot)
            print(listMots)
        else:
            resultat.config(bg='red', fg='white', text="mot introuvable, vous perdez 2 pts.")
            score = score-2
        champsScore['text'] = score
            

bouton = tk.Button(fenetre, text= "test", command= actionTest )



# Placement des elements dans la fenêtre
label.grid(row=0,column=len(grille))
affichage.grid(row=0,column=len(grille)+1)
bouton.grid(row=5,column=3)
resultat.grid(row=6, column=4)
labelScore.grid(row= 12, column = 6)
champsScore.grid(row= 12, column = 7)
# ouverture de la fenêtre
fenetre.mainloop()



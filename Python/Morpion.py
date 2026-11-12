def afficher_grille(grille):
   
    for ligne in grille:
        for case in ligne :
            if(case == ""):
                print(".", end = " ")
            else : 
                print(case, end = " ")
        print()

def changement(ligne, colone, grille,symbole):
    #ici on chope la lignepuis la colone entré par le joueur ratarcher a son symbole, apres on y change l'element de la grille au coordonés indiqué
    grille[ligne][colone] = symbole

def reponseLignes():
    while True :
        ligne = int(input("quelle ligne (0,1,2) : "))
        if ligne <= 2 and ligne >= 0:
            return ligne
        print("entrez une valeur correcte")

def reponseCol():
    ligne = int(input("quelle colone (0,1,2) : "))
    if ligne <= 2:
        return ligne
    else:
        return "veulliez entrez une colone correcte"

def victoire(grille, joueur):
    
grille = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]
    
joueur = "X"
for tour in range(9):
    print()
    print("c'est a ", joueur, " de jouer !")
    reponseLignes()   
    reponseCol ()
    changement(reponseLignes, reponseCol, grille, joueur)
    afficher_grille(grille)

    #changemùeent de joeuur ici on switch en perma
    if joueur == "X":
        joueur = "O"
    else : 
        joueur = "X"


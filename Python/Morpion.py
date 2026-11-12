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
    while True:
        ligne = int(input("quelle colone (0,1,2) : "))
        if ligne <= 2 and ligne >=0:
            return ligne
        print("entrez une valeur correcte pour la colone")

def victoire(grille, joueur):
    for ligne in grille:
        if ligne[0] == joueur and ligne[1] == joueur and ligne[2] == joueur:
            return True
    for colone in range(3):
        if grille[0][colone] == joueur and grille[1][colone] == joueur and grille[2][colone] == joueur:
            return True
    
    return False
    
grille = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]
    
joueur = "X"
for tour in range(9):
    print()
    print("c'est a ", joueur, " de jouer !")
    lignes = reponseLignes()   
    colone = reponseCol ()
    changement(lignes, colone, grille, joueur)
    afficher_grille(grille)

    #changemùeent de joeuur ici on switch en perma
    if joueur == "X":
        joueur = "O"
    else : 
        joueur = "X"


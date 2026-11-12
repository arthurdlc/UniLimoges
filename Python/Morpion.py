def afficher_grille(grille):
   
    for ligne in grille:
        for case in ligne :
            if(case == ""):
                print(".", end = " ")
            else : 
                print(case, end = " ")
        print()
reponseLignes = int(input("quelle ligne (0,1,2) : "))
reponseCol = int(input("quelle colone (0,1,2) : "))

def changement(ligne, colone, grille,symbole):
    grille[ligne][colone] = symbole
    
grille = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]
changement(reponseLignes,reponseCol,grille)
afficher_grille(grille)
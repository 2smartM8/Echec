# Creation du tableau
tableau = [["_" for j in range(8)] for i in range(8)]

# Fonction qui permet de afficher le tableau
def afficheTableau(tableau):
        for ligne in tableau:
            print (ligne)
            

# Listes des pieces blanches et noires 
piecesB = ["T","C","F","D","R","F","C","T","P"]
piecesN = ["t","c","f","d","r","f","c","t","p"]

# Fonction pour placer les piecces a leurs endroit
def placerPieces(tableau, piecesB):
    for i in range(8):
        tableau[-1][i] = piecesB[i]
        tableau[-2][i] = piecesB[-1]
        tableau[1][i] = piecesB[-1]
        tableau[0][i] = piecesB[i]
    afficheTableau(tableau)

# Fonction pour faire deplacer les pieces 
def deplacement(tableau):
    
placerPieces(tableau,piecesB)
        

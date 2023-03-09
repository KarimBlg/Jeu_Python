import random

class Joueur:
    def __init__(self, position):
        self.position = position
    
    def se_deplacer(self, direction):
        if direction == "haut":
            self.position[0] -= 1
        elif direction == "bas":
            self.position[0] += 1
        elif direction == "gauche":
            self.position[1] -= 1
        elif direction == "droite":
            self.position[1] += 1
    
class Labyrinthe:
    def __init__(self, taille):
        self.taille = taille
        self.sortie = [taille-1, taille-1]
        self.joueur = Joueur([0, 0])
        self.grille = []
        for i in range(taille):
            ligne = []
            for j in range(taille):
                if i == 0 and j == 0:
                    ligne.append("D")  # Point de départ
                elif i == taille-1 and j == taille-1:
                    ligne.append("S")  # Sortie
                else:
                    ligne.append(".")  # Chemin vide
            self.grille.append(ligne)
    
    def afficher(self):
        for ligne in self.grille:
            print(" ".join(ligne))
    
    def generer_obstacles(self, nombre):
        for i in range(nombre):
            x = random.randint(0, self.taille-1)
            y = random.randint(0, self.taille-1)
            if self.grille[x][y] == ".":
                self.grille[x][y] = "#"
    
    def est_sortie(self):
        return self.joueur.position == self.sortie
    
    def deplacer_joueur(self, direction):
        x, y = self.joueur.position
        if direction == "haut" and x > 0 and self.grille[x-1][y] != "#":
            self.joueur.se_deplacer(direction)
        elif direction == "bas" and x < self.taille-1 and self.grille[x+1][y] != "#":
            self.joueur.se_deplacer(direction)
        elif direction == "gauche" and y > 0 and self.grille[x][y-1] != "#":
            self.joueur.se_deplacer(direction)
        elif direction == "droite" and y < self.taille-1 and self.grille[x][y+1] != "#":
            self.joueur.se_deplacer(direction)

# Initialisation du labyrinthe
labyrinthe = Labyrinthe(10)
labyrinthe.generer_obstacles(15)

# Boucle principale du jeu
while not labyrinthe.est_sortie():
    labyrinthe.afficher()
    direction = input("Choisissez une direction (haut/bas/gauche/droite) : ")
    labyrinthe.deplacer_joueur(direction)

print("Félicitations, vous avez trouvé la sortie !")

import heapq
from collections import defaultdict

class AB:
    def __init__(self, racine = [], gauche = None, droite = None):
        self.racine = racine
        self.gauche = gauche
        self.droite = droite

# Getters
    def get_racine(self):
        return self.racine
    
    def get_gauche(self):
        return self.gauche
    
    def get_droite(self):
        return self.droite
    
# Setters
    def set_racine(self, racine):
        self.racine = racine

    def set_gauche(self, gauche):
        self.gauche = gauche

    def set_droite(self, droite):
        self.droite = droite

# Cette fonction permet de savoir si l'arbre est vide ou non
    def estVide(self):
        if self.racine == []:
            return True
        else:
            return False

# Cette fonction permet d'afficher l'arbre
    def display(self):
        print(self)


    def __str__ (self):
        return "(racine>" + str(self.racine) + " gauche>" + str(self.gauche) + " droite>" + str(self.droite) + ")"

# Cette fonction permet de calculer la taille de l'arbre
    def taille(self):
        taille_gauche = 0
        taille_droite = 0

        if self.estVide():
            return 0
        else:
            if isinstance(self.gauche, AB):
                taille_gauche = self.gauche.taille()
                
            if isinstance(self.droite, AB):
                taille_droite = self.droite.taille()

        taille = 1 + taille_gauche + taille_droite
        return taille

# Cette fonction permet de parcourir l'arbre en prefixe
    def prefixe(self):
        if self.racine is None:
            return
        else:
            print(self.racine)
            if isinstance(self.gauche, AB):
                self.gauche.prefixe()
            if isinstance(self.droite, AB):
                self.droite.prefixe()
    
# Cette fonction permet de parcourir l'arbre en infixe
    def infixe(self):
        if self.racine is None:
            return
        else:
            if isinstance(self.gauche, AB):
                self.gauche.infixe()
            print(self.racine)
            if isinstance(self.droite, AB):
                self.droite.infixe()

# Cette fonction permet de parcourir l'arbre en postfixe
    def postfixe(self):
        if self.racine is None:
            return
        else:
            if isinstance(self.gauche, AB):
                self.gauche.postfixe()
            if isinstance(self.droite, AB):
                self.droite.postfixe()
            print(self.racine)

# Cette fonction permet de calculer la hauteur de l'arbre
    def hauteur(self):
        if self.estVide():
            return -1
        else:
            gauche = self.gauche.hauteur() if self.gauche is not None else -1
            droite = self.droite.hauteur() if self.droite is not None else -1
            return 1 + max(gauche,droite)

# Cette fonction permet de savoir si l'arbre est un ABR ou non 
    def ABR(self):
        if self.estVide():
            return True
        else:
            if self.gauche is not None:
                if self.gauche.racine > self.racine:
                    self.gauche.ABR()
                    return False
                if self.droite.racine < self.racine:
                    self.droite.ABR()
                    return False
            if self.droite is not None:
                if self.droite.racine < self.racine:
                    self.droite.ABR()
                    return False
                if self.droite.racine < self.racine:
                    self.droite.ABR()
                    return False
            return True

# Cette fonction permet de savoir si l'arbre est équilibré ou non
    def estEquilibre(self):
        if self.estVide():
            return True
        else:
            delta = 0
            gauche = self.gauche.hauteur() if self.gauche is not None else -1
            droite = self.droite.hauteur() if self.droite is not None else -1
            delta = gauche - droite
            if delta > 1 or delta < -1:
                return False
            else:
                gauche = self.gauche.estEquilibre() if self.gauche is not None else True
                droite = self.droite.estEquilibre() if self.droite is not None else True
                return True and gauche and droite
    
    
    
# 3
A1 = AB()
print(A1.estVide())

# # 4
A2 = AB([5])
print(A2.estVide())

# # 5
A3 = AB([3])

# # 6
A2.set_gauche(A3)
print(A2.__str__())
# # 7
Soussousarbre = AB([12], AB([11]), AB([13]))
SousArbre = AB([5], AB([3]), AB([8]))
Atest = AB([10], SousArbre, Soussousarbre)
Atest.estVide()

# 8 - 9
print(Atest.taille())

# 10
print(Atest.__str__())
print(Atest.taille())

# 11
Atest.prefixe()

# 13
Atest.infixe()
Atest.postfixe()   

# 14
print(Atest.hauteur())

# 15
print(Atest.ABR())

# 16
print(Atest.estEquilibre())


# Cette fonction permet de construire un arbre binaire à partir d'un parcours selon le type donné en 2e argument
def construire_arbre(parcours, type):
    if type == "infixe":
        return construire_arbre_infixe(parcours)
    elif type == "prefixe":
        return construire_arbre_prefixe(parcours)
    elif type == "postfixe":
        return construire_arbre_postfixe(parcours)
    else:
        return ("Type de parcours inconnu")
    
def construire_arbre_infixe(parcours):
    if not parcours:
        return AB()
    else:
        milieu = len(parcours) // 2
        racine = parcours[milieu]
        gauche = construire_arbre_infixe(parcours[:milieu])
        droite = construire_arbre_infixe(parcours[milieu+1:])
        return AB(racine, gauche, droite)

def construire_arbre_prefixe(parcours):
    if not parcours:
        return AB()
    else:
        racine = parcours[0]
        index_pivot = 1
        while index_pivot < len(parcours) and parcours[index_pivot] < racine:
            index_pivot += 1
        gauche = construire_arbre_prefixe(parcours[1:index_pivot])
        droite = construire_arbre_prefixe(parcours[index_pivot:])
        return AB(racine, gauche, droite)

def construire_arbre_postfixe(parcours):
    if not parcours:
        return AB()
    else:
        racine = parcours[-1]
        index_pivot = len(parcours) - 2
        while index_pivot >= 0 and parcours[index_pivot] > racine:
            index_pivot -= 1
        gauche = construire_arbre_postfixe(parcours[:index_pivot+1])
        droite = construire_arbre_postfixe(parcours[index_pivot+1:-1])
        return AB(racine, gauche, droite)


print(construire_arbre([3,8,5,11,13,12,10], "postfixe"))
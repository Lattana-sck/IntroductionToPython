# Breakpoint: 1

# Ex 1
temps = 6.893
distance = 19.7

vitesse = distance / temps
print("la vitesse est de " + str(round(vitesse, 1)) + " km/h")

# Ex 2
print('Bonjour, quel est votre nom ?')
nom = str(input())
print('Bonjour ' + nom + ', quel âge avez-vous ?')
age = int(input())
print("Bonjour " + nom + ", vous avez " + str(age) + " ans.")

# Ex 3
float = float(input("Entrez un float: "))
if float > 0 :
    print("La racine = " + str(float ** 0.5) + "")
elif float == 0 :
    print("La racine = " + str(float ** 0.5) + "")
else :
    print("Le nombre est négatif")

# Ex 4
mot1 = input("Entrez un mot: ")
mot2 = input("Entrez un autre mot: ")

if mot1 < mot2:
    print("Le mot le plus petit est:", mot1)
elif mot1 > mot2:
    print("Le mot le plus petit est:", mot2)
else:
    print("Les deux mots sont identiques.")

# Ex 5
pSeuil = 2.3
vSeuil = 7.41
p = float(input("Entrez la pression: "))
v = float(input("Entrez le volume: "))

if v > vSeuil and p > pSeuil:
    if v > vSeuil and p > pSeuil:
        print("Arrêt immédiat")
elif p > pSeuil:
    print("Veuillez augmenter le volume de l'enceinte !")
elif v > vSeuil:
    print("Veuillez diminuer le volume de l'enceinte !")
else:
    print("Tout va bien")

# Breakpoint: 2

# Ex 6
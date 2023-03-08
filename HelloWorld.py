import re
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
string = str(input("Entrez une chaîne de caractères: "))
if re.search("@.*com$", string) :
    print("L'adresse mail est valide")
else:
    print("L'adresse mail est invalide")

# Ex 7
for i in range(0, 10):
  print("hello")

# Ex 8
mot = "salut"
for i in range(0, len(mot)):
    print(mot[i])

# Ex 9
a = 0
b = 10

while a < b:
    print(a)
    a = a + 1

# Ex 10

b = 10

while b > 0:
    if b % 2 == 1:
        print(str(b) + " est imppair")
    b -= 1

# Ex 11

saisie = int(input("Entrez un nombre: "))
if saisie >= 1 and saisie <= 10:
    print("Le nombre est compris entre 1 et 10")
else:
    print("Le nombre est en dehors de l'intervalle")

# Ex 12

chainedecaractere = "Bonjour"
liste = [1, 2, 3, 4, 5]

for i in range(0, len(chainedecaractere)):
    print(chainedecaractere[i])

for i in range(0, len(liste)):
    print(liste[i])

for i in range(1, 15):
    if i % 3 == 0:
        print(i)

# Ex 13

n = int(input("Indiquez combien de nombre pair voulez vous ? "))
 
for i in range(n):
    print(2*i)

i=0
while i < n:
    print(2*i)
    i += 1

# Breakpoint : 3

# Ex 15

liste = [17, 38, 10, 25, 72]
liste.sort()
print(liste)

liste.append(12)
print(liste)

liste.sort(reverse=True)
print(liste)

liste.remove(38)
print(liste)

print(liste[1:2])
print(liste[0:1])
print(liste[3:])

# Ex 16

chaine = "Bonjour"
inverse = chaine[::-1]
print(inverse)

# Ex 17

mot = "kayak"
if mot == mot[::-1]:
    print("Le mot est un palindrome")
else:
    print("Le mot n'est pas un palindrome")

# Ex 18

email = str(input("Entrez une adresse mail: "))
if "@" in email and "." in email:
    domaine = email.split(".")[-1]
    if len(domaine) <= 3:
        print("Le domaine est valide")
    else:
        print("Le domaine est invalide")
else:
    print("L'adresse mail est invalide")

# Ex 19

truc = []
machin = [0.0] * 5

print(truc)
print(machin)

# Ex 20

for i in range(0,4):
    print(i)

for i in range(4,8):
    print(i)

for i in range(2,9):
    if(i % 2 == 0):
        print(i)

chose = [0, 1, 2, 3, 4, 5]

if 2 in chose:
    print("2 appartient à chose.")
else:
    print("2 n'appartient pas à chose.")

if 5 in chose:
    print("5 appartient à chose.")
else:
    print("5 n'appartient pas à chose.")

# Breakpoint : 4

# Ex 21

x = int(input("Entrez un nombre : "))

with open("data.txt", "w") as f:
    for i in range(x):
        s = input("Entrez une chaîne de caractères : ")
        f.write(s + "\n")

# Ex 22

with open("data.txt", "r") as file:
    for line in file:
        line = line.strip()  # supprimer les espaces au début et à la fin de la ligne
        if "@" in line and line.endswith(".com"):
            print(line + " est un email.")
        else:
            print(line + " n'est pas un email.")

# Ex 23

def compterMots(chaine):
    # Convertir la chaîne en liste de mots
    mots = chaine.split()

    # Initialiser un dictionnaire vide pour stocker les fréquences de chaque mot
    freq = {}

    # Boucler sur chaque mot et compter sa fréquence
    for mot in mots:
        if mot in freq:
            freq[mot] += 1
        else:
            freq[mot] = 1

    # Renvoyer le dictionnaire de fréquences
    return freq

# Ex 24

def cube(x):
    return x ** 3

def volumeSphere(r):
    volume = (4/3) * cube(r) * 3.14
    return volume

rayon = int(input("Entrez le rayon de la sphère: "))
volume = volumeSphere(rayon)
print("Le volume de la sphère de rayon", rayon, "est de", volume)

# Ex 25

def somme(a, b, c):
    return a + b + c

nombres = (2, 4, 6)
resultat = somme(*nombres)
print("La somme de", nombres, "est égale à", resultat)


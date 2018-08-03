#depuis la bibliotheque random, on importa la formule (fontcfion) randrange():
#qui pêrmet de recuperer un chiffre aleatoire
from random import randrange

#-----------------------------
#exemple 1

#vous creer une variable phrase qui contient la chaine de charactere "bonjour a tous"
phrase = "Bonjour a tous !"

#la boucle for, permet de parcourir la phrase en recuperant chaque
#charctere et la stoque termporairement dans lettre
for lettre in phrase:
    #on compare la lettre recuperee avec la liste des voyelles
    if lettre in "aeiou":
        print(lettre)



#-----------------------------
#exemple 2

#input permet de demander de taper quelque chose au clavier
#ici, un entier : (int)
#on stoque la valeur tapee dans table
table = int(input("tapez un chiffre : "))
multiple = 1

#tant que la variable multiple est plus petite OU egale a 10
while multiple <= 10:
    #on affiche la multiplication de la table choisie avec son multiplicateur
    print (table * multiple)
    #on augmente a chaque tour la variable multiple de 1
    multiple = multiple + 1



#-----------------------------
#exemple 3

#on demande a randrange de nous donner un chiffre aleatoire compris 
#entre 0 et 99
chiffre = random.randrange(100)

#on cree une variable booleanne qui vaut FAUX 
trouver = False

#tant que trouver = FAUX, on continue la boucle
while trouver == False :
    a = int(input("Entrez un chiffre : "))
    if a < chiffre:
        print("le chiffre est plus grand")
    elif a > chiffre:
        print("le chiffre est plus petit")
    else:
        print("Bravo !")
        #si on a trouve, il faut penser a changer la valeur de
        #notre "Flag" trouver qui passe a VRAI
        trouver = True

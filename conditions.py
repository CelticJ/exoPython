#on cree une variable qui est egale a 5
boite = 5

#si la variable boite est plus grande que 10
if boite > 10 :
    #on affiche plus grand
    print("plus grand")
#sinon, si la varible boite est plus petite que 10
elif boite < 10 :
    #on affiche plus petit
    print("plus petit")
#autrement, la varibale est egale exactement a 10    
else:
    #on affiche "egal"
    print("egal")


#------------------
#exemple 2

#on garde le reste de la division de 52 par 2 (le modulo)
#et on stoque le resultat dans la variable boite
boite = 52 % 2

#si le contenu de la variable boite est egal a 0
#ATTENTION, double = quand on compare 2 elements
if boite == 0 :

    print("52 est un chiffre pair")
"""

@name affichage_tableau.py
@author Aélion
@version 1.0.0

"""

"""
 Fonction getLowerOf donne plus petite valeur de 2 valeurs
 @param
 @return
"""

def getLowerOf(firstVal, secondVal):
    if firstVal < secondVal:
        return firstVal
    else :
        return secondVal


"""
Fonction getGreaterOf donne plus grande valeur de 2 valeurs
@param
@return
"""
def getGreaterOf(firstVal, secondVal):
    if firstVal > secondVal:
        return firstVal
    else :
        return secondVal

"""
Fonction qui compare
@param
@return
"""

def compare(firstVal, secondVal, desc=True):
    if(desc):
        return getLowerOf(firstVal, secondVal)
    return getGreaterOf(firstVal, secondVal)



# Déclaration du tableau de démonstration
monTableau = [125,12,5,7,-15]

for i in range(3):
    indiceNouveau = i*2
    print(monTableau[indiceNouveau]*2)

# Simple loop 
for i, val in enumerate(monTableau):
    print(monTableau[i])

# More complex loop with conditions
for i, val in enumerate(monTableau):
    if i % 2 == 0:
        print(monTableau[i]*2)


"""
max function
@param le tableau duquel je veux extraire la plus grande valeur
@return la plus grand valeur
"""
def max(anArray):
    valeurMaximum = anArray[0]

    for val in anArray[1:]:
        if val > valeurMaximum:
            valeurMaximum = val
    return valeurMaximum

"""
indice de la valeur maximale
@param tableau
@return indice de la plus grande valeur
"""
def indiceMax(anArray):
    valeurMaximum = anArray[0]
    indiceMaximum = 0
    compteur = 0

    for val in anArray[1:]:
        compteur = compteur + 1
        if val > valeurMaximum:
            valeurMaximum = val
            indiceMaximum = compteur

    return indiceMaximum


"""
min function
@param tableau
@return plus petite valeur
"""
def min(anArray):
    valeurMinimum = anArray[0]

    for val in anArray[1:]:
        if val < valeurMinimum:
            valeurMinimum = val

    return valeurMinimum

"""
indice de la valeur minimale
@param tableau
@return indice de la plus petite valeur
"""
def indiceMin(anArray):
    valeurMinimum = anArray[0]
    indiceMinimum = 0
    compteur = 0

    for val in anArray[1:]:
        compteur = compteur + 1
        if val < valeurMinimum:
            valeurMinimum = val
            indiceMinimum = compteur 

    return indiceMinimum


"""
average function
@param
@return
"""
def average(anArray):
    total = 0
    for val in anArray[0:]:
        total = total + val
    print("total:",total)
    moyenne = total / len(anArray)
    return moyenne

"""
factorielle function
@param
@return
"""
def fact(anArray):
    factoriel = 1
    for val in anArray[0:]:
        factoriel = factoriel * val
    print("fact:",factoriel)
    return factoriel


print("La plus petite valeur est ", min(monTableau),"c'est la",indiceMin(monTableau) + 1,"ème valeur.")
print("La plus grande valeur est ", max(monTableau), "c'est la",indiceMax(monTableau) + 1,"ème valeur.")
print("la moyenne des valeurs du tableau est de ", average(monTableau))
print("la factorielle des valeurs du tableau est de ",fact(monTableau))

"""
function classer ordre chronologique
@param tableau avec les valeurs que l'on veut classer dans l'ordre chronologique
@return autre tableau avec valeurs dans le bon ordre
"""




"""def croissant(anArray):
    for i in range(len(anArray)):
        tableauOrdre [i] = 0
    tableauOrdre[0] = min(anArray)
    for i in """

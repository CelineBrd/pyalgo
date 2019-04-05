"""
@name caisse_enregistreuse.py
@author Aélion
@version 0.0.1
une caisse enregistreuse 
"""
# somme à payer
aPayer = 500
# somme donné par le client
donne = 458
# somme rendue par la caisse enregistreuse
rendu = aPayer - donne

# décomposition de la somme rendu en nombres de billets et de pièces
billet100 = rendu // 100
reste100 = rendu % 100
billet50 = reste100 // 50
reste50 = reste100 % 50
billet20 = reste50 // 20
reste20 = reste50 % 20
billet10 = reste20 // 10
reste10 = reste20 % 10
billet5 = reste10 // 5
reste5 = reste10 % 5
piece2 = reste5 // 2
piece1 = reste5 % 2


listeBillet = [billet100,billet50,billet20,billet10,billet5,piece2,piece1]
listeChaine = ["","","","","","",""]
listeMonnaie = [100,50,20,10,5,2,1]


for i in range(5) :
    if listeBillet[i] == 1:
        listeChaine[i]= str(listeBillet[i]) + " billet de " + str(listeMonnaie[i])
    elif listeBillet[i] == 0:
        listeChaine[i] = ""
    else :
        listeChaine[i]= str(listeBillet[i]) + " billets de " + str(listeMonnaie[i])

for i in range(5,7):
    if listeBillet[i] == 1:
        listeChaine[i]= str(listeBillet[i]) + " pièce de " + str(listeMonnaie[i])
    elif listeBillet[i] == 0:
        listeChaine[i] = ""
    else :
        listeChaine[i]= str(listeBillet[i]) + " pièces de " + str(listeMonnaie[i])

#
# Affichage de ce que la caisse enregistreuse doit rendre
#
    
print("Je vous rend :")
for i in range(7):
    if listeChaine[i] != "":
        print(listeChaine[i])

print("Merci")
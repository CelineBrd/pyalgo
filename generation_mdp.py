"""
Génération de mot de passe
@name generation_mdp.py
@author aelion
@version 1.0.0
"""
import random
alphabetMin = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabetMaj = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
chiffres = ["0","1","2","3","4","5","6","7","8","9"]
ponctuation = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]


tailleMdp = random.randint(8,12)


nbMajMax = tailleMdp - 2
nbMaj = random.randint(1,nbMajMax)
nbChiffresMax = tailleMdp-nbMaj-1
nbChiffres = random.randint(1,nbChiffresMax)
nbPonctuationMax = tailleMdp-nbMaj-nbChiffres
nbPonctuation = random.randint(1,nbPonctuationMax)
nbMin = tailleMdp-nbMaj-nbChiffres-nbPonctuation

print("tailleMdp",tailleMdp)
print("nbMaj",nbMaj)
print("nbChiffres",nbChiffres)
print("nbPonctu",nbPonctuation)
print("nbMin",nbMin)

passwordDesordre = [""] * tailleMdp
password = [""] * tailleMdp


for i in range(nbMaj):
    passwordDesordre[i] = alphabetMaj[random.randint(0,25)]

for i in range(nbChiffres):
    passwordDesordre[i+nbMaj] = chiffres[random.randint(0,9)]

for i in range(nbPonctuation):
    passwordDesordre[i+nbMaj+nbChiffres] = ponctuation[random.randint(0,14)]

if nbMin != 0:
    for i in range(nbMin):
        passwordDesordre[i+nbMaj+nbChiffres+nbPonctuation] = alphabetMin[random.randint(0,25)]
print(passwordDesordre)
random.shuffle(passwordDesordre)
print(passwordDesordre)

print("Génération d'un mot de passe:")
for i,value in enumerate(passwordDesordre):
    print(value, end = '')

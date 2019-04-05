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
theMaj = alphabetMaj[random.randint(0,25)]
theDigit = chiffres[random.randint(0,9)]
theDot = ponctuation[random.randint(0,14)]

password = [theMaj, theDigit, theDot]

while len(password) < tailleMdp:

    i = random.randint(0,3)
    tableau = []
    if i == 0:
        tableau = alphabetMaj
    elif i == 1:
        tableau = alphabetMin
    elif i == 2:
        tableau = chiffres
    elif i == 3:
        tableau = ponctuation

    password.append(tableau[random.randint(0,len(tableau)-1)])

print("le mot de passe initial \n",password)
print("Mon mot de passe fait ",len(password),"caractères.")

passwordFin = [""] * len(password)

while len(password) > 0:
    for j in range(len(password)):
        print(j)
        i = random.randint(0,len(password)-1)
        passwordFin[j] = password[i]
        password.remove(password[i])
        print("Dans la boucle, mot de passe initial \n",password)
        print("Dans la boucle, mot de passe final \n",passwordFin)


print("Génération d'un mot de passe:")
for i,value in enumerate(passwordFin):
    print(value, end = '')
import json
import random
import string
#import generateur_de_mot_de_passe
#dict_info = json.dump(info)

dict_info = {
    "passwd" : "khaledlea12"
}


#from file yan_generator import fonction_generator
#def passwordGenerator():
    #fonction_generator()
#    psswd_generator = #fonction_generator()
#    return psswd_generator
def passwordGenerator():
    letters = string.ascii_lowercase
    psswd_generator = ( ''.join(random.choice(letters) for i in range(10)) )
    return psswd_generator


def passwdUser():
    password = dict_info.get("passwd")
    return password



def comparaison(i):
#    i = 0
    passwd = passwdUser()
    passwd_genere = passwordGenerator()
    while i < 15 and passwd != passwd_genere:
        if passwd_genere != passwd :
            i += 1
        passwd_genere = passwordGenerator()
    return i



def resultatPasswd():
    nbre_de_tour = comparaison(0)
    print(nbre_de_tour)
    if nbre_de_tour == 15:
        print("Votre mot de passe est sécurisé")
    else:
        print("Votre mot de passe n'est pas sécurisé")

resultatPasswd()






#les inputs doivent être dans le générateur
#psswd doit rester sur cette feuille
#ville -- numéro département

#Comparer le mdp avec les output du générateur de mot de passe
#--> faire une boucle qui dit que le output
#la boucle i = 0 et stopper la boucle si :
#i = 15
#le mdp est safe
# ou
# si le mdp de la personne = mot de passe généré
#le mdp est pas safe


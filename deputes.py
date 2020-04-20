#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:52:40 2020

@author: Théophane Durand
"""
import os
import csv



#On pose des constantes correspondants au intutilés de chaque colone du fichier des deputes
NOM = 0
SEXE = 1
NUM_DEPTMT = 2
NOM_CIRCO	 = 3
NUM_CIRCO	 = 4
GROUPE_SIGLE	= 5 
COMMISSION_PERMANENTE = 6 
FONCTION = 7
SITES_WEB = 8
EMAILS = 9
TWITTER = 10
AUTRES_MANDATS = 11
TEL = 12
ADRESSE_PERMANENCE  = 13
CP_PERMANENCE = 14
VILLE_PERMANENCE = 15
REPERTOIRMAILS = './Mails/'
CSVDEPUTES = './deputes.csv'
MAIL = './mail.txt'
    
if not os.path.exists(CSVDEPUTES):
    raise Exception('Le fichier "deputes.csv" n\'est pas présent dans le dossier. Le traitement n\'est donc pas possible')
    
if not os.path.exists(MAIL):
    raise Exception('Le fichier "mail.txt" n\'est pas présent dans le dossier. Le traitement n\'est donc pas possible')

def csv2tab(file):
    """
        csv2tab prend en entrée l'adresse d'un fichier csv et renvoit un tableau de tableau.
        Traduisant chque ligne du fichier csv en tableau (pour chaque cases)
    """
    tab = []
    with open(file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            tab.append(row)
    return tab

    
def modifMail(depute, mail = MAIL):
    """
        modifMail renvoit une chaine de caractères d'un mail personnélisé pour chaque députés des comissions choisies
        Prend en entrée :   infoDeput : un tableau de tableau avec les données des députés.
                            mail : l'adresse d'un fichier txt remplit selon le formalisme choisit
                            commissionChoisies : un tableau avec les différentes commissions correspondantes aux commissions du tableau infoDeput
        cette fonction ne renvoit rien mais créer un dossier Mail dans lequel sera stoqué tous les documents textes personnalisés avec comme premiere ligne l'adresse email du député en question
    """
    #Ouverture du fichier mail
    f = open(mail, 'r')
    messageMail = f.read() 
       
    #Dictionnaire mettant en relation chemps personnalisés et les données du deputé:
    donnesDeputes = {}
    donnesDeputes['@nom@'] = depute[NOM].replace('É', 'E') #Le É fait bugger tout le programme...
    donnesDeputes['@fonction@'] = depute[FONCTION].lower()
    donnesDeputes['@commission@'] = depute[COMMISSION_PERMANENTE].lower()
    if(depute[SEXE] == 'F'):
        donnesDeputes['@politesse@'] = 'madame'
    elif(depute[SEXE] == 'H'):
        donnesDeputes['@politesse@'] = 'monsieur'
        
    #On remplace les tag par les données des députés
    texteMail = messageMail
    for tag in donnesDeputes.keys():
        texteMail = texteMail.replace(tag, donnesDeputes[tag])
    
    #On s'occupe des mots genrés
    message = texteMail.split("#")
    while(len(message) > 1):
        mot = message[1].split('/')
        if(depute[SEXE] == 'F'):
            message[0] += mot[1]
        elif(depute[SEXE] == 'H'):
            message[0] += mot[0]
        message.pop(1)
        message[0] += message[1]
        message.pop(1)

    return(message[0])
    
def creerFichierMail(chaine, nom):
    """
        creerFichierMail permet de créer un fichier remplit d'une chaine de caractères portant de nom entré en parametre
        Prend en entrée :   chaine : la chaine à écrire dans le fichier
                            nom : le nom du fichier à créer
    """
    newfile = open(nom, 'w')
    newfile.write(chaine)
    newfile.close()
    

#--------------------------------Main----------------------------------------------------------
if __name__ == '__main__': 
    
    #On créer le dossier ou sera stocké tous les mails
    if not os.path.exists(REPERTOIRMAILS):
        os.makedirs(REPERTOIRMAILS)
        
    #On détermine les commissions que l'on souhaite
    commissionChoisies = ['Finances de l’économie générale et du contrôle budgétaire', 'Lois', 'Affaires sociales', 'Affaires économiques']
    
    #On récupère un tableau à partir du fichier csv des députés.
    tabDeputes = csv2tab(CSVDEPUTES)
    
    #On compte le nombre de fichiers créés
    mailsCrees = 0
    
    #On créé un nouveau fichier pour chaque depute
    for depute in tabDeputes:
        if(depute[COMMISSION_PERMANENTE] in commissionChoisies):
            nomDuFichier = "{}mail{}.txt".format(REPERTOIRMAILS, depute[NOM])
            creerFichierMail(modifMail(depute), nomDuFichier)
            mailsCrees += 1
    print("{} mails ont été créé avec succès".format(mailsCrees))
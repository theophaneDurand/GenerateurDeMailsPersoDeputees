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

#On créer le dossier ou sera stocké tous les mails
if not os.path.exists(REPERTOIRMAILS):
    os.makedirs(REPERTOIRMAILS)

def csv2tab(file):
    tab = []
    with open(file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            tab.append(row)
    return tab

def modifMail(infoDeput, mail):
    #Ouverture du fichier mail
    f = open(mail, 'r')
    
    #transformation du fichier mail en tableau de mots
    messageMail = f.read()
    mailsCrees = 0
    #On créé un nouveau fichier pour chaque depute
    for depute in infoDeput:
        if(depute[COMMISSION_PERMANENTE] in commissionChoisies):
            
            #Dictionnaire mettant en relation chemps personnalisés et les données des deputés:
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
                
            message = message[0]
            nomDuNouveaufichierTexte = "{}mail{}.txt".format(REPERTOIRMAILS, depute[NOM])
            newMail = open(nomDuNouveaufichierTexte, 'w')
            newMail.write(message)
            newMail.close()
            mailsCrees +=1
            print("Création du fichier {} réussie".format(nomDuNouveaufichierTexte))
    return(mailsCrees)

#--------------------------------Main----------------------------------------------------------
commissionChoisies = ['Finances de l’économie générale et du contrôle budgétaire', 'Lois', 'Affaires sociales', 'Affaires économiques']
csvDeputes = input('Veuillez entrer le nom du fichier cvs avec les informations des députés svp (avec l\'extension) : ')
mail = input('Veuillez entrer le nom du fichier avec votre mail rédigé et formaté (selon le formatage du README.md) avec l\'extension : ')
tabDeputes = csv2tab(csvDeputes)
print("{} mails ont été créé avec succès".format(modifMail(tabDeputes, mail)))

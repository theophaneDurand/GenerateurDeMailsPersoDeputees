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

commissionChoisies = ['Finances de l’économie générale et du contrôle budgétaire', 'Lois', 'Affaires sociales', 'Affaires économiques']

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
    tabMotsMail = f.read().split(sep = ' ')
    
    #On créé un nouveau fichier pour chaque depute
    for depute in infoDeput:
        if(depute[COMMISSION_PERMANENTE] in commissionChoisies):
            #On boucle sur tous les mots du mails pour modifier ceux à modifier
            message = ''
            for mot in tabMotsMail :
                #modifications a effectuer sur les mots genres
                if(mot[0] == "#" and mot[-1] == "#"):
                    if(depute[SEXE] == 'F'):
                        #on prend la deuxieme ecriture pour le feminin
                        mot = mot.split(sep='/')[1][:-1]
                    elif(depute[SEXE] == 'H'):
                        #on prend la premiere ecriture pour le masculin
                        mot = mot.split(sep='/')[0][1:]
                       
                #On remplace les champs personnalises
                elif(mot[0] == '@' and mot[-1] == '@'):
                    if (mot == '@politesse@'):
                        if (depute[SEXE] == 'F'):
                            mot = mot.replace('@politesse@', 'madame')
                        elif (depute[SEXE] == 'H'):
                            mot = mot.replace('@politesse@', 'monsieur')
                    if (mot == '@nom@'):
                        mot = mot.replace('@nom@', depute[NOM])
                    elif (mot == '@fonction@'):
                        mot = mot.replace('@fonction@', depute[FONCTION].lower())
                    elif (mot == '@commission@'):
                        mot = mot.replace('@commission@', depute[COMMISSION_PERMANENTE].lower())
                message += mot + ' '
            nomDuNouveaufichierTexte = "{}mail{}.txt".format(REPERTOIRMAILS, depute[NOM])
            newMail = open(nomDuNouveaufichierTexte, 'w')
            newMail.write(message)
            newMail.close()


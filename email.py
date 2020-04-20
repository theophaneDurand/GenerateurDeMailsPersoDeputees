#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:44:33 2020

@author: theo
"""

import smtplib
import deputes
import getpass
from random import randint
from time import sleep

paramSMTP = {}
paramSMTP["live.fr"] = ('smtp-mail.outlook.com', 587)
paramSMTP["hotmail.fr"] = ('smtp-mail.outlook.com', 587)
paramSMTP["gmail.com"] = ('smtp.gmail.com', 587)

MAILCLIC = 'contact@lobby-citoyen.org'


def envoiMail(message, objet, serveur, **destinataires):
    """
        envoiMail envoi un email contenant comme message la chaine de carctère passée en parametre, avec l'objet passé en parametre aux adresses passée en parametres.
        Parametres :    message : chaine de caractère contenant le corps du mail
                        objet : chaine de caractères contenant l'objet du mail
                        destinataire. sous le forme de dictionnaire de tableaux d'emails : clés : to, cc, bcc
    """
    fromaddr = serveur.auth_login()
    mail = "From: %s\r\n" % fromaddr + "To: %s\r\n" % ",".join(destinataires['to']) + "Subject: %s\r\n" % objet + "\r\n" + message
    toaddrs = destinataires['to'] + destinataires['bcc']
    serveur.sendmail(fromaddr, toaddrs, mail.encode("utf8"))

def envoiTousLesMails(tabDeputes, commissionChoisies, serveur, objet):

    mailsEnvoyes = 0

    for depute in tabDeputes:
        if(depute[deputes.COMMISSION_PERMANENTE] in commissionChoisies):
            #si le député n'a pas d'adresse email, on passe au suivant
            if(depute[deputes.EMAILS] == ''):
                break
            message = deputes.modifMail(depute)
            envoiMail(message, objet, serveur, to = [depute[deputes.EMAILS].split('|')[0]], bcc = MAILCLIC) #On envoit le mail en copie cachée au lobby citoyen
            mailsEnvoyes += 1
            cooldown = 5 + randint(0,5)
            print("mail envoyé à {}, prochain mail dans {}s, total des mails envoyés : {}.".format(depute[deputes.NOM], cooldown, mailsEnvoyes))
            sleep(cooldown)

    return(mailsEnvoyes)

def connexionServeurSMTP():
    mailUser = input("Veulliez entrer votre adresse e-mail : \n")
    mdpUser = getpass.getpass("Veuillez entrer le mot de passe de votre adresse e-mail (à ne faire que si vous avez vraiment confiance à ce programme.) : \n")

    domaine = mailUser.split('@')[1]

    if (domaine in paramSMTP.keys()):
        SMTP = paramSMTP[domaine][0]
        port = paramSMTP[domaine][1]
    else :
        SMTP = input("Veulliez entrer le nom de votre serveur SMTP (ex : smtp.gmail.com) : \n")
        port = eval(input("Veulliez entrer le port de votre serveur SMTP (ex : 587) : \n"))

    server = smtplib.SMTP(SMTP, port)
    server.ehlo()
    server.starttls()
    server.login(mailUser, mdpUser)

    return(server)

def deconnexionServeurSMTP(server):
    server.quit()


if __name__ == '__main__':

    #On détermine les commissions que l'on souhaite
    commissionChoisies = ['Finances de l’économie générale et du contrôle budgétaire', 'Lois', 'Affaires sociales', 'Affaires économiques']

    objet = input("Veuillez entrer l'objet du mail qui va être envoyé : \n")

    #On récupère un tableau à partir du fichier csv des députés.
    tabDeputes = deputes.csv2tab(deputes.CSVDEPUTES)[1:]

    # On se connecte au serveur SMTP
    serveur = connexionServeurSMTP()

    print('{} mails ont été envoyés'.format(envoiTousLesMails(tabDeputes, commissionChoisies, serveur, objet)))

    #On se déconnecte du serveur SMTP
    deconnexionServeurSMTP(serveur)

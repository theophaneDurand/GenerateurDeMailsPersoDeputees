# GenerateurDeMailsPersoDeputees
Script python premettant de générer des mails personnalisés pour les députés. #LobbyingCitoyen

### Fichiers
Le projet est constitué de trois fichiers : 
Le fichier deputes.py qui est le scripte python de mon application.
Un tri des députés est fait en fonction des commission que vous souhaitez. (voir ligne 36 du code)

Le fichier fichier_deputes_commissions.csv ([source : voxpublic.org](https://www.voxpublic.org/IMG/csv/fichier_deputes_commissions.csv))

Le fichier mail.txt qui est le contenu du mail à envoyer

Le script va automatiquement créer un dossier *Mails* à l'emplacement où vous l'executez dans lequel sera stocké les fichiers avec les emails personnélisés (avec comme nom *mailNOMDUDEPUTÉ.txt*
> ex : mailAdrien Quatennens.txt

### fichier mail.txt
Le programme prends en entrée un fichier mails.txt qui doit suivre un certain formalisme.

Les députés pouvant être des hommes ou des femmes, les mots genrés doivent être écrit sous cette forme : 
#masculin/feminin#
> ex : #député/députée#

Les champs personnalisés sont pour l'instant au nombre de 4 : 
@politesse@ qui donnera "madame", si c'est une députée ou "monsieur", si c'est un député.
@nom@ qui sera remplacé par le nom du député
@fonction@ qui sera remplacé par la fonction su député dans sa commission permanante
@commission@ qui sera remplacé par le nom de sa commission permanante.


### Limites de ce srcipt : 
À ce jour, le script ne peux pas prendre en charge des commissions avec différents déterminants.
> ex : la commission **des** affaires étrangères ou bien la commision **de la** Défense nationale et forces armées

## Utilisation du script
Pour utiliser ce script, téléchargez tous les fichiers sur votre ordinateur dans un même dossier.
Rendez le fichier deputes.py executable (sur ubuntu : clic droit / propiété / Permission / "Allow ewecuting file as program")
POUR UBUNUTU : dans votre dossier : faites clic droit "ouvrir un terminal ici" puis écrivez "./deputes.py"
Répondez aux deux question :
entrer le nom du fichier des données des députés (le fichier csv) avec l'extension

> ex : deputes.csv (par defaut)

entrer le nom du fichier mail (le fichier avec votre mail rédigé dans le bon formalisme) avec l'extension

> ex : mail.txt (par defaut)

Si vous avez entré les bons nom de fichers, vos fichiers txt pour chaque mails sont créés dans le dossier Mails


Si vous êtes sur windows j'ai pas testé mais voici un site qui explique comment executer un script python sur windows : 

[http://www.ordinateur.cc/programmation/Programmation-Python/93856.html](http://www.ordinateur.cc/programmation/Programmation-Python/93856.html)

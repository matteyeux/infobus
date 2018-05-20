# SYSTEME  INFOBUS

EPREUVE E5.2

## Contexte:

La RATP a mis en place un système de suivi du parcours des BUS dans la Région Parisienne. Les Bus sont équipés de capteurs GPS et les coordonnés GPS sont transmises au fur et à mesure sont transmises au centre de supervision et sont stockées dans des tables d'un Système de Gestion de Bases de Données Relationnelles MYSQL.

Il existe une table de référence des parcours qui contientles trajets des lignes de BUS. Les candidats travailleront qu'avec cette table.

Cette table s'appelle parcours et contient :

- `numpar` : le numéro du parcours par exemple PC3 quicorrespond au trajet de Bus Petite Ceinture 3
- `numpt` : le numero d'un point sur un parcours identifié de 1(premier point du parcours) à N (dernier point du parcours, par exemple 24 pourla ligne PC3),
- `lati` : la coordonnée en latitude, par exemple 48.898707 pourle point 6 de la ligne PC3,
- `longi` : la coordonnée en longitude, par exemple  2.366563 pour le point 6 de la ligne PC3,
- `alt` : l'altitude du point (pour l'instant l'altitude n'estpas gérée et on a toujours 0),
- `nompt` : le nom du point (ce nom de point peut apparaîtredans plusieurs parcours), par exemple 1 Place General Koen pour le point 22 de la ligne PC3 (une adresse précise ou le nom d'une station de métro).
- `despt` : la description du point ou un commentaire, parexemple come(nom de magasin) pour le point 22 de la ligne PC3.



 ## PARTIE  MYSQL.

Après avoir installé **MYSQL** , vous pouvez mettre en place la démo en lancant les 2 scripts : 

 `crtparcours2.sql`  qui sert à créer la table parcours et  `insPC3SQL.sql`  qui sert à insérer les lignes du parcours dela ligne PC3 dans la table parcours.

 Voici les commande correspondantes :

```bash
$ mysql < crtparcours2.sql
$ mysql < insPC3SQL.sql 
```


Pour vérifier le chargement de la table parcours :

Dans une fenêtre terminal :

```mysql
$ mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.1.56 Source distribution
Copyright (c) 2000, 2010, Oracle and/or its affiliates. Allrights reserved.
This software comes with ABSOLUTELY NO WARRANTY. This isfree software, 
and you are welcome to modify and redistribute it under theGPL v2 license
Type 'help;' or '\h' for help. Type '\c' to clear thecurrent input statement.

$ mysql> show databases;
+-------------------------+
| Database                |
+-------------------------+
| information_schema      |
| gps                     |
+-------------------------+

$ mysql> use gps;
Reading table information for completion of table and columnnames
You can turn off this feature to get a quicker startup with-A
Database changed
$ mysql> show tables;
$ mysql> select * from parcours;

```

Après on tape des commandes sql.....

Il faut aussi apprendre à gérer les comptes mysql : 

#### Pour créer un compte:

`mysql>CREATE USER 'jeffrey'@'localhost'   IDENTIFIED BY 'new_password' ;`

`mysql>GRANT ALL ON *.*TO 'jeffrey'@'localhost';`

#### Pour se connecter depuis un terminal linux:

`$ mysql -u jeffrey -p`

Voir [DOC](http://dev.mysql.com/doc/refman/5.7/en/create-user.html)

`man mysql`

Il faut apprendre aussi à créer un compte mysql utilisable depuis un poste distant.

A l'aide des coordonnées d'un parcours qu'il convient d'extraire de cette table on peut représenter sur le carte le trajet du parcours du bus en utilisant l'api de google pour tracer un déplacement quand on connait une succession de coordonnées GPS.

 Voici les étapes : 

1)  Extraire les coordonnées d'un parcours de la table et les présenter en utilisant le format de fichier PARCOURS2 dont voici un exemple:

 ``` javascript
  new google.maps.LatLng(48.8800, 2.3730) 
 ,new google.maps.LatLng(48.8800, 2.3740) 
 ,new google.maps.LatLng(48.8800, 2.3730) 
 ,new google.maps.LatLng(48.8810, 2.3740) 
 ,new google.maps.LatLng(48.8810, 2.3760) 
 ,new google.maps.LatLng(48.8800, 2.3790) 
 ,new google.maps.LatLng(48.8800, 2.3810) 
 ,new google.maps.LatLng(48.8810, 2.3820) 
 ,new google.maps.LatLng(48.8800, 2.3840) 
 ,new google.maps.LatLng(48.8800, 2.3850) 

 ```

 Dans cet exemple on a 10 coordonnées. On peut produire ce fichier en utilisant un programme (à écrire), un éditeur de texte ou un outil de manipulation de données tel que awk, directives vi, sed.

 

2) Remplacer dans le fichier PARCOURS1 les coordonnées gps pardéfaut par les coordonnées du premier point de votre parcours.

Voici le fichier PARCOURS1 de référence:

 ```html
<!DOCTYPE html> <html> <head> <metaname="viewport" content="initial-scale=1.0,user-scalable=no"> <meta charset="utf-8"><title>Simple Polylines</title> <style> html, body,#map-canvas { height: 100%; margin: 0px; padding: 0px } </style>scriptsrc="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"</script><script> function initialize() { var mapOptions = { zoom: 16, center: newgoogle.maps.LatLng(48.880465,2.374932), mapTypeId:google.maps.MapTypeId.TERRAIN }; var map = newgoogle.maps.Map(document.getElementById('map-canvas'), mapOptions); varflightPlanCoordinates = [
 ```

Les coordonnées par défaut sont `48.880465,2.374932` , pour le parcours PC3 on mettrait:

`48.897582,2.385684`

3) Assembler les fichiers PARCOURS1 , PARCOURS2 que l'onvient de produire et PARCOURS3

dans un fichier `parcoursPC3.html`.

 Voici le fichier PARCOURS3 de référence:

 ```html
 ]; var flightPath = newgoogle.maps.Polyline({ path: flightPlanCoordinates, geodesic: true,strokeColor: '#FF0000', strokeOpacity: 1.0, strokeWeight: 2 });flightPath.setMap(map); } google.maps.event.addDomListener(window, 'load',initialize); </script> </head> <body> <div id="map-canvas"></div></body> </html>
 ```

Comme on travaille sous Linux (Fedora et Ubuntu), on pourra utiliser la commande shell:

`cat   PARCOURS1   PARCOURS2  PARCOURS3  >   parcoursPC3.html`

4) On visualise le parcours grace à un navigateur tel que Firefox ou Internet Explorer.



## COMPETANCES  ATTENDUES POUR VOTRE EXAMEN.

- Installer, mettre en oeuvre un outils d'administration réseau tel que wireshark ou ethereal.


- Savoir se connecter à mysql et être capable de produire des commandes sql de bases : insert, update, delete, select...


- Savoir créer et gérer des comptes utilisateurs mysql.


- Savoir travailler sous Linux : connaitre les commandes debase et l'éditeur vi.


- Savoir utiliser le langage de programmation de votre choix(c , java...).


- Savoir utiliser et gérer un navigateur.


- Savoir écrire un compte rendu avec libre office.

Au début de l'épreuve , plusieurs questions **INDEPENDANTES** seront écrites au tableau et vous aurez 4 heures maximum pour y répondre.Certaines questions seront faciles et d'autres plus dures. Il n'est pas indispensable de savoir répondre à toutes les questions pour avoir une note correcte. Les professeurs présents seront là pour vous assister, vous aider et vous evaluer.

Il convient de remettre une compte-rendu détaillé etpertinent réalisé avec libre office à la fin de l'épreuve.

## CONSEILS DE PREPARATION.

 Créer vous même un nouveau parcours (choisir une ligne debus et repérer avec google les coordonnées de quelques points sur cette ligne) et l'insérer dans la table parcours.

 Puis produire la page html correspondant à ce parcours etvérifier le résultat avec un navigateur.

Structure de données
====================

Le projet est developpé en Django, par conséquent chacune de nos classes héritant
de `models` génère une table SQL.
De plus nous utilisons SQLite (même en production) pour gérer notre base de données

Structure du projet
-------------------

Le projet comprend 3 applications:
    - oc_lettings_site, qui est l'application parente
    - profiles
    - lettings

Oc Lettings Site
----------------

oc_lettings_site ne possède pas de models, par conséquent aucune table n'est
géré par cette application

Profiles
--------

Profiles ne possède qu'un modele qui est responsable de la creation des profils
des utilisateurs
Spécificité: Nous utilisons le model `User` par défaut de Django car il répond
à tous nos besoins actuellement

Lettings
--------

L'application Lettings possède 2 modèles:
    - Address
    - Letting

Chacun de ces modèle possède donc sa table SQL


Conclusion
----------

Le projet possède actuellement 3 tables SQL (en dehors des tables gérées automatiquement
par Django)
De plus, aucune relation spécifique entre les tables n'est actuellement mise en place

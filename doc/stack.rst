Technologies et langages
========================

Développement
-------------

L'application est developpé grâce au framework web `Django` de python
La base de donnée est relationnelle (SQL) et géré avec SQLite

Qualité du code et monitoring
-----------------------------

Linting
~~~~~~~~

Pour assurer une qualité de code, l'outil de linting `flake8` est utilisé
Vous pouvez retrouver le fichier de config du linter à la racine du projet
dans le fichier `setup.cfg`

Tests
~~~~~

Pour les tests, nous utilisons `pytest`
De même, le fichier de config de pytest se trouve à la racine du projet
dans le fichier `setup.cfg`

Monitoring
~~~~~~~~~~

En ce qui concerne le monitoring, nous utilisons `Sentry`
Grâce au sdk (`sentry-sdk` à installer via pip), l'intégration se fait très
facilement dans `settings.py`

Déploiement
-----------

Pour le déploiement, nous utilisons:
    - Docker pour conteneuriser le projet
    - Render pour l'hébergement
    - GUnicorn (WSGI)
    - Whitenoise pour rendre les fichiers statiques en l'absence de serveur Nginx

CI/CD
-----

Les tâches de linting et de tests, ainsi que le déploiement sont gérés automatiquement
via `GitHub Actions`

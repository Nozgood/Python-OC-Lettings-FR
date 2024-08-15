Déploiement
===========

Fonctionnement
--------------

Le déploiement de l'application se fait grâce à une image Docker
créée et poussée sur Docker Hub au préalable. La tâche de création de l'image Docker ainsi que du déploiement (sur Render) se fait automatiquement via des pipelines sur GitHub Actions, à condition que certains prérequis soient respectés :

- Le push doit être effectué sur la branche `master`.
- La pipeline de test et de lint ne doit pas échouer pour que la conteneurisation se fasse.
- La pipeline de conteneurisation ne doit pas échouer pour que le déploiement se fasse.

Vous retrouverez tous les détails concernant la configuration des pipelines directement dans `./github/workflows/main.yml`.

Credentials
-----------

Afin d'assurer la conteneurisation et le déploiement de l'application en toute sécurité, il faudra configurer 3 `secrets` sur votre compte GitHub :

- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
- `RENDER_DEPLOY_HOOK_P13`

Les deux premiers secrets correspondent à vos identifiants Docker, quant au troisième, il est nécessaire pour pouvoir lancer une requête à Render qui redéploiera automatiquement l'application.

Ainsi, en respectant les prérequis et en ajoutant les secrets, l'application se déploiera automatiquement.

WARNING: Si vous modifiez le nom de domaine de l'application, pensez à l'ajouter dans
la variable d'environnement `ALLOWED_HOSTS`

Note: nous n'avons pas encore mis en place de serveur Nginx pour rendre "proprement" les fichiers statiques.
C'est donc la librairie `Whitenoise` qui nous permets de les renvoyer

La mise en place d'un serveur Nginx reste néanmoins une tâche à garder en tête.
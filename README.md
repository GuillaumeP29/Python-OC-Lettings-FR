## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure
- Compte CircleCI
- Compte DockerHub
- Compte Heroku
- Compte sentry

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- Faites un fork du projet à l'adresse suivante : `https://github.com/GuillaumeP29/Python-OC-Lettings-FR.git` pour l'obtenir sur votre dépôt distant github
- Puis rendez-vous dans votre dossier local où vous souhaitez enregistrer le projet à l'aide de : `cd /path/to/put/project/in`
- Puis cloner le projet : `git clone https://github.com/nom_de_votre_compte_github/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiment en ligne

### Automatisation avec CircleCI
Connectez-vous à CircleCI avec votre dépôt en ligne
Cliquer sur la liste des projets et faites follow sur le projet `Python-OC-Lettings-FR`
Désormais, à chaque push git vers votre dépôt distant, un workflow CircleCI s'exécutera.
Afin que les workflow puissent fonctionner, il vous faut renseigner plusieurs variables d'environnement sur votre compte CircleCI :
|Variable|Description|
|:---- |:-------|
|DJANGO_SECRET_KEY|Clé secrête Django|
|DOCKER_LOGIN|Identifiant de votre compte Dockerhub|
|DOCKER_PASSWORD|Mot de passe / Token de votre compte Dockerhub|
|HEROKU_APP_NAME|Nom de votre projet sur votre compte Heroku|
|HEROKU_TOKEN|Token de votre compte Heroku|
|PROJECT_REPONAME|Nom du dépôt sur votre compte DockerHub|
|SENTRY_DSN|Clé client Sentry|

Il vous faut également créer un fichier .env à la racine de votre projet avec les variables suivantes :
|Variable|Description|
|:---- |:-------|
|DJANGO_SECRET_KEY|Clé secrête Django|
|SENTRY_DSN|Clé client Sentry|

Une fois votre CircleCI ainsi que votre fichié .env configuré, les workflows devraient fonctionner.
Le workflow master fonctionnera lors d'un push de la brance master de votre git. Ce workflow va effectuer trois jobs :
- Le travail de construction de l'image avec installation des dépendances ainsi que de réaliser des tests et du linting pour s'assurer la conformité du code.
- Un travail de publication de l'image docker sur Dockerhub.
- Un travail de déploiement de l'application sur Heroku.
Pour un push sur tout autre branche, le workflow dev se déclanchera et effectuera le premier des 3 jobs présenté juste au dessus.
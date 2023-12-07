# STARTER-BACK

<img src="./doc/assets/genee.png" alt="Image 1" width="150px">

Starter-KIT est un projet de backend développé avec [Python](https://www.python.org/)
et [Flask](https://flask.palletsprojects.com/en/2.3.x/).

## informations globales
Genee est une entreprise Française, les documentations et les commits sont en français
## Dépendances Principales

- [Flask](https://flask.palletsprojects.com/en/2.3.x/) : Une micro framework pour Python.
- [SQLAlchemy](https://www.sqlalchemy.org/) : Un SQL toolkit et ORM pour Python.
- [Marshmallow](https://marshmallow.readthedocs.io/en/stable/) : Une bibliothèque pour la conversion des types de
  données, la validation et la désérialisation.
- [Docker](https://www.docker.com/) : Une plateforme de conteneurisation.
- [Docker Compose](https://docs.docker.com/compose/) : Un outil pour définir et gérer des applications multi-conteneurs
  avec Docker.

## Structure du Projet

```markdown
.
├── app
│   │ └── Contient toute la logique de l'application
│   ├── data
│   │   └── Données (modèles SQLAlchemy) avec leur logique d'accès/modification (routes API, schémas)
│   ├── shared
│   │   └── Logique d'initialisation de l'application, modules partagés (fonctions utilitaires, services)
│   └── main.py
│       └──Point d'entrée de l'application, il démarre le projet
├── doc
│   └── Décisions d'architecture (ARDs), guides, accumulation du savoir
├── envs
│   │ └── Environnements Docker de développement et de production
│   ├── dev
│   ├── prod
│   └── shared
└── scripts
    └── Utilitaires de lancement de l'application et liés aux tests
```
Dans le répertoire `data`, chaque sous-répertoire représente une fonctionnalité (entité ou groupe d'entités reliées) distincte de l'application.
Chaque module peut contenir les modules suivants :

- `controllers` : Définitions des points d'accès API pour le module. C'est ici que les requêtes HTTP sont reçues et dirigées
  vers les fonctions appropriés. Les routes sont regroupées dans un `flask.Blueprint`
- `models` : Modèles de données **SQLAlchemy** associés à la fonctionnalité.
- `schemas` : Schémas qui sont utilisés pour la validation des données entrantes pour le module.
- `services` : Classes utilitaire pour la logique métier associée à la fonctionnalité
- `test`: Contient les tests unitaires liés à la fonctionnalité


## Installation

### Prérequis

Pour exécuter cette application, vous devez avoir Docker et Docker Compose installés sur votre système.

#### Installation de WSL2

Dans Powershell (mode administrateur):

```bash
wsl --install
```

#### Installation de Docker Desktop

L'installation des utilitaires Docker sur Windows se fait grâce à l'application `Docker Desktop` \
Référence: https://docs.docker.com/desktop/install/windows-install/

#### Installation de Docker

1. Mettez à jour l'index du paquet `apt` :
   ```sh
   sudo apt-get update
   ```
2. Installez les paquets permettant à `apt` d'utiliser un dépôt sur HTTPS :
   ```sh
   sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
   ```
3. Ajoutez la clé GPG officielle de Docker :
   ```sh
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   ```
4. Ajoutez le dépôt Docker à vos sources `APT` :
   ```sh
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   ```
5. Mettez à jour l'index du paquet `apt` et installez Docker CE :
   ```sh
   sudo apt-get update
   sudo apt-get install docker-ce
   ```

#### Installation de Docker Compose

1. Téléchargez la version actuelle de Docker Compose :
   ```sh
   sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   ```
2. Appliquez les permissions d'exécution au binaire :
   ```sh
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### Lancement de l'application

Ouvrez une invite de commande ou un terminal.

Accédez au répertoire "dev" situé dans le répertoire "envs" de l'application. Utilisez la commande suivante pour vous
déplacer vers ce répertoire :

```sh
cd /envs/dev
```

Une fois dans le répertoire "dev", exécutez la commande suivante pour démarrer l'application à l'aide de Docker
Compose :

```sh
docker-compose up --build
```

Une fois l'application démarrée, vous pouvez accéder à celle-ci en faisant vos requêtes
à `http://localhost:5001/api/<ROUTE>`.


## Variables d'Environnement

Le projet utilise les variable d'environnement suivantes:

- `DB_USER`: Nom de l'utilisateur BDD
- `DB_PASS`: Mot de passe de l'utilisateur BDD
- `DB_NAME`: Nom de la BDD
- `DB_IP`: Adresse de la BDD
- `MIGRATIONS` : Cette variable détermine si des migrations doivent être effectuées sur la base de données.
  Mettez-la à `1` pour activer les migrations et à `0` pour les désactiver.

Ces variables sont à définir dans un fichier .env, situé à còté du Dockerfile de son environnement (`envs/dev/back/.env` et `envs/prod/back/.env`)\
Comme les .env contiennent souvent des données sensibles, ces fichiers ne sont pas versionnés.\
Pour démarrer le développement, créer un `.env` en copiant le `.env.example` situé au même endroit.

## Lancement de l'application en mode développement

Ouvrez une invite de commande ou un terminal.

```shell
docker-compose -f envs/dev/docker-compose.yml up 
``` 

Ne pas oublier de créer le fichier `.env` à ``envs/dev/back/.env``


## Gestion des dépendances

La gestion des dépendances du projet utilise pip-tools. Cet outil permet, à la manière des package-lock.json sur les
projets Node, de freeze la totalité des dépendances (directes et indirectes) du projet.

pour installer pip-tools :
```shell
pip install pip-tools
```

Les dépendances directes sont spécifiées dans le fichier `pyproject.toml`à la racine du projet.

Les fichiers requirements.txt et requirements-dev.txt situés dans le dossier app ne doivent pas être modifiés manuellement.

En cas de changement de dépendance directe (ajout, modification, suppression) :
- Modifier le fichier pyproject.toml
  - Si la dépendance sert au fonctionnement nominal de l'application
    - Toucher à la section [project] > dependencies
    - Lancer les commandes suivantes :
      ```shell
      pip-compile --upgrade --output-file=app/requirements.txt pyproject.toml
      pip-compile --upgrade --extra=dev --output-file=app/requirements-dev.txt pyproject.toml
      ```
    - Si la dépendance sert uniquement à l'environnement de dev ou de CI
      - Toucher à la section [project.optional-dependencies] > dependencies
      - Lancer la commande suivante :
      ```shell
      pip-compile --upgrade --extra=dev --output-file=app/requirements-dev.txt pyproject.toml 
      ```
La commande pip-compile permet de générer les fichiers requirements.txt et requirements-dev.txt, qui contiennent les dépendances
directes et indirectes et leurs versions figées.



## Configuration de Pycharm

Pycharm est l'IDE Python de jetbrains, pour avoir acces au programme par l'IDE sans erreurs demande quelque 
modification

> **NOTE**: cette configuration a été faites avec la nouvelle UI de Pycharm elle peut ne pas fonctionner sur l'ancienne

### Selection de l'interpreteur python du service docker (permet d'avoir la complétion sans avoir à installer les dépendences sur l'hôte)

- Cliquer sur le bouton de l'interpréteur en bas a droite (là où il y a probablement écrit ``Python 3.X`` avec la
  version de python installée sur l'hôte)
- ``Add New Interpreter``, puis choisir ``On Docker Compose...``
- Dans le champ ``Configuration files`` sélectionner le fichier suivant: ``envs/dev/docker-compose.yml``
- Dans le champ ``Service``, choisir le nom du service qui contient flask, i.e. ``flask`` (le champ devrait avoir des
  valeurs disponibles apres avoir fini l'étape précédente)
- Appuyer sur ``Next``, attendre la fin de commande lancée par l'IDE puis ``Next``
- Appuyer sur ``Create`` dans la dernière fenêtre
- Si en bas a gauche il y a ecrit ``Remote Python 3.X Docker Compose (flask)``, vous avez tout pour commencer !

### Mise en place de la visualisation de la base de donnée

Cliquez sur le logo qui ressemble a une pile de disque sur le coté droit.\
Si vous ne le voyez pas, assurez vous que le plugin ``Database tools and SQL`` soit bien installé.\
Une fois le menu ouvert, cliquez sur ``+ > Data Source > PostgreSQL``\
Mettez les informations suivantes :

- ``port: 5432``
- ``host: localhost``
- ``connect with user and password``
    - user: ``postgres``
    - password: ``postgres``

> **NOTE**: assurez vous bien pendant la connexion avec le docker postgres que le docker soit lancé

Une fois connecté vous verrez a droite ``postgres@localhost`` et plus a droite un petit bouton avec écrit quelque choise
du genre ``1 of 4`` ou bien ``4``, cliquez dessus.\
Cochez ``db_dev`` et ``All schemas`` dans le menu déroulant de ``db_dev``\
Vous pouvez maintenant accéder à toutes vos table dans ``postgres@localhost > db_dev > public > tables``

## Explication des scripts

Les scripts sont situés dans le dossier ``scripts/``
- ``application_restart.sh``
  - Relance l'application tout en effaçant les données de la base de données
  - Fait en sorte que l'application se relance automatiquement apres un Ctrl-C
- ``*.http``
  - Permet de prototyper des requetes pour tester l'application et peupler la base de données facilement exactement comme Postman
  - Pycharm permet de lancer chaque requete du fichier indépendamment (bouton 'Play' a gauche de la requete) ou toutes les requetes (bouton 'Double Play' en haut du fichier)
  - Important : les requêtes doivent être séparées par une ligne avec 3 hashtags ('###')

## Mise en place du format par lint

``black`` permet de formatter le code. Pour le relier à la fonction ``format code`` de l'IDE:

- S'assurer que Black est bien installé : ``python3 -m pip install Black``
- Aller dans ``Settings... > Tools > Black`` et activer ``on code reformat``



## Schemas

Les schemas marshamallow remplissent deux roles en meme temps:
- __Serialisation* / deserialisation__** des donnees
- __Validation__ des donnees

*Sérialisées ->  __Objets Python__\
**Désérialisées ->  __Dictionnaires Python__


### Vocabulaire

Dans marshmallow '__load__' = __deserialize__ et '__dump__' = __serialize__:

__[payload: JSON]__ ----load--->  __[instance: Object]__\
__[payload: JSON]__ <---dump----  __[instance: Object]__

### Definir un schema

- Un schema __marshmallow__ 'pur'

```python3
class Album:
    title: str
    release_date: datetime.date


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
```

- Un schema __marshmallow_sqlalchemy__

```python3
class AlbumModel:
    title: Column(String(255))
    release_date: Column(Date())

class AlbumSchema(SQLAlchemySchema):
    class Meta:
        model = AlbumModel
        load_instance = True  # Optional: deserialize to model instances
        include_fk = True # Optional: To include foreign fields
        include_relationships = True # Optional: To include relationships (become a fields.Related not fields.Nested)

    title = auto_field()
    release_date = auto_field()

# Ou avec SQLAlchemyAutoSchema

class AlbumSchema(SQLAlchemySchema):
    class Meta:
        model = AlbumModel
        load_instance = True  # Optional: deserialize to model instances
        include_fk = True # Optional: To include foreign fields
        include_relationships = True # Optional: To include relationships (become a fields.Related not fields.Nested)
```

Note: SQLAlchemySchema n'inclut pas les `sqlalchemy.relationship()`, juste les `sqlalchemy.Column()`

Regarder aussi:
- [marshmallow.fields.Nested()](https://marshmallow.readthedocs.io/en/stable/nesting.html)
- [read_only et dump_only](https://marshmallow.readthedocs.io/en/stable/quickstart.html#read-only-and-write-only-fields)
- [data_key](https://marshmallow.readthedocs.io/en/stable/quickstart.html#specifying-serialization-deserialization-keys)
  pour changer le nom d'un field du dictionnaire en un autre nom dans l'objet


## Services

Les services sont des classes utilitaires regroupant la logique métier propre a une entité\
Leur role est d'encapsuler cette logique (creer des méthodes dont le nom explicite la tache abstrite effectuée) et
donc rendre le code des controllers clair
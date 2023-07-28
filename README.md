# Projet de machine learning avec dashboard interactif et API

Ce projet de machine learning comprend un dashboard interactif développé avec Streamlit et une API déployée sur Heroku. L'objectif de ce projet est de fournir des prédictions basées sur un modèle de machine learning entraîné.
Ce projet est inspiré de la compétition kaggle https://www.kaggle.com/competitions/home-credit-default-risk/

## Fonctionnalités

- Dashboard interactif basé sur **streamlit**.
- API (**FLASK**)déployée sur **heroku** pour recevoir des requêtes GET et renvoyer des prédictions.
- Modèle de machine learning pré-entraîné utilisé pour les prédictions.

## Structure du projet

Le projet est organisé comme suit :

- Dasboard (streamlit)
    -  `Streamlit_App.py`: Fichier principal pour le dashboard interactif développé avec Streamlit.
    -  `dictionnaire.pickle`: permet d'inverser label-encoder et reccupérer les noms des classes de chaque variable
    -  `requirements.txt`: Fichier listant les dépendances Python requises pour exécuter le projet.

- Les autres fichiers (API)
   - `api.py`: Fichier contenant le code pour l'API déployée sur Heroku.
   - `requirements.txt`: Fichier listant les dépendances Python requises pour exécuter le projet.

## Modèle de machine learning

Le détail de la partie machine learning se trouve sur le repo : 
https://github.com/Florian-BOUDON/Scoring_Bancaire_Machine_Learning
- script evdently permettant d'obtenir les pages html du data drift
- ML-flow 
- Tests unitaires
- Pipeline du meilleur modèle


## Les grandes étapes

1. **Collecte des données** : merging des tables.
2. **Exploration des données** : analyse exploratoire des données pour comprendre leur structure, leurs caractéristiques et effectuer des prétraitements si nécessaire.
3. **Entraînement du modèle** : sélection d'un algorithme de machine learning, division des données en ensembles d'entraînement et de test, entraînement du modèle sur les données d'entraînement.
4. **Évaluation du modèle** : évaluation des performances du modèle à l'aide de métriques appropriées et ajustement des hyperparamètres création d'une fonction de perte.
5. **Développement du dashboard** : création d'un dashboard interactif.
6. **Déploiement de l'API** : déploiement de l'API sur Heroku pour permettre l'accès aux prédictions du modèle via des requêtes GET.

## Prérequis

Avant d'exécuter le projet, assurez-vous d'avoir installé les dépendances suivantes :

- Python 3.x
- Les bibliothèques Python spécifiées dans le fichier `requirements.txt`

## Installation

1. Clonez ce dépôt vers votre machine locale.
2. Accédez au répertoire du projet.
3. Installez les dépendances


## Utilisation streamlit

Afficher le dashboard Streamlit : https://dashboard-v3.streamlit.app/


## Utilisation heroku

Afficher le dashboard Streamlit : https://api-scoring-194928115115.herokuapp.com/
- point d'API GET :https://api-scoring-194928115115.herokuapp.com/proba
- point d'API POST :https://api-scoring-194928115115.herokuapp.com/predict

  ****
  Ce projet fait partie de la formation data scientist de CentraleSupélec & Openclassrooms (certificat bac+5).

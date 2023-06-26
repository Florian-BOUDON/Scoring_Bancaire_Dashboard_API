# Projet de Machine Learning avec Dashboard Interactif et API

Ce projet de machine learning comprend un dashboard interactif développé avec Streamlit et une API déployée sur Heroku. L'objectif de ce projet est de fournir des prédictions basées sur un modèle de machine learning entraîné.
Ce projet est inspiré de la compétition kaggle https://www.kaggle.com/competitions/home-credit-default-risk/

## Fonctionnalités

- Dashboard interactif basé sur Streamlit.
- API déployée sur Heroku pour recevoir des requêtes GET et renvoyer des prédictions basé sur le Framework FLASK.
- Modèle de machine learning pré-entraîné utilisé pour les prédictions.

## Structure du Projet

Le projet est organisé comme suit :

- dasboard (streamlit)
    -  `Streamlit_App.py`: Fichier principal pour le dashboard interactif développé avec Streamlit.
    -  `dictionnaire.pickle`: permet d'inverser label-encoder et reccupérer les noms des classes de chaque variable
    -  `requirements.txt`: Fichier listant les dépendances Python requises pour exécuter le projet.

- les autres fichiers (API)
   - `api.py`: Fichier contenant le code pour l'API déployée sur Heroku.
   - `requirements.txt`: Fichier listant les dépendances Python requises pour exécuter le projet.

## Modèle de Machine Learning

Le détail de la partie Machine Learning se trouve sur le repo : 
https://github.com/Florian-BOUDON/Scoring_Bancaire_Machine_Learning
- script evdently permettant d'obtenir les pages html du data drift
- ML Flow 
- tests unitaires
- pipeline du meilleur modèle


## Les grandes étapes

1. **Collecte des données** : Merging des tables.
2. **Exploration des données** : Analyse exploratoire des données pour comprendre leur structure, leurs caractéristiques et effectuer des prétraitements si nécessaire.
3. **Entraînement du modèle** : Sélection d'un algorithme de machine learning, division des données en ensembles d'entraînement et de test, entraînement du modèle sur les données d'entraînement.
4. **Évaluation du modèle** : Évaluation des performances du modèle à l'aide de métriques appropriées et ajustement des hyperparamètres création d'une fonction de perte.
5. **Développement du dashboard** : Création d'un dashboard interactif.
6. **Déploiement de l'API** : Déploiement de l'API sur Heroku pour permettre l'accès aux prédictions du modèle via des requêtes GET.

## Prérequis

Avant d'exécuter le projet, assurez-vous d'avoir installé les dépendances suivantes :

- Python 3.x
- Les bibliothèques Python spécifiées dans le fichier `requirements.txt`

## Installation

1. Clonez ce dépôt vers votre machine locale.
2. Accédez au répertoire du projet.
3. Installez les dépendances


## Utilisation Streamlit

Afficher le dashboard Streamlit : https://dashboard-v3.streamlit.app/


## Utilisation Heroku

Afficher le dashboard Streamlit : https://api-scoring-194928115115.herokuapp.com/
- point d'API GET :https://api-scoring-194928115115.herokuapp.com/proba
- point d'API POST :https://api-scoring-194928115115.herokuapp.com/predict

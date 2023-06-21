import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pickle
import unittest
import requests
import json
import os


df = pd.read_csv("data/df_streamlit.csv", index_col="SK_ID_CURR")
df_post = df.copy()

with open('dictionnaire.pickle', 'rb') as fichier:
    dictionnaire = pickle.load(fichier)
    
# Création de tests unitaires
def test_number_of_variables():
    assert len(df.columns) == 30, "Le nombre de variables est incorrect."
    
def test_variable_types():
    assert all(df.dtypes == "float64"), "Le type des variables est incorrect."

# Classe de tests unitaires
class MyTests(unittest.TestCase):
    def test_number_of_variables(self):
        test_number_of_variables()

    def test_variable_types(self):
        test_variable_types()

# Exécution des tests unitaires
unittest.main(argv=[''], exit=False, verbosity=2)


# Ajout d'une colonne avec la décennie (sert pr filtre en page 2)
df['Decennie'] = (df['Age'] // 10) * 10


def page_accueil():
    st.title("Application d'octroi des crédits")


    st.subheader("La banque prêt à dépenser vous présente sa nouvelle application \
                 de scoring bancaire quant à l'octroi de ces clients")


    col1, col2 = st.columns(2)

    with col1:
        st.header("Information relative au crédit bancaire")
        st.write("Un crédit est un engagement et doit être remboursé. "
                 "\nAssurez vous d'être en capacité de rembourser votre crédit")

    with col2:
        st.header("Information client")
        st.write("Les données consernant votre client peuvent récuppérées en page 2. "
                 "Les explications de l'octroi du crédit se trouve en page 2")


    # Sidebar elements

    # Les différents boutons

    st.sidebar.subheader("Caractéristiques du client")

    id_client = st.sidebar.number_input("Entrez l'ID du client",
                                        min_value=100000, max_value=999999, step=1)

    if id_client in df.index:
        client = df.loc[id_client]
        Salaire = st.sidebar.slider("Sélectionner l'ensemble des revenus du clients : ",
                                    min_value=0,
                                    max_value=100000,
                                    step=500)

        Enfant = st.sidebar.slider("Nombre d'enfant(s) du client : ",
                                    min_value=0,
                                    max_value=15,
                                    step=1)

        term = st.sidebar.radio("Durée du crédit en mois : ",
                                (24,36,48,60))

        AMT_GOODS_PRICE = st.sidebar.slider("Choisir le montant à emprunter : ",
                                            min_value=2000,
                                            max_value=40000,
                                            step=500)

        # Enregistrement des infos

        client["Enfant"] = Enfant
        client["Duree"] = term/12
        client["Salaire"] = Salaire
        client["AMT_GOODS_PRICE"] = AMT_GOODS_PRICE
        
        # Requête post api heroku
        client = df_post.loc[id_client]
        
        if st.button("Prediction_post"):
            client_dict = client.to_dict()
            st.write(client_dict)
            url_post = "https://app-scoring-heroku.herokuapp.com////prediction"
            response = requests.post(url_post, json=client_dict)
            st.write(response.json())
        
        
        
        # Requête get api heroku
        if st.sidebar.button("Prediction"):
            url = f"https://app-scoring-heroku.herokuapp.com////data?proba={id_client}"
            response = requests.get(url)
            if response.status_code == 200:
                    # Affichage de la réponse
                st.write(response.text)
            else:
                st.write("Erreur lors de la requête GET")
        

    else :
        st.sidebar.error("Ce client n'existe pas, veuillez vérifier l'identifiant")




def page_2():
    st.title("Comprendre les décisions bancaires")

    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Filtre par type de contrat
    labels_filtre = list(dictionnaire["Contrat"].keys())
    selected_label = st.sidebar.selectbox("Selectionner le type de contrat", labels_filtre)
    filtre_value = dictionnaire["Contrat"][selected_label]
    filtered_df = df[df["Contrat"] == filtre_value]

    # Filtre par taux de payment
    pr = st.sidebar.slider("Taux de remboursement",
                           min_value=0,
                           max_value=100,
                           value=10,
                           step=5)
     
    
    filtered_df["Taux de remboursement"]=filtered_df["AMT_CREDIT"]/(filtered_df["Duree"]*12)
    filtered_df = filtered_df[filtered_df["Taux de remboursement"]>(pr/100)]



    # Créer la barre latérale (sidebar)
    st.sidebar.title('Selectionner l\'âge')
    
    decennie_filter = st.sidebar.selectbox('Filtre par décennie', 
                                            range(20, 91, 10))

    
    col1, col2 = st.columns(2)
    
    with col1:
        sizes = filtered_df['TARGET'].value_counts(sort=True)

        colors = ["lightblue", "red"]

        fig_1, ax_1 = plt.subplots()

        explode = (0.05, 0.05)
        ax_1.pie(sizes, colors=colors, autopct='%1.1f%%',explode=explode,
                 shadow=True, startangle=90, labeldistance=0.5)

        plt.legend(["0 - Crédits remboursés", "1 - Défault de remboursement"],
                   fontsize=6, loc="lower right")

        plt.title('Part des défaults de crédit', fontsize=10)
        ax_1.axis('equal')
        st.pyplot(fig_1)


    with col2:
        
        # Filtrer les données en fonction de l'âge sélectionné dans la barre latérale
        filtered_df = df[df['Decennie'] == decennie_filter]

        # Calculer le pourcentage de défaut par genre
        defaut_par_genre = filtered_df.groupby('Genre')['TARGET'].mean() * 100
        
        fig_2, ax_2 = plt.subplots()
        plt.title('Pourcentage de défaut selon le genre')
        defaut_par_genre.plot(kind='bar', ax=ax_2)
        ax_2.set_xlabel('Genre')
        ax_2.set_ylabel('Pourcentage de défaut')
        ax_2.set_xticklabels(['Femme', 'Homme'], rotation=0)
        st.pyplot(fig_2)
    
    
# Sidebar de la page 2
    fichier = st.sidebar.file_uploader("Télécharger le fichier client ")
    if fichier is not None:
        st.write("Le fichier est télécharger")
        
def main():
    st.sidebar.title("Menu")
    pages = ["Accueil", "Deuxième page","df_streamlit"]
    choix = st.sidebar.selectbox("Choisir une page", pages)

    if choix == "Accueil":
        page_accueil()
    elif choix == "Deuxième page":
        page_2()
    elif choix=="df_streamlit":
        df_streamlit()
    

if __name__ == '__main__':
    main()

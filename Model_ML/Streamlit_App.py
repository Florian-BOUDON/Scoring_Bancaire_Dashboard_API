import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pickle

csv_url = "https://github.com/Florian-BOUDON/P7_API_Scoring/blob/main/df_streamlit.csv"
df = pd.read_csv(csv_url, sep=",",index_col="SK_ID_CURR")



with open('dictionnaire.pickle', 'rb') as fichier:
    dictionnaire = pickle.load(fichier)

def page_accueil():
    st.title("Application d'octroi des crédits")

    # Création d'un conteneur qui affiche une image
    container = st.container()
    image_path = "C:/Users/fbbou/PycharmProjects/P7_API_Scoring/Banque.png"
    image = open(image_path, "rb").read()
    with container:
        st.image(image)

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

        # affiche une barre de progression
        import time
        progress_bar = st.sidebar.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(1+i)

    else :
        st.sidebar.error("Ce client n'existe pas, veuillez vérifier l'identifiant")


    #predict button

    btn_predict = st.sidebar.button("Predict")

    """
    if btn_predict:
        pred = model.predict_proba(user_input)[:, 1]
    
        if pred[0] < 0.78:
            st.error('Warning! The applicant has a high risk to not pay'
                     ' the loan back!')
        else:
            st.success('It is green! The aplicant has a high probability to '
                       'pay the loan back'
    """


def page_2():
    st.title("Comprendre les décisions bancaires")

    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Filtre par type de contrat
    labels_filtre = list(dictionnaire["Contrat"].keys())
    selected_label = st.sidebar.selectbox("Selectionner le type de contrat",labels_filtre)
    filtre_value = dictionnaire["Contrat"][selected_label]
    filtered_df = df[df["Contrat"] == filtre_value]

    # Filtre par taux de payment
    pr = st.sidebar.slider("Taux de remboursement",
                   min_value=0,
                   max_value=100,
                   value=10,
                   step=5)
    filtered_df = filtered_df[filtered_df["PAYMENT_RATE"]>(pr/100)]


    with st.container():
        sizes = filtered_df['TARGET'].value_counts(sort=True)

        colors = ["lightblue", "red"]

        fig, ax = plt.subplots()

        explode = (0.05, 0.05)
        ax.pie(sizes, colors=colors, autopct='%1.1f%%',explode=explode,
               shadow=True, startangle=90, labeldistance=0.5)

        plt.legend(["0 - Crédits remboursés", "1 - Défault de remboursement"],
                   fontsize=6, loc="lower right")

        plt.title('Part des défaults de crédit', fontsize=10)
        ax.axis('equal')
        st.pyplot(fig)

    # Sidebar de la page 2
    fichier = st.sidebar.file_uploader("Télécharger le fichier client ")
    if fichier is not None:
        st.write("Le fichier est télécharger")

def main():
    st.sidebar.title("Menu")
    pages = ["Accueil", "Deuxième page"]
    choix = st.sidebar.selectbox("Choisir une page", pages)

    if choix == "Accueil":
        page_accueil()
    elif choix == "Deuxième page":
        page_2()

if __name__ == '__main__':
    main()
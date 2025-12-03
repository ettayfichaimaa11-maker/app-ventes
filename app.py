import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ---------- CONFIGURATION DE LA PAGE ----------
st.set_page_config(
    page_title="Prévisions des ventes",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CSS ----------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #0d0d0d, #1a1a1a);
        color: #f0f0f0;
    }
    h1, h2, h3 {
        color: #00ffff;
        font-family: 'Arial Black', sans-serif;
    }
    p, label, span {
        font-size: 16px;
        color: #f0f0f0;
    }
    div.stButton > button {
        background-color: #ff6f61;
        color: white;
        height: 3em;
        width: 12em;
        border-radius: 12px;
        border: none;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        background-color: #ff3b2f;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📊 Mes prévisions de ventes (Régression multiple)")


fichier_excel = st.file_uploader("📥 Sélectionnez votre fichier Excel", type=["xlsx"])

if fichier_excel:
    
    df_ventes = pd.read_excel(fichier_excel)
    
    
    colonnes_utiles = ["Mois", "Ventes", "Prix", "Publicité (DH)", "Satisfaction (%)"]
    df_ventes = df_ventes[colonnes_utiles]
    
    st.subheader(" Aperçu des données")
    st.dataframe(df_ventes)

    
    st.subheader("📈 Graphique des ventes par mois")
    fig, ax = plt.subplots()
    ax.plot(df_ventes["Mois"], df_ventes["Ventes"], marker='o', linestyle='--', color='green')
    plt.xticks(rotation=45)
    plt.xlabel("Mois")
    plt.ylabel("Ventes")
    plt.title("Évolution des ventes")
    st.pyplot(fig)

    
    st.subheader(" Entraînement du modèle de régression")

    X_values = df_ventes[["Prix", "Publicité (DH)", "Satisfaction (%)"]]
    y_values = df_ventes["Ventes"]

    modele_regression = LinearRegression()
    modele_regression.fit(X_values, y_values)

    st.success(" Le modèle est prêt !")
    
    st.subheader(" Faites vos prédictions")

    prix_input = st.number_input("Prix du produit", value=float(df_ventes["Prix"].mean()))
    pub_input = st.number_input("Budget publicitaire (DH)", value=float(df_ventes["Publicité (DH)"].mean()))
    sat_input = st.number_input("Taux de satisfaction (%)", value=float(df_ventes["Satisfaction (%)"].mean()))

    if st.button("Prédire les ventes"):
        prediction = modele_regression.predict([[prix_input, pub_input, sat_input]])[0]
        st.success(f" Estimation des ventes : {int(prediction)} unités ")

else:
    st.info(" Importez un fichier Excel pour démarrer l'analyse.")





    






 
  

 






















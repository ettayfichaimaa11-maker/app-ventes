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

# ---------- CSS PERSONNALISÉ ----------
st.markdown(
    """
    <style>
    /* Fond sombre dégradé */
    .stApp {
        background: linear-gradient(to right, #0d0d0d, #1a1a1a);
        color: #f0f0f0;
    }
    /* Titres stylés */
    h1, h2, h3 {
        color: #00ffff;  /* Cyan vif */
        font-family: 'Arial Black', sans-serif;
    }
    /* Texte normal */
    p, label, span {
        font-size: 16px;
        color: #f0f0f0;
    }
    /* Boutons stylés */
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
    /* Graphiques centrés */
    .css-1d391kg {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


      
# ---------- TITRE ----------
st.title("📊 Prévisions des ventes – Régression multiple")

# ----------- IMPORTATION -----------  
uploaded_file = st.file_uploader("📥 Importer le fichier Excel", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Réorganisation des colonnes (assure-toi que le fichier contient ces colonnes)
    df = df[["Mois", "Ventes", "Prix", "Publicité (DH)", "Satisfaction (%)"]]

    st.subheader("📄 Données importées")
    st.dataframe(df)

    # ----------- GRAPHIQUE -----------  
    st.subheader("📈 Évolution des ventes")
    fig, ax = plt.subplots()
    ax.plot(df["Mois"], df["Ventes"], marker='o')
    ax.set_xlabel("Mois")
    ax.set_ylabel("Ventes")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # ----------- RÉGRESSION MULTIPLE -----------  
    st.subheader("🤖 Modèle de régression multiple")

    X = df[["Prix", "Publicité (DH)", "Satisfaction (%)"]]
    y = df["Ventes"]

    model = LinearRegression()
    model.fit(X, y)

    st.success("✨ Le modèle a été entraîné avec succès !")

    # ----------- FORMULAIRE DE PRÉDICTION -----------  
    st.subheader("🔮 Prédiction des ventes")

    prix = st.number_input("Prix", value=float(df["Prix"].mean()))
    pub = st.number_input("Publicité (DH)", value=float(df["Publicité (DH)"].mean()))
    satisfaction = st.number_input("Satisfaction (%)", value=float(df["Satisfaction (%)"].mean()))

    if st.button("Prédire"):
        prediction = model.predict([[prix, pub, satisfaction]])[0]
        st.success(f"📌 Prévision des ventes : **{int(prediction)} unités**")

else:
    st.info("📌 Veuillez importer un fichier Excel pour commencer.")








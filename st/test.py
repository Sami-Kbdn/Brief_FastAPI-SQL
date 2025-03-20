import streamlit as st 
import sqlite3
import pandas as pd
import requests


# # Fonction pour récupérer les noms des colonnes de la table 'Performances'
# def get_performances_columns():
#     conn = sqlite3.connect("database.db")
#     cursor = conn.cursor()

#     # Exécuter une requête pour récupérer une ligne de la table, juste pour obtenir les noms de colonnes
#     cursor.execute("SELECT * FROM Performances LIMIT 1")
#     columns = [description[0] for description in cursor.description]  # Récupère les noms des colonnes

#     conn.close()
#     return columns

# # Créer un DataFrame avec les colonnes récupérées
# columns = get_performances_columns()
# df_data = pd.DataFrame(columns=columns)

# # Afficher le DataFrame vide sur Streamlit
# st.title("Performances des Athlètes")
# st.write("Voici un DataFrame avec les colonnes de la table Performances :")
# st.dataframe(df_data)  # Afficher le DataFrame dans Streamlit


import sqlite3
import pandas as pd
import streamlit as st

# Fonction pour récupérer les noms des colonnes de la table 'Performances'
def get_performances_columns():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Exécuter une requête pour récupérer une ligne de la table, juste pour obtenir les noms de colonnes
    cursor.execute("SELECT * FROM Performances LIMIT 1")
    columns = [description[0] for description in cursor.description]  # Récupère les noms des colonnes

    conn.close()
    return columns

# Fonction pour récupérer les performances par id
def get_performances_by_id(user_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Requête SQL pour récupérer les performances de l'utilisateur par id
    cursor.execute("SELECT * FROM Performances WHERE id = ?", (user_id,))
    performances = cursor.fetchall()

    conn.close()
    return performances


# Interface Streamlit
st.title("Gestion des Performances des Athlètes")

# Récupérer les ids des utilisateurs (par exemple, les ids sont dans la table 'Users')
conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT id FROM Performances")
user_ids = [row[0] for row in cursor.fetchall()]  # Liste des IDs d'utilisateurs
conn.close()

# Sélecteur de l'ID de l'utilisateur
user_id = st.selectbox("Sélectionnez un ID d'utilisateur", user_ids)

# Affichage des performances de l'utilisateur sélectionné
if user_id:
    performances = get_performances_by_id(user_id)
    if performances:
        st.write(f"Voici les performances pour l'utilisateur {user_id}:")
        # Créer un DataFrame avec les performances pour un affichage structuré
        columns = get_performances_columns()
        df_performances = pd.DataFrame(performances, columns=columns)
        st.dataframe(df_performances)  # Affichage du DataFrame
    else:
        st.warning(f"Aucune performance trouvée pour l'utilisateur {user_id}.")
    


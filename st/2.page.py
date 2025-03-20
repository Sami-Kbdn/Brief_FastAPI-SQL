import streamlit as st 
import sqlite3
import pandas as pd

connection = sqlite3.connect("database.db") 
cursor = connection.cursor()

st.sidebar.title("Main Menu")
choice = st.sidebar.radio(
    "Choose a section:",
    [
        "Add/Modify Performances",
        "View Athletes' Real-Time Statistics",
        "Visualize Trends and Comparisons Between Athletes"
    ]
)

def display(user_id):
    if choice == "Add/Modify Performances" : 
        st.title("Add/Modify Performances")




    elif choice == "View Athletes' Real-Time Statistics" :
        st.title("View Athletes' Real-Time Statistics")

        conn = sqlite3.connect("database.db")  # Adapter le chemin de la base
        cursor = conn.cursor()

        # Requête SQL pour récupérer les performances de l'utilisateur
        cursor.execute("SELECT * FROM Performances WHERE id = ?", (user_id,))
        performances = cursor.fetchall()  # Récupérer toutes les lignes correspondantes

        conn.close()
        return performances  # Retourne une liste de tuples avec les performances



        performances = get_performances_by_id(user_id)
        
        if performances:
            st.write("Voici vos performances :")
            for perf in performances:
                st.write(perf)  # Affichage brut, à adapter selon la structure des données
        else:
            st.warning("Aucune performance trouvée pour cet utilisateur.")


if st.session_state['loggedIn']:
    user_id = 1  # Remplace par l'ID de l'utilisateur connecté
    show_performances(user_id)












    elif choice == "Visualize Trends and Comparisons Between Athletes":
        st.title("Visualize Trends and Comparisons Between Athletes")

        
#tablo avec power_max / hr_max / vo2_max / rf_max / cadence
import sqlite3
import streamlit as st

# Fonction pour récupérer les performances
def get_performances_by_id(user_id: int):
    conn = sqlite3.connect("database.db")  # Adapter le chemin de la base
    cursor = conn.cursor()

    # Requête SQL pour récupérer les performances de l'utilisateur
    cursor.execute("SELECT * FROM Performances WHERE id = ?", (user_id,))
    performances = cursor.fetchall()  # Récupérer toutes les lignes correspondantes

    conn.close()
    return performances  # Retourne une liste de tuples avec les performances

# Fonction pour afficher les performances
def show_performances(user_id):
    performances = get_performances_by_id(user_id)
    
    if performances:
        st.write("Voici vos performances :")
        for perf in performances:
            st.write(perf)  # Affichage brut, à adapter selon la structure des données
    else:
        st.warning("Aucune performance trouvée pour cet utilisateur.")

# Interface Streamlit
# if st.session_state['loggedIn']:
#     st.title("View Athletes' Real-Time Statistics")
#     user_id = 1  # Remplace par l'ID de l'utilisateur connecté, ici juste un exemple
#     show_performances(user_id)


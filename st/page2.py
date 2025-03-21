import streamlit as st 
import sqlite3
import pandas as pd
import requests

connection = sqlite3.connect("database.db") 
cursor = connection.cursor()

def view_athletes():
    API_URL = "http://127.0.0.1:8000/all_athletes"

    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        athletes = data.get("athletes", [])  

    else:
        st.error(f"Error retrieving athletes : {response.status_code}")
        athletes = []

    if athletes:
        df = pd.DataFrame(athletes)

        athlete_ids = df["id"].tolist()
        selected_id = st.selectbox("Select an athlete by ID :", athlete_ids)

        selected_athlete = df[df["id"] == selected_id]

        st.write("Selected athlete information :")
        st.dataframe(selected_athlete)

    else:
        st.warning("No athletes found in the database")



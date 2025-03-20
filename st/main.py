import streamlit as st 
import sqlite3


connection = sqlite3.connect("database.db") 
cursor = connection.cursor()

# st.sidebar.title("Main Menu")
# choice = st.sidebar.radio(
#     "Choose a section:",
#     [
#         "Add/Modify Performances",
#         "View Athletes' Real-Time Statistics",
#         "Visualize Trends and Comparisons Between Athletes"
#     ]
# )


headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()
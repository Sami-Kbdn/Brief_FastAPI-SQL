import streamlit as st
import requests

def login():
    API_URL = "http://127.0.0.1:8000/login" 

    st.title("Welcome to VeloSense")

    username = st.text_input (label="", value="", placeholder="Enter your user name")
    password = st.text_input (label="", value="", placeholder="Enter password", type="password")

    if st.button("Se connecter"):
        if username and password:
            response = requests.post(API_URL, json={"username": username, "password": password})
            
            if response.status_code == 200:
                data = response.json()  
                st.success(f"Welcome {username} !")
                st.session_state["token"] = data.get("token")
                st.session_state["authenticated"] = True

    if "authenticated" in st.session_state and st.session_state["authenticated"]:
        if st.button("Click to access analytics"):
            st.session_state["page"] = "analytics"

if "page" in st.session_state and st.session_state["page"] == "analytics":
    import page2 
    page2.view_athletes()
else:
    login()
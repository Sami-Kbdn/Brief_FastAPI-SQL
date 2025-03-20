import streamlit as st
import sqlite3

headerSection = st.container()
loginSection = st.container()
logOutSection = st.container()

def login(username: str, password: str) -> bool:
    conn = sqlite3.connect("database.db") 
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM user WHERE username = ? AND password = ? AND role = 1", (username, password))
    user = cursor.fetchone()  

    conn.close()

    return user is not None

def LoggedIn_Clicked(userName, password):
    if login(userName, password): 
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False
        st.error("Invalid user name, password, or you are not authorized (coach required)")

def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            userName = st.text_input (label="", value="", placeholder="Enter your user name")
            password = st.text_input (label="", value="",placeholder="Enter password", type="password")
            st.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))

def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    
def show_logout_page():
    loginSection.empty()
    with logOutSection:
        st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)

with headerSection:
    st.title("Welcome to VeloSense")
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page() 
    else:
        if st.session_state['loggedIn']:
            show_logout_page()    
            #redirection page2()  
        else:
            show_login_page()
import streamlit as st
import streamlit_authenticator as stauth
from bs4 import BeautifulSoup
import requests

# --- Setup User Authentication ---
names = ["Alex"]
usernames = ["combust"]
passwords = ["qaz123"]  # Replace with hashed passwords for security

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "some_cookie_name", "some_signature_key", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.sidebar.title(f"Welcome {name}")
    authenticator.logout("Logout", "sidebar")

    # --- Page Navigation ---
    pages = {
        "Web Entry Interface": "pages/web_entry",
        "Knowledge Management": "pages/knowledge_management",
        "Large Language Model Interaction": "pages/llm_interaction",
        "Research Testing": "pages/research_testing"
    }

    page = st.sidebar.radio("Go to", list(pages.keys()))

    if pages[page] == "pages/web_entry":
        st.experimental_rerun()
    elif pages[page] == "pages/knowledge_management":
        st.experimental_rerun()
    elif pages[page] == "pages/llm_interaction":
        st.experimental_rerun()
    elif pages[page] == "pages/research_testing":
        st.experimental_rerun()

elif authentication_status is False:
    st.error("Username/password is incorrect")

elif authentication_status is None:
    st.warning("Please enter your username and password")
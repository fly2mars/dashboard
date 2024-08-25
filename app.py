import streamlit as st
#import streamlit_authenticator as stauth
#from bs4 import BeautifulSoup
import requests

# --- Setup User Authentication ---
names = ["Alex"]
usernames = ["combust"]
passwords = ["qaz123"]  # Replace with hashed passwords for security

#hashed_passwords = stauth.Hasher(passwords).generate()

#authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "some_cookie_name", "some_signature_key", cookie_expiry_days=30)

#name, authentication_status, username = authenticator.login("Login", "main")

st.write(names)
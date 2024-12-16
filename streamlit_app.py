import streamlit as st
import supabase
from dotenv import load_dotenv
load_dotenv()
st.title("🎈 Recipe Maker")
email = st.text_input("Email")
password = st.text_input("Password", None, 18, None, 'password', None, None, None, None, None)

signup = st.button("Sign Up")

if signup == True:
    st.write("sigma")

import streamlit as st
import pandas as pd

# Replace this with your published Google Sheets CSV URL
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQGCIkQEvfia5GeNnTXAOi1CAAA-IcOZCgcR1hXvj-JIepsUn3tPqtIaB-56fFXl8yadsRMockQ7dPx/pub?output=csv"

# Load member data
@st.cache_data
def load_data(url):
    return pd.read_csv(url)

df = load_data(sheet_url)

# UI
st.title("Member Directory")

name = st.selectbox("Select a member:", df['Name'])

if name:
    member = df[df['Name'] == name].iloc[0]
    st.text_input("Contact", member['Contact'] if pd.notna(member['Contact']) else "", disabled=True)
    st.text_input("Number", member['Number'] if pd.notna(member['Number']) else "", disabled=True)

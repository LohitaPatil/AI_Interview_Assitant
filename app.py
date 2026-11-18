import streamlit as st
from groq import Groq
st.set_page_config(page_title = "AI_Assistant", page_icon ="🤩", layout = "centered")
st.title("AI_Interview_Assitant")
st.caption("Practice and prepare your placements here")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFound):
  st.error("API key is missing Add it in advance setting")
  st.stop()
  

import streamlit as st
from groq import Groq
st.set_page_config(page_title = "AI_Assistant", page_icon ="🤩", layout = "centered")
st.title("AI_Interview_Assitant")
st.caption("Practice and prepare your placements here")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFoundError):
  st.error("API key is missing Add it in advance setting")
  st.stop()
role = st.selectbox("Job Title", ["ML engineer", "DevOps engineer", "Software developer", "Software Engineer", "Prompt engineer", "Data analyst", "Other"])
if role == "Other":
  st.text_input("Enter the job title","XXXXXXXX")
model = st.selectbox("Model",["openai/gpt-oss-20b", "openai/gpt-oss-120b"])
level = st.selectbox("Difficulty",["Beginner", "Intermediate", "Adavance"])
mode = st.radio("Activity", ["Generate questions","Evaluate answers","Improve answer", "Generate coding question"])+

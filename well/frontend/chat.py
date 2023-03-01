import streamlit as st
from streamlit_chat import message
import requests

st.set_page_config(
    page_title = "WELL",
    page_icon=":flower:"
)

st.header("WELL Chat")
st.markdown("[Github](https://github.com/Carlotaortizml/WELL-repository/tree/master/well)")

if 'generated' not in st.session_state:
    st.session_state["generated"] = []

if 'past' not in st.session_state:
    st.session_state["past"] = []

API_URL = "http://127.0.0.1"
API_PORT = "8080"

def query(payload):
    url = f"{API_URL}:{API_PORT}/send"
    response = requests.post(
                    url,
                    data={"input_text": payload}
                ).json()
    return response

def get_text():
    user_input = st.text_input("You: ")
    return user_input

#container = st.container()
#container.write("container inner")
user_input = get_text()

if user_input:
    output = query(user_input)
    st.write(output)

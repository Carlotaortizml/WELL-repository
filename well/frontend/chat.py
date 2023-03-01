import streamlit as st
from streamlit_chat import message
import requests
from well.utils import Utils
from well.params import *

user_input = ""
output = ""
util = Utils()

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

def query(payload):
    url = f"{API_URL}:{API_PORT}/send"
    if util.check_connection():
        params = {"input_text": payload}
        output = requests.post(
                        url,
                        params=params
                    )

        if output.status_code == 200:
            response = output.json()
            return response['response']
    else:
        return "Failed to connect to server"

def get_text():
    user_input = st.text_input("You: ")
    return user_input

user_input = get_text()

if user_input:
    output = query(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))

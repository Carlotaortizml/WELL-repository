import streamlit as st
from streamlit_chat import message
import requests
#from well.utils import Utils
#from well.params import *

#util = Utils()

# st.set_page_config(layout="wide")

def header(content):
    st.markdown(f'<div style="position: fixed;top: 0;width: 100%;padding: 25px 0px;z-index:9999;"><h2>{content}</h2></div>', unsafe_allow_html=True)

header("WELL Chat")

if "output_history" not in st.session_state:
    st.session_state["output_history"] = []

if "input_history" not in st.session_state:
    st.session_state["input_history"] = []

if "temp_user_input" not in st.session_state:
    st.session_state["temp_user_input"] = ""


def query(payload):
    api_url = st.secrets["API_URL"]
    url = f"{api_url}/chat"
    params = {"input_text": payload}
    output = requests.post(
                        url,
                        params=params
                    )
    if output.status_code == 200:
            response = output.json()
            return response['response']

    # print(url)
    '''
    if util.check_connection():
        params = {"input_text": payload}
        output = requests.post(
                        url,
                        params=params
                    )

        # print(output)

        if output.status_code == 200:
            response = output.json()
            return response['response']
    else:
        return "Failed to connect to server"
    '''

def clear_text():
    st.session_state["temp_user_input"] = st.session_state["user_input"]
    st.session_state["user_input"] = ""

def get_text():
    st.text_input("You: ", key="user_input", on_change=clear_text)
    return st.session_state["temp_user_input"]

placeholder = st.empty()
user_input = get_text()

with placeholder.container():
    if user_input:
        output = query(user_input)
        st.session_state["input_history"].append(user_input)
        st.session_state["output_history"].append(output)

with placeholder.container():
    if st.session_state["input_history"]:
        for i in range(len(st.session_state["input_history"])):
            message(st.session_state["input_history"][i], key=str(i) + '_user', avatar_style="adventurer", is_user=True)
            message(st.session_state["output_history"][i], key=str(i) + '_bot', seed=123, is_user=False)

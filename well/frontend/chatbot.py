from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
import streamlit as st
from streamlit_chat import message

tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")
model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")


def predict(input, history=[]):

    instruction = 'Instruction: given a dialog context, you need to response empathically'

    knowledge = '  '

    s = list(sum(history, ()))

    s.append(input)

    #print(s)

    dialog = ' EOS ' .join(s)

    #print(dialog)

    query = f"{instruction} [CONTEXT] {dialog} {knowledge}"

    top_p = 0.9
    min_length = 8
    max_length = 64


    # tokenize the new input sentence
    new_user_input_ids = tokenizer.encode(f"{query}", return_tensors='pt')


    output = model.generate(new_user_input_ids, min_length=int(
        min_length), max_length=int(max_length), top_p=top_p, do_sample=True).tolist()


    response = tokenizer.decode(output[0], skip_special_tokens=True)
    history.append((input, response))

    return history[0][1]

def get_text():
    input_text = st.text_input("You: ")
    return input_text

def chat():
    input = get_text()
    if input:
        result = predict(input)
        message(result[0][1])

if __name__=='__main__':
    chat()

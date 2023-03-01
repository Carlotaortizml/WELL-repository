import pandas as pd
import re
import numpy as np
from well.params import *


def create_input_output_df(df: pd.DataFrame) -> pd.DataFrame:
    preprocessed_df = pd.DataFrame(index=np.arange(df[df.interlocutor == "therapist"].shape[0]))
    preprocessed_df["transcript_id"] = -1
    preprocessed_df["input"] = ""
    preprocessed_df["output"] = ""
    preprocessed_df["knowledge"] = ""

    row_cursor = 0
    i = 0
    for transcript_id in df.transcript_id.unique():

        sub_df = df[df.transcript_id==transcript_id]
        i_prior = i
        while i < sub_df.shape[0] + i_prior:
            client_text = ""
            while i < sub_df.shape[0] + i_prior and sub_df.interlocutor[i] == "client":
                client_text += ("; " if client_text else "") + sub_df.utterance_text[i]
                i += 1

            therapist_text = ""
            while i < sub_df.shape[0] + i_prior and sub_df.interlocutor[i] == "therapist":
                therapist_text += ("; " if therapist_text else "") + sub_df.utterance_text[i]
                i += 1
            if i >= sub_df.shape[0] + i_prior:
                break
            preprocessed_df["input"][row_cursor] = client_text
            preprocessed_df["output"][row_cursor] = therapist_text
            preprocessed_df["transcript_id"][row_cursor] = transcript_id
            preprocessed_df["knowledge"][row_cursor] = sub_df["topic"][i_prior]
            row_cursor += 1
    return preprocessed_df[preprocessed_df.transcript_id != -1]

def get_df_with_joined_inputs(input_output_df:pd.DataFrame)->pd.DataFrame:

    input_output_df["joined_inputs"] = ""
    joined_inputs = ""
    for i in range(len(input_output_df)):
        if i > 0 and input_output_df.transcript_id[i] != input_output_df.transcript_id[i-1]:
            joined_inputs = ""
        joined_inputs += (" EOS " if joined_inputs else "") + input_output_df.input[i]
        input_output_df["joined_inputs"][i] = joined_inputs
        joined_inputs += (" EOS " if joined_inputs else "") + input_output_df.output[i]
    input_output_df =\
        input_output_df.drop(columns="transcript_id")\
            .applymap(lambda exp_string: re.sub(r"\[.*\]","",exp_string).strip())
    input_output_df["input"] = input_output_df["joined_inputs"]
    input_output_df.drop(columns="joined_inputs", inplace=True)
    return input_output_df

def create_preprocessed_file(path_original, path_target):
    df = pd.read_csv(path_original)
    df = df[["transcript_id", "topic", "utterance_id", "interlocutor", "utterance_text", "main_therapist_behaviour", "client_talk_type"]]
    input_output_df = create_input_output_df(df)
    input_output_df = get_df_with_joined_inputs(input_output_df)
    input_output_df.to_csv(path_target)

if __name__ == "__main__":
    print(__file__)
    # TODO might have to add knowledge as column (e.g. the topic of the conversation)
    create_preprocessed_file(path_original=YOUTUBE_CONVERSATIONS_RAW_PATH,
                             path_target=YOUTUBE_CONVERSATIONS_PROCESSED_PATH)

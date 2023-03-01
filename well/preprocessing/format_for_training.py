import pandas as pd
import numpy as np
import jsonlines

def create_jsonl(path_csv="/home/moritzb6626/code/Carlotaortizml/WELL-repository/preprocessed_data_level1/chats/preprocessed_full.csv", path_jsonl="/home/moritzb6626/code/Carlotaortizml/WELL-repository/preprocessed_data_level1/chats/formatted_for_training.jsonl"):
    full_csv = pd.read_csv(path_csv).drop(columns="Unnamed: 0")
    full_dictionary = []

    for i in range(full_csv.__len__()):
        full_dictionary.append(
            {
                "Context":
                    full_csv["input"][i],
                "Knowledge":
                    "",
                "Response":
                    full_csv["output"][i]
            }
        )

    with jsonlines.open(file=path_jsonl, mode="w") as writer:
        for e in full_dictionary:
            writer.write(e)

if __name__ == "__main__":
    create_jsonl()

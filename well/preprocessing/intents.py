import pandas as pd
import json
def process_intents(d: dict[list[dict]]) -> pd.DataFrame:
    inputs = pd.DataFrame(columns=["tag", "input"])
    outputs = pd.DataFrame(columns=["tag", "output"])
    for intent in d["intents"]:
        for pattern in intent["patterns"]:
            inputs = pd.concat(
                [inputs, pd.DataFrame([[intent["tag"], pattern]],columns=["tag", "input"])])
        for response in intent["responses"]:
            outputs = pd.concat([outputs, pd.DataFrame([[intent["tag"], response]],columns=["tag", "output"])])
    return inputs.merge(outputs, on="tag").drop(columns="tag")

def create_preprocessed_file(path_original="/home/moritzb6626/code/Carlotaortizml/WELL-repository/raw_data/intents.json", path_target="/home/moritzb6626/code/Carlotaortizml/WELL-repository/preprocessed_data_level1/chats/preprocessed_intends.csv"):
    pd.read_json("../raw_data/intents.json")
    with open(path_original, "r") as intent_file:
        d = json.load(intent_file)
        process_intents(d=d).to_csv(path_target)

if __name__ == "main":
    create_preprocessed_file()

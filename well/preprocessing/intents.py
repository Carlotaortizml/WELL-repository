import pandas as pd
import json
from well.params import *
def process_intents(d: dict[list[dict]]) -> pd.DataFrame:
    inputs = pd.DataFrame(columns=["tag", "input"])
    outputs = pd.DataFrame(columns=["tag", "output"])
    for intent in d["intents"]:
        for pattern in intent["patterns"]:
            inputs = pd.concat(
                [inputs, pd.DataFrame([[intent["tag"], pattern]],columns=["tag", "input"])])
        for response in intent["responses"]:
            outputs = pd.concat([outputs, pd.DataFrame([[intent["tag"], response]],columns=["tag", "output"])])
    result_df = inputs.merge(outputs, on="tag")
    result_df["knowledge"] = result_df["tag"]
    result_df["knowledge"] = result_df["knowledge"].map(lambda text: "fact" if "fact" in text else text)
    return result_df.drop(columns="tag")

def create_preprocessed_file(path_original=INTENTS_RAW_PATH, path_target=INTENTS_PROCESSED_PATH):
    pd.read_json(path_original)
    with open(path_original, "r") as intent_file:
        print(":true: preprocessing intents")
        d = json.load(intent_file)
        process_intents(d=d).to_csv(path_target)

if __name__ == "__main__":
    create_preprocessed_file()

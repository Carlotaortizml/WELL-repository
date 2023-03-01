import pandas as pd
import jsonlines
from well.params import *
def create_jsonl(path_csv, path_jsonl):
    full_csv = pd.read_csv(path_csv).drop(columns="Unnamed: 0")
    full_dictionary = []
    for i in range(full_csv.__len__()):
        full_dictionary.append(
            {
                "Context":
                    full_csv["input"][i],
                "Knowledge":
                    full_csv["knowledge"][i],
                "Response":
                    full_csv["output"][i]
            }
        )
    with jsonlines.open(file=path_jsonl, mode="w") as writer:
        for e in full_dictionary:
            writer.write(e)
if __name__ == "__main__":
    create_jsonl(path_csv=FULL_PROCESSED_PATH,
                 path_jsonl=FULL_JSONL_PATH)
    create_jsonl(path_csv=YOUTUBE_CONVERSATIONS_PROCESSED_PATH,
                 path_jsonl=YOUTUBE_CONVERSATIONS_JSONL_PATH)

    create_jsonl(path_csv=INTENTS_PROCESSED_PATH,
                 path_jsonl=INTENTS_JSONL_PATH)

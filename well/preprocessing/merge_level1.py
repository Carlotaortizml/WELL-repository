import pandas as pd
from well.params import *
def create_full_preprocessed_csv(path_intend,
                                 path_youtube_conversations,
                                 path_target):
    intents_df = pd.read_csv(path_intend).drop(columns="Unnamed: 0")
    youtube_conversations_df = pd.read_csv(path_youtube_conversations).drop(columns="Unnamed: 0")
    pd.concat([intents_df, youtube_conversations_df], ignore_index=True)\
        .dropna()\
            .to_csv(path_target)
if __name__ == "__main__":
    create_full_preprocessed_csv(path_intend=INTENTS_PROCESSED_PATH,
                                 path_youtube_conversations=YOUTUBE_CONVERSATIONS_PROCESSED_PATH,
                                 path_target=FULL_PROCESSED_PATH)

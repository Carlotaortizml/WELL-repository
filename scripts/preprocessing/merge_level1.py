import pandas as pd
def create_full_preprocessed_csv(path_intend="/home/moritzb6626/code/Carlotaortizml/WELL-repository/preprocessed_data_level1/chats/preprocessed_intends.csv",
                                 path_mental_health_faq = "/home/moritzb6626/code/Carlotaortizml/WELL-repository/preprocessed_data_level1/chats/preprocessed_mental_health_faq.csv",
                                 path_youtube_conversations = "/home/moritzb6626/code/Carlotaortizml/WELL-repository/preprocessed_data_level1/chats/preprocessed_youtube-conversations.csv",
                                 path_target="/home/moritzb6626/code/Carlotaortizml/WELL-repository/preprocessed_data_level1/chats/preprocessed_full.csv"):
    intents_df = pd.read_csv(path_intend).drop(columns="Unnamed: 0")
    mental_health_faq_df = pd.read_csv(path_mental_health_faq).drop(columns="Unnamed: 0")
    youtube_conversations_df = pd.read_csv(path_youtube_conversations).drop(columns="Unnamed: 0")

    pd.concat([intents_df, mental_health_faq_df, youtube_conversations_df], ignore_index=True)\
        .dropna()\
            .to_csv(path_target)

if __name__ == "__main__":
    create_full_preprocessed_csv()

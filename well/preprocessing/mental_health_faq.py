import pandas as pd

def process_mental_health_faq(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(columns={"Questions": "input", "Answers": "output"}).drop(columns=["Question_ID"])

def create_preprocessed_file(path_original="/home/moritzb6626/code/Carlotaortizml/WELL-repository/raw_data/Mental_Health_FAQ.csv", path_target="/home/moritzb6626/code/Carlotaortizml/WELL-repository/preprocessed_data_level1/chats/preprocessed_mental_health_faq.csv"):
    df = pd.read_csv(path_original)
    df.rename(columns={"Questions": "input", "Answers": "output"}).drop(columns=["Question_ID"])
    process_mental_health_faq(df).to_csv(path_target)

if __name__ == "__main__":
    create_preprocessed_file()

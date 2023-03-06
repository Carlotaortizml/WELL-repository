import pandas as pd
import json
with open("/home/moritzb6626/code/Carlotaortizml/WELL-repository/raw_data/empathetic_dialogues_train.json") as file:
    train_json = json.load(file)
temp = pd.DataFrame([train_json["rows"][i]["row"] for i in range(train_json["rows"].__len__())], index=[i for i in range(train_json["rows"].__len__())])
temp.utterance = temp.utterance.map(lambda utterance: utterance.replace("_comma_", ","))
n = 3
dfs = []

for conv_id in temp.conv_id.unique():
    # conv_id = temp.conv_id.unique()[0]
    temp_temp = temp[temp.conv_id == conv_id]
    contexted = []
    for i in range(temp_temp.index[-1], temp_temp.index[0]-1, -1):
        row = []
        prev = i - 1 - n # we additionally substract 1, so row will contain current responce and 7 previous responses
        # print(prev)
        if prev >= temp_temp.index[0]-1:
            for j in range(i, prev, -1):
                print(j)
                # display(temp_temp.utterance)
                row.append(temp_temp.utterance[j])
            contexted.append(row)
        else:
            break
        # print(row)
    columns = ['response', 'context']
    columns = columns + ['context/' + str(i) for i in range(n-1)]
    df = pd.DataFrame.from_records(contexted, columns=columns)
    dfs.append(df)
    # assert df.shape[0] > 0, f"{temp_temp.shape[0]}"


for df in dfs:
    if df.shape[1] != n+1:
        raise Exception()


pd.concat(dfs, ignore_index=True).to_csv("raw_data/empathetic_dialogues.csv")

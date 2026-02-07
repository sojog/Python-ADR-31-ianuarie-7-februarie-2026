
import pandas as pd
import matplotlib.pyplot as plt

f1df = pd.read_csv("date/fisier1.csv")
f1df

f2df = pd.read_csv("date/fisier2.csv")
f2df

f1df.keys()

f1df = f1df.rename(columns={
    "Unnamed: 0" : "COD",
    "Unnamed: 1" : "Produs",
}) 
f1df

f2df = f1df.rename(columns={
    "Unnamed: 0" : "COD",
    "Unnamed: 1" : "Produs",
}) 
f2df

merge_df = pd.merge(f1df,f1df, on="COD")
merge_df

merge_df.keys()

merge_df = merge_df.drop(['Unnamed: 2_x', 'Unnamed: 2_y', 'Produs_y'], axis=1)
merge_df

merge_df["TR CI"] = 0
merge_df["TR CR"] = 0

merge_df.head(2)

merge_df.keys()

merge_df = merge_df[['COD', 'Produs_x', 'Cinema_x', 'Cinema_y', 'Crisan_x', 'DEPOZIT_x',
       'Gara_x', 'Progresu_x', 'Steaua_x', 'Zahana_x', 'TOTAL_x', 'Crisan_y',
       'DEPOZIT_y', 'Gara_y', 'Progresu_y', 'Steaua_y', 'Zahana_y', 'TOTAL_y',
       'TR CI', 'TR CR']]


merge_df.rename(
    columns={
        "Produs_x": "PRODUS",
        "Cinema_x": "Cinema",
    }
)

print(merge_df)

merge_df.to_csv("date/fisier_salvat.csv")





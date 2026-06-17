import os
import pandas as pd
import numpy as np

"""this will clean up data and collect the info i need and load to a new csv file"""

input_folder = "raw_data.csv"
output_folder = "cleaned_data.csv"
#os.makedirs(output_folder, exist_ok=True)


#i removed nickname from this along with other redundant columns
columns = ["PLAYER_ID","PLAYER_NAME","TEAM_ID","TEAM_ABBREVIATION","AGE","GP","W","L","W_PCT",
            "MIN","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","FTM","FTA","FT_PCT","OREB","DREB","REB","AST","TOV",
            "STL","BLK","BLKA","PF","PFD","PTS","PLUS_MINUS","TEAM_COUNT"]

columns2beAVG = ["MIN","FGM","FGA","FG3M","FG3A","FTM","FTA","REB","AST","TOV","STL","BLK","PTS"]


df = pd.read_csv(input_folder, usecols = columns)

for col in columns2beAVG:
    df[col] = df[col] / df["GP"]
    df[col] = df[col].round(1)

df = df[df["MIN"] >= 20]
df = df[df["GP"] >= 30] #change this value to around 40?
#df = df[df["TEAM_ABBREVIATION"] == 'MIA']

print("File transformation complete. The following stats have been set to averages:")
print(", ".join(columns2beAVG))


#
# print(df.head())
# print(df.info())

df.to_csv(output_folder, index = False) #uncomment this once i get the fix


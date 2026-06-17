import os
import pandas as pd
import numpy as np

"""this will clean up data and collect the info i need and load to a new csv file"""

input_folder = "raw_data.csv"
output_folder = "test_data.csv"
#os.makedirs(output_folder, exist_ok=True)

sample = ["testtt"]

#i removed nickname from this along with other redundant columns
columns = ["PLAYER_ID","PLAYER_NAME","TEAM_ID","TEAM_ABBREVIATION","AGE","GP","W","L","W_PCT",
            "MIN","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","FTM","FTA","FT_PCT","OREB","DREB","REB","AST","TOV",
            "STL","BLK","BLKA","PF","PFD","PTS","PLUS_MINUS"]

columns2beAVG = ["MIN","FGM","FGA","FG3M","FG3A","FTM","FTA","REB","AST","TOV","STL","BLK","PTS"]

column_toprac = ["MIN", "REB", "PTS"]

###My goal here is to first find these stats (prob by STAT / GP) and then to create the (new) csv with these files
# final_columns = ["PLAYER_ID","PLAYER_NAME","TEAM_ID","TEAM_ABBREVIATION","AGE","GP","W","L","W_PCT",
#                  "MIN","PPG","REB","AST","TOV","STL","BLK","FGM","FGA","FG3M","FG3A","FTM","FTA",
#                  "PLUS_MINUS","TEAM_COUNT"]

df = pd.read_csv(input_folder, usecols = columns)
# print(df[columns].head())
# print(df[columns].info())
new_values = []

for col in columns2beAVG:
    df[col] = df[col] / df["GP"]
    df[col] = df[col].round(1)

df = df[df["MIN"] >= 20]

    # if k["AGE"] > 37:
    #     print(f"player name: {k["PLAYER_NAME"]}")
    #     print(form_PPG)



# print(len(new_values))
# df['PPG'] = new_values

print(df.head())
print(df.info())

df.to_csv(output_folder, index = False) #uncomment this once i get the fix

def stat_per_game():
    stat_avg = 8

# for filename in os.listdir(input_folder):
#     if filename.endswith(".csv"):
#         file_path = os.path.join(input_folder, filename)
#         print("File in process: ", file_path)
#
#         df = pd.read_csv(file_path)
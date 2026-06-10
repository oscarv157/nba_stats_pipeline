import os
import pandas as pd
import numpy as np

#this will clean up data and collect the info i need and load to a new csv file

input_folder = "raw_data.csv"
output_folder = "cleaned_data.csv"
#os.makedirs(output_folder, exist_ok=True)

sample = ["testtt"]

columns = ["PLAYER_ID","PLAYER_NAME","NICKNAME","TEAM_ID","TEAM_ABBREVIATION","AGE","GP","W","L","W_PCT",
            "MIN","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","FTM","FTA","FT_PCT","OREB","DREB","REB","AST","TOV",
            "STL","BLK","BLKA","PF","PFD","PTS","PLUS_MINUS","TEAM_COUNT"]

df = pd.read_csv(input_folder, usecols = columns)
print(df[columns].head())
print(df[columns].info())

df[columns].to_csv(output_folder, index = False)

# for filename in os.listdir(input_folder):
#     if filename.endswith(".csv"):
#         file_path = os.path.join(input_folder, filename)
#         print("File in process: ", file_path)
#
#         df = pd.read_csv(file_path)
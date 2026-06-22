import pandas as pd
from nba_api.stats.endpoints import commonplayerinfo

"""This script adds a years played columns to the cleaned csv file. It then calculates the total YOE for each player"""

input_folder = "cleaned_data.csv"
df = pd.read_csv(input_folder)
# df = pd.DataFrame(input_folder)

# df['YEARS_PLAYED'] = 0 #This creates a new column, setting all values to 0

for i,k in df.iterrows():
    if k["YEARS_PLAYED"] == 0: #This checks if the YEARS_PLAYED column has already been filled out
        draftYear = commonplayerinfo.CommonPlayerInfo(player_id=k["PLAYER_ID"])
        df2 = draftYear.get_data_frames()
        dftYR = df2[0]['FROM_YEAR'][0]
        total = 2026 - dftYR
        df.loc[i, 'YEARS_PLAYED'] = total
        print(k["PLAYER_ID"], k["PLAYER_NAME"], total)
        df.to_csv(input_folder, index=False)
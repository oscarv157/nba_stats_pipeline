import pandas as pd

input_file = 'cleaned_data.csv'
output_file = 'enhanced_data.csv'

columns = ["PLAYER_NAME","TEAM_ABBREVIATION","FG_PCT","REB","AST","PTS","YEARS_PLAYED"]
dfx = pd.read_csv(input_file)

def player_zscores():
    """this func defines z scores for points, rebounds, and assists"""
    dfx["PTS_Z"] = round((dfx["PTS"] - dfx["PTS"].mean()) / dfx["PTS"].std(), 2)
    dfx["REB_Z"] = round((dfx["REB"] - dfx["REB"].mean()) / dfx["REB"].std(), 2)
    dfx["AST_Z"] = round((dfx["AST"] - dfx["AST"].mean()) / dfx["AST"].std(), 2)
    dfx["BLK_Z"] = round((dfx["BLK"] - dfx["BLK"].mean()) / dfx["BLK"].std(), 2)
    dfx["STL_Z"] = round((dfx["STL"] - dfx["STL"].mean()) / dfx["STL"].std(), 2)



    dfx.to_csv(output_file, index=False)
    print("Z-scores now written to enhanced_data.csv file")

player_zscores()
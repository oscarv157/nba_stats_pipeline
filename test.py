from nba_api.stats.endpoints import playercareerstats
import json
from tabulate import tabulate
import pandas as pd

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999')

# pandas data frames (optional: pip install pandas)
df = career.season_totals_regular_season.get_data_frame()
# Set pandas to show all columns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

#print(df.to_string(index=False))
# json
hey = career.get_json()

# dictionary
hi = career.get_dict()
cols = ['SEASON_ID', 'TEAM_ABBREVIATION', 'GP', 'PTS', 'REB', 'AST']

print(tabulate(df[cols], headers='keys', tablefmt='pretty', showindex=False))

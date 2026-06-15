from nba_api.stats.static import players
from nba_api.stats.endpoints import leaguedashplayerstats
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import teams
import pandas as pd
from tabulate import tabulate


"""This takes in current season data of each player from nba_api.
    This also transfer data into csv file"""

player_list = leaguedashplayerstats.LeagueDashPlayerStats(season="2025-26",)
all_player_stats = player_list.get_data_frames()[0]

#this just prints the data in a pretty table on console
player_table  = tabulate(all_player_stats, headers="keys",tablefmt='pretty', showindex=False)
print(player_table)

df = pd.DataFrame(all_player_stats)

df.to_csv("raw_data.csv", index= False)


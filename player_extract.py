from nba_api.stats.static import players
from nba_api.stats.endpoints import leaguedashplayerstats
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import teams
import pandas as pd
from tabulate import tabulate

#
# #waza = players.find_players_by_first_name("lebron")
# waza = teams.find_teams_by_full_name("Miami Heat")
# team_id = waza[0]['id']
#
# jang = tabulate(waza,headers='keys', tablefmt='pretty', showindex=False)
#
# print(jang)

# lebron = players.find_players_by_first_name("lebron")
# print(lebron)
# bron_id = lebron[0]["id"]
# lebron_nums = playercareerstats.PlayerCareerStats(player_id=bron_id)
#
# lebronseason = lebron_nums.season_totals_regular_season.get_data_frame()
# current_season  = "2025-26"
# lebron_df = lebronseason[lebronseason["SEASON_ID"] == current_season]
# #cols = ["SEASON_ID", "PLAYER_AGE", "GP", "MIN"]
# gang = tabulate(lebron_df,headers='keys', tablefmt='pretty', showindex=False)
# print(gang)

"""this takes in current season data of each player from nba_api"""
player_list = leaguedashplayerstats.LeagueDashPlayerStats(season="2025-26",)
all_player_stats = player_list.get_data_frames()[0]

#this just prints the data in a pretty table on console
player_table  = tabulate(all_player_stats, headers="keys",tablefmt='pretty', showindex=False)
print(player_table)

df = pd.DataFrame(all_player_stats)

df.to_csv("raw_data.csv", index= False)


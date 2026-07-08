import pandas as pd
from tabulate import tabulate

input_file = 'cleaned_data.csv'
df = pd.read_csv(input_file)
yearsByGroup = df["YEARS_PLAYED"].value_counts()
yearsByGroup = yearsByGroup.sort_index()
# print(yearsByGroup)

# currentYR = (yearsByGroup[2])
# print(currentYR)

def year_avg(year): #this gets the averages per YOE
    yr_pts = 0
    yr_reb = 0
    yr_ast = 0
    yr_blk = 0
    yr_stl = 0
    currentYR = (yearsByGroup[year])
    for i, k in df.iterrows():
        if k["YEARS_PLAYED"] == year:
            yr_pts += k["PTS"]
            yr_reb += k["REB"]
            yr_ast += k["AST"]
            yr_blk += k["BLK"]
            yr_stl += k["STL"]
            # print(k["PLAYER_NAME"],k["PTS"]),k["REB"],k["AST"])

    #print(f"Year {year} total points: {yr_pts:.1f}")
    yr_av = [float(round(yr_pts / currentYR,1)),
             float(round(yr_reb / currentYR,1)),
             float(round(yr_ast / currentYR,1)),
             float(round(yr_blk / currentYR,1)),
             float(round(yr_stl / currentYR,1))
             ]
    yr_avg = yr_pts / currentYR
    # print(yr_av)
    # print(f"Year {year} average points: {yr_avg:.1f} out of {currentYR} players")
    return yr_av

def get_allAVG(): #this lists all the year specified players and their stat
    top_yrS  = {"YEARS_PLAYED": 0, "PTS": 0,"REB": 0, "AST": 0,"BLK": 0, "STL": 0}
    top_yrR  = {"YEARS_PLAYED": 0, "PTS": 0,"REB": 0, "AST": 0,"BLK": 0, "STL": 0}
    top_yrA = {"YEARS_PLAYED": 0, "PTS": 0,"REB": 0, "AST": 0,"BLK": 0, "STL": 0}
    top_yrST = {"YEARS_PLAYED": 0, "PTS": 0, "REB": 0, "AST": 0, "BLK": 0, "STL": 0}
    top_yrB = {"YEARS_PLAYED": 0, "PTS": 0, "REB": 0, "AST": 0, "BLK": 0, "STL": 0}

    rows = []

    #print(f"Stats: PTS, REB, AST, BLK, STL")
    for yr,pts in yearsByGroup.items():
        points = year_avg(yr)
        rows.append({
            "YEARS_PLAYED": yr,
            "PTS": round(points[0], 1),
            "REB": round(points[1], 1),
            "AST": round(points[2], 1),
            "BLK": round(points[3], 1),
            "STL": round(points[4], 1)
        })
        # print(f"Year: {yr}, Stats: {points}")

        if top_yrS is None or points[0] > top_yrS["PTS"]: #this is to get the year with highest PPG
            top_yrS["YEARS_PLAYED"] = yr
            top_yrS["PTS"] = float(round(points[0], 1))
        if top_yrR is None or points[1] > top_yrR["REB"]: #this is to get the year with highest REB
            top_yrR["YEARS_PLAYED"] = yr
            top_yrR["REB"] = float(round(points[1], 1))
        if top_yrA is None or points[2] > top_yrA["AST"]: #this is to get the year with highest AST
            top_yrA["YEARS_PLAYED"] = yr
            top_yrA["AST"] = float(round(points[2], 1))
        if top_yrB is None or points[3] > top_yrA["BLK"]: #this is to get the year with highest BLK
            top_yrB["YEARS_PLAYED"] = yr
            top_yrB["BLK"] = float(round(points[3], 1))
        if top_yrST is None or points[4] > top_yrA["STL"]: #this is to get the year with highest STL
            top_yrST["YEARS_PLAYED"] = yr
            top_yrST["STL"] = float(round(points[4], 1))

    # print(f"Year {top_yrS["YEARS_PLAYED"]} has the highest scoring averages: {top_yrS["PTS"]}")
    # print(f"Year {top_yrR["YEARS_PLAYED"]} has the highest rebound averages: {top_yrR["REB"]}")
    # print(f"Year {top_yrA["YEARS_PLAYED"]} has the highest assist averages: {top_yrA["AST"]}")
    # print(f"Year {top_yrB["YEARS_PLAYED"]} has the highest block averages: {top_yrB["BLK"]}")
    # print(f"Year {top_yrST["YEARS_PLAYED"]} has the highest steal averages: {top_yrST["STL"]}")

    yearly_df = pd.DataFrame(rows)

    return top_yrS, top_yrR, top_yrA, top_yrB, top_yrST, yearly_df


def topScorer(year): #this finds the player who averaged the most points in specified year
    topPlayer = None
    for i, k in df.iterrows():
        if k["YEARS_PLAYED"] == year:
            if topPlayer is None or k["PTS"] > topPlayer["PTS"]:
                topPlayer = k

    # print(f"Year {topPlayer["YEARS_PLAYED"]} Best Scorer: {topPlayer["PLAYER_NAME"]}: {topPlayer["PTS"]}")

    return topPlayer

def topRebounder(year): #this finds the player who averaged the most rebounds in specified year
    topPlayer = None
    for i, k in df.iterrows():
        if k["YEARS_PLAYED"] == year:
            if topPlayer is None or k["REB"] > topPlayer["REB"]:
                topPlayer = k

    # print(f"Year {topPlayer["YEARS_PLAYED"]} Best Rebounder: {topPlayer["PLAYER_NAME"]}: {topPlayer["REB"]}")
    return topPlayer

def topPlaymaker(year): #this finds the player who averaged the most assists in specified year
    topPlayer = None
    for i, k in df.iterrows():
        if k["YEARS_PLAYED"] == year:
            if topPlayer is None or k["AST"] > topPlayer["AST"]:
                topPlayer = k

    # print(f"Year {topPlayer["YEARS_PLAYED"]} Best Playmaker: {topPlayer["PLAYER_NAME"]}: {topPlayer["AST"]}")
    return topPlayer

def topSteals(year): #this finds the player who averaged the most steals in specified year
    topPlayer = None
    for i, k in df.iterrows():
        if k["YEARS_PLAYED"] == year:
            if topPlayer is None or k["STL"] > topPlayer["STL"]:
                topPlayer = k

    # print(f"Year {topPlayer["YEARS_PLAYED"]} Steal leader: {topPlayer["PLAYER_NAME"]}: {topPlayer["STL"]}")
    return topPlayer

def topBlocker(year): #this finds the player who averaged the most blocks in specified year
    topPlayer = None
    for i, k in df.iterrows():
        if k["YEARS_PLAYED"] == year:
            if topPlayer is None or k["BLK"] > topPlayer["BLK"]:
                topPlayer = k

    # print(f"Year {topPlayer["YEARS_PLAYED"]} Top Shot Blocker: {topPlayer["PLAYER_NAME"]}: {topPlayer["BLK"]}")
    return topPlayer

# year = 5
# year_avg(year)
# topScorer(year)
# topRebounder(year)
# topPlaymaker(year)
# topSteals(year)
# topBlocker(year)
# get_allAVG()

def player_ranking(year = 5): #this version uses an overall score to get top player
    dfx = pd.read_csv("enhanced_data.csv")
    topPlayer = None
    topScore = None
    for i, k in dfx.iterrows():
        if int(k["YEARS_PLAYED"]) == int(year):
            score = (k["AST_Z"]  + k["REB_Z"] + k["PTS_Z"] + k["BLK_Z"] + k["STL_Z"] )
            #score = (0.3 *(k["AST_Z"]) + (0.175 * k["REB_Z"]) + (0.175 * k["PTS_Z"]) + (0.175 * k["BLK_Z"]) + (0.175 * k["STL_Z"]))
            # print(f'{k["PLAYER_NAME"]} Score: {score:.1f}')
            if topPlayer is None or score > topScore:
                topPlayer = k
                topScore = score

    # print(f"Best Year {year} Player:\n", topPlayer["PLAYER_NAME"])

    return topPlayer

# player_ranking(5)

def year_rank(year = 2): #This lists all the players in the year in ranking order
    dfx = pd.read_csv("enhanced_data.csv")
    dfx["TOTAL_SCORE"] = (dfx["AST_Z"] +
                             dfx["REB_Z"] +
                             dfx["PTS_Z"] +
                             dfx["BLK_Z"] +
                             dfx["STL_Z"]
                             )

    col = ["PLAYER_NAME","TEAM_ABBREVIATION","TOTAL_SCORE","PTS","REB","AST","BLK","STL","GP",
            "MIN","FG_PCT","PLUS_MINUS","YEARS_PLAYED"]

    allofem = dfx[dfx["YEARS_PLAYED"].astype(int) == int(year)]
    players_ord = allofem.nlargest(len(allofem),"TOTAL_SCORE")[col]
    num = 1
    for i, k in players_ord.iterrows():
        # print(f"{num}th Player: {k["PLAYER_NAME"]} Score: {float(round(k["TOTAL_SCORE"], 2))}")
        num += 1
    return players_ord
# year_rank()

def top10players(): #This list top 10 players regardless of year
    dfx = pd.read_csv("enhanced_data.csv")
    col = ["PLAYER_NAME", "TEAM_ABBREVIATION", "TOTAL_SCORE", "PTS", "REB", "AST", "BLK", "STL", "GP",
           "MIN", "FG_PCT", "PLUS_MINUS", "YEARS_PLAYED", "PTS_Z","REB_Z","AST_Z","BLK_Z","STL_Z"]
    dfx["TOTAL_SCORE"] = (dfx["AST_Z"] +
                             dfx["REB_Z"] +
                             dfx["PTS_Z"] +
                             dfx["BLK_Z"] +
                             dfx["STL_Z"]
         )
    top10 = dfx.nlargest(10,"TOTAL_SCORE")[col]
    num = 1
    for i, k in top10.iterrows():
        #print(f"{num}th Player: {k["PLAYER_NAME"]} Score: {float(round(k["TOTAL_SCORE"],2))}")
        num += 1

    return top10

# top10players()

def top10spec(stat):
    dfx = pd.read_csv("enhanced_data.csv")
    # print(stat)
    col = ["PLAYER_NAME", "TEAM_ABBREVIATION", "PTS", "REB", "AST", "BLK", "STL","YEARS_PLAYED", "GP",
           "MIN", "FG_PCT", "PLUS_MINUS", "PTS_Z", "REB_Z", "AST_Z", "BLK_Z", "STL_Z"]
    # choice = stat
    if(stat == "Points"):
        choice = "PTS_Z"
    if(stat == "Assists"):
        choice = "AST_Z"
    if(stat == "Rebounds"):
        choice = "REB_Z"
    if(stat == "Blocks"):
        choice = "BLK_Z"
    if(stat == "Steals"):
        choice = "STL_Z"

    top10 = dfx.nlargest(10, choice)[col]
    num = 1
    for i, k in top10.iterrows():
        # print(f"{num}th Player: {k["PLAYER_NAME"]} Score: {float(round(k[choice], 2))}")
        num += 1
    return top10

# c= "Blocks"
# top10spec(c)
import pandas as pd
from tabulate import tabulate

input_file = 'cleaned_data.csv'
df = pd.read_csv(input_file)
output_file = 'enhanced_data.csv'
yearsByGroup = df["YEARS_PLAYED"].value_counts()
yearsByGroup = yearsByGroup.sort_index()
# print(yearsByGroup)

# currentYR = (yearsByGroup[2])
# print(currentYR)

def year_avg(year): #this gets the average PPG per YOE
    yr_pts = 0
    yr_reb = 0
    yr_ast = 0
    currentYR = (yearsByGroup[year])
    for i, k in df.iterrows():
        if k["YEARS_PLAYED"] == year:
            yr_pts += k["PTS"]
            yr_reb += k["REB"]
            yr_ast += k["AST"]
            # print(k["PLAYER_NAME"],k["PTS"]),k["REB"],k["AST"])

    #print(f"Year {year} total points: {yr_pts:.1f}")
    yr_av = [float(round(yr_pts / currentYR,1)),
             float(round(yr_reb / currentYR,1)),
             float(round(yr_ast / currentYR))]
    yr_avg = yr_pts / currentYR
    # print(yr_av)
    # print(f"Year {year} average points: {yr_avg:.1f} out of {currentYR} players")
    return yr_av

def get_allAVG(): #this lists all the year specified players and their ppg
    top_yrS  = {"YEARS_PLAYED": 0, "PTS": 0,"REB": 0, "AST": 0}
    top_yrR  = {"YEARS_PLAYED": 0, "PTS": 0,"REB": 0, "AST": 0}
    top_yrA = {"YEARS_PLAYED": 0, "PTS": 0,"REB": 0, "AST": 0}

    for yr,pts in yearsByGroup.items():
        points = year_avg(yr)
        print(f"Year: {yr}, Stats: {points}")

        if top_yrS is None or points[0] > top_yrS["PTS"]: #this is to get the year with highest PPG
            top_yrS["YEARS_PLAYED"] = yr
            top_yrS["PTS"] = float(round(points[0], 1))
        if top_yrR is None or points[1] > top_yrR["REB"]: #this is to get the year with highest REB
            top_yrR["YEARS_PLAYED"] = yr
            top_yrR["REB"] = float(round(points[1], 1))
        if top_yrA is None or points[2] > top_yrA["AST"]: #this is to get the year with highest AST
            top_yrA["YEARS_PLAYED"] = yr
            top_yrA["AST"] = float(round(points[2], 1))

    print(f"Year {top_yrS["YEARS_PLAYED"]} has the highest scoring averages: {top_yrS["PTS"]}")
    print(f"Year {top_yrR["YEARS_PLAYED"]} has the highest rebound averages: {top_yrR["REB"]}")
    print(f"Year {top_yrA["YEARS_PLAYED"]} has the highest assist averages: {top_yrA["AST"]}")



def topScorer(year): #this finds the player who averaged the most points in specified year
    topPlayer = None
    for i, k in df.iterrows():
        if k["YEARS_PLAYED"] == year:
            if topPlayer is None or k["PTS"] > topPlayer["PTS"]:
                topPlayer = k

    print(f"Best Scorer:\n",topPlayer)

def topRebounder(year): #this finds the player who averaged the most rebounds in specified year
    topPlayer = None
    for i, k in df.iterrows():
        if k["YEARS_PLAYED"] == year:
            if topPlayer is None or k["REB"] > topPlayer["REB"]:
                topPlayer = k

    print(f"Best Rebounder:\n",topPlayer)

def topPlaymaker(year): #this finds the player who averaged the most assists in specified year
    topPlayer = None
    d = "AST"
    for i, k in df.iterrows():
        if k["YEARS_PLAYED"] == year:
            if topPlayer is None or k["AST"] > topPlayer["AST"]:
                topPlayer = k

    print(f"Best Playmaker:\n",topPlayer)

year = 2
# year_avg(year)
# topScorer(year)
# topRebounder(year)
#topPlaymaker(year)
# get_allAVG()

def player_ranking(year = 5): #this version uses an overall score to get top player
    topPlayer = None
    for i, k in df.iterrows():
        if k["YEARS_PLAYED"] == year:
            sum = ((k["AST"] * 0.5) +
                   (k["REB"] * 0.25) +
                   (k["PTS"] * 0.25))
            print(f"{k["PLAYER_NAME"]} Score: {sum:.1f}")
            # if topPlayer is None or k["AST"] > topPlayer(sum):
            #     topPlayer = k

    # print(f"Best Playmaker:\n", topPlayer["PLAYER_NAME"])

def player_zscores():
    avg_score = float(round(df["PTS"].mean(),1)) # i should orb leave the round to the end
    avg_reb = float(round(df["REB"].mean(),1))
    avg_ast = float(round(df["AST"].mean(),1))



    print(avg_score, avg_reb, avg_ast)

player_zscores()
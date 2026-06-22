import pandas as pd
from tabulate import tabulate

input_file = 'cleaned_data.csv'
df = pd.read_csv(input_file)

yearsByGroup = df["YEARS_PLAYED"].value_counts()
# print(yearsByGroup)

# currentYR = (yearsByGroup[2])
# print(currentYR)

def year_avg(year):
    yr_tot = 0
    currentYR = (yearsByGroup[year])
    for i, k in df.iterrows():
        if k["YEARS_PLAYED"] == year:
            yr_tot += k["PTS"]
            #print(k["PLAYER_NAME"])

    print(f"Year {year} total points: {yr_tot:.1f}")
    yr_avg = yr_tot / currentYR
    print(f"Year {year} average points: {yr_avg:.1f}")
    return yr_avg

year_avg(5)
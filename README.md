# NBA Career Analytics Project
"Who was the best 5th year player in the 2025-26 NBA season?"

Live demo:
https://nbastatspipeline-site.streamlit.app

This project uses NBA data to build an end-to-end analytics pipeline. The data will be used to make analysis on 
different types of statistics. The main goal is to group each NBA player to either age or different stages in their 
career and identify top performing players. This project extracts NBA data, cleans it up, transforms it, 
stores in a database, and visualizes it.

Experience Explorer:

<img src="assets/Screenshot 2026-07-10 at 2.16.05 PM.png" width="400">

League Leaders:

<img src="assets/Screenshot 2026-07-10 at 2.16.47 PM.png" width="400">

Career Trends: 

<img src="assets/Screenshot 2026-07-10 at 2.17.39 PM.png" width="400">


Data Extraction:
    
    This step involves taking in data for all active NBA player that played during the 2025-2026 season.
    This data was attained using the NBA python api.

Data Cleaning:

    The first step in this portion was to trim down the columns to important to the analysis. For example, stats like 
    total minutes played and total points scored were kept while stats like NBA fantasy points rank were eliminated.
    
    The data was also trimmed for players that did not played a certain amount of time. The minimum was for at least
    30 games played and 20 minutes played. This made the list of players trimmed to around half of original list.
    In this manner, important bench role players to mvp caliber players are kept.

#Data Transformation:

    Originally all stats were extracted as total ammount attained during season. This step transformed that data to be
    game by game averages. 
    The year_experience script comes in and adds a YEARS_PLAYED columns and calculates the years of experience for each 
    player. The FROM_YEAR columns was selected instead of draft year as their may be undrafted players in the data. This
    avoids any errors or mismanaging of data. 

#Analysis:

    This section is where the main opbjective of the project is produced. Questions such as who was the top scorer or 
    rebounder in the 2025-26 season are analyzed here. The scoring average per year of experience is tallied up here
    in this portion. 
    The main task here is to determined who was the best overall player per year according to a standardized 
    performance metric, consisted of points, rebounds,assists, blocks, and steals. This done by adding up the z scores 
    for points, rebounds, assists, blocks, and steals. 
    This section also list who had the highest averages for each stat per year specified. At the end, a list of the top 
    10 players according to the sum of the z scores is generated. This finds top 10 players regardless of year. 

#Visualization:

    Implemented a dashboard interface via Streamlit. 
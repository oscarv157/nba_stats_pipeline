# NBA Career Analytics Project
This project uses NBA data to build an end-to-end analytics pipeline. The data will be used to make analysis on 
different types of statistics. The main goal is to group each NBA player to either age or different stages in their 
career and identify top performing players. This project extracts NBA data, cleans it up, transforms it, 
stores in a database, and visualizes it.

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
import streamlit as st
import pandas as pd
import plotly.express as px

import year_groups as yg

st.title("NBA Career Analytics Project")
st.subheader("Data Analysis Project")
st.text('"Who was the best 5th year player in the 2025-26 NBA season?"')

pro_about = ("This project uses NBA data to build an end-to-end analytics pipeline. The data is used to make "
             "analysis on different types of statistics. The main goal is to group each NBA player to different stages "
             "in their career and identify top performing players. A custom standardized performance metric is "
             "developed to evaluate each player. This project extracts NBA data, cleans it up, transforms it, and "
             "visualizes it.")

st.caption(pro_about)
st.text("Player Eligibility:") #perhaps give a detail about player eligibility here

st.markdown(
    ":violet-badge[:material/check: >= 30 Games played] :blue-badge[:material/check: >= 25 Minutes played] "
    ":green-badge[:material/check: Played during 25-26 Season]"
)

st.text("Project Process:")
st.caption("NBA API :material/arrow_forward: Extraction :material/arrow_forward: Cleaning :material/arrow_forward: "
         "Transform :material/arrow_forward: Analysis :material/arrow_forward: Visualization")

tab1, tab2, tab3, tab4 = st.tabs([
    "Project Insights",
    "Experience Explorer",
    "League Leaders",
    "Career Trends"
])

col_map = {
            "Points": "PTS",
            "Rebounds": "REB",
            "Assists": "AST",
            "Blocks": "BLK",
            "Steals": "STL"
        }

with tab1:
    st.subheader("Behind the Scenes:")
    with st.container(border=True):
        st.markdown("### :blue[:material/arrow_forward_ios: Data Extraction]")
        st.text("Retrieved active player statistics for the 2025–26 NBA season using the NBA Python API.\n"
                "\nCollected player information, season totals, and career experience data.\n"
                "\nCombined data into a unified dataset for analysis.")

    with st.container(border=True):
        st.markdown("### :violet[:material/arrow_forward_ios: Data Cleaning]")
        st.text("Removed unnecessary columns that were not relevant to the analysis.\n"
                "\nReduced the dataset to players with meaningful playing time while preserving both starters and "
                "key rotation players.")

    with st.container(border=True):
        st.markdown("### :green[:material/arrow_forward_ios: Data Transformation]")
        st.text("Converted season totals into per-game averages.\n"
                "\nEngineered new features for statistical analysis.")

    with st.container(border=True):
        st.markdown("### :red[:material/arrow_forward_ios: Data Analysis]")
        st.text("The project explores player performance through several analytical questions:\n"
                "\n- Top scorer by experience year"
                "\n- Top rebounder by experience year"
                "\n- Top playmaker by experience year "
                "\n- Steals leader by experience year"
                "\n- Blocks leader by experience year"
                "\n- Best overall player by experience year")
        st.text("A custom Standardized Performance Metric (SPM) is calculated by combining standardized (z-score) values for "
                "points per games, rebounds per game, assists per game, steals per game, and blocks per game for "
                "each player.")

    with st.container(border=True):
        st.markdown("### :yellow[:material/arrow_forward_ios: Model Interpretation]")
        st.text("SPM is designed to measures a player's all-around production statistics by combining the standardized "
                "values for points, rebounds, assists, blocks, ans steals.\n"
                "\nThis metric focuses on box score production and rankings which may differ from media awards or "
                "expert evaluations that also take advanced analytics into consideration.\n"
                "\nThe goal is to produce a consistent and transparent framework for comparing players.")

    with st.container(border=True):
        st.markdown("### :gray[:material/arrow_forward_ios: Technology]")
        st.markdown("""
                    | | |
                    |---|---|
                    | Language | Python |
                    | Data Source | NBA API |
                    | Data Processing | Pandas |
                    | Graph Visualization | Plotly Express |
                    | Dashboard | Streamlit |
                    """)
with tab2:
    years_list = sorted(yg.yearsByGroup.index.unique())
    selected_year = st.selectbox("Select Year",years_list)

    # print(f"num of players: {yg.yearsByGroup[1]}")

    overall = yg.player_ranking(selected_year)
    topPTS = yg.topScorer(selected_year)
    topREB = yg.topRebounder(selected_year)
    topAST = yg.topPlaymaker(selected_year)
    topBLK = yg.topBlocker(selected_year)
    topSTL = yg.topSteals(selected_year)

    # print(overall["PTS"])
    st.text(f"Top Overall Player for Year {selected_year}:")
    st.subheader(f"{overall["PLAYER_NAME"]}")
    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric('PTS:',overall["PTS"], border=True)
    col2.metric('REB',overall["REB"], border=True)
    col3.metric('AST', overall["AST"], border=True)
    col4.metric('BLK', overall["BLK"], border=True)
    col5.metric('STL', overall["STL"], border=True)

    st.caption(f"Number of Players in Year {selected_year}:  {yg.yearsByGroup[selected_year]}")
    st.markdown(f"Top :green[Scorer] in Year {selected_year} is *{topPTS["PLAYER_NAME"]}* with {topPTS["PTS"]}")
    st.markdown(f"Top :yellow[Rebounder] in Year {selected_year} is *{topREB["PLAYER_NAME"]}* with {topREB["REB"]}")
    st.markdown(f"Top :blue[Playmaker] in Year {selected_year} is *{topAST["PLAYER_NAME"]}* with {topAST["AST"]}")
    st.markdown(f"Top :red[Shot Blocker] in Year {selected_year} is *{topBLK["PLAYER_NAME"]}* with {topBLK["BLK"]}")
    st.markdown(f"Top :violet[Steal Leader] in Year {selected_year} is *{topSTL["PLAYER_NAME"]}* with {topSTL["STL"]}")

    player_list = yg.year_rank(selected_year)
    st.dataframe(player_list)

with tab3:
    option = ['Overall','Points','Rebounds','Assists','Blocks','Steals']
    choices = st.selectbox("Select a stat:",option)

    if choices == 'Overall':
        topOver = yg.top10players()

        melted = topOver.melt(
            id_vars="PLAYER_NAME",
            value_vars=["PTS_Z", "REB_Z", "AST_Z", "BLK_Z", "STL_Z"],
            var_name="Stat",
            value_name="Z-Score"
        )

        player_order = topOver.sort_values("TOTAL_SCORE", ascending=False)["PLAYER_NAME"].tolist()

        fig = px.bar(melted,
                     x="Z-Score",
                     y="PLAYER_NAME",
                     color="Stat",
                     orientation="h",
                     title="Top 10 Overall Players",
                     barmode="stack",
                     category_orders = {"PLAYER_NAME": player_order})

        st.plotly_chart(fig)
        st.dataframe(topOver)



    else:
        st.header(choices)
        topSco = yg.top10spec(choices)

        color_map = {
            "PTS": "#6666FF",
            "REB": "#FF6666",
            "AST": "#00CC99",
            "BLK": "#CC66FF",
            "STL": "#FF9966"
        }

        col_name = col_map[choices]
        player_order = topSco.sort_values(col_name, ascending=False)["PLAYER_NAME"].tolist()

        fig = px.bar(topSco,
                     x=col_name,
                     y="PLAYER_NAME",
                     orientation="h",
                     title=f"Top 10 {choices} Leaders",
                     category_orders={"PLAYER_NAME": player_order},
                     color_discrete_sequence=[color_map[col_name]])

        st.plotly_chart(fig)

        st.dataframe(topSco)

with tab4:
    # st.text("Stat averages per year")
    # option = ['Points', 'Rebounds', 'Assists', 'Blocks', 'Steals']
    # choices = st.selectbox("Select a stat:", option)
    # col_name = col_map[choices]

    top_yrS, top_yrR, top_yrA, top_yrB, top_yrST, yearly_df = yg.get_allAVG()
    st.subheader("Best Year Per Stat")
    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Top Scoring Year", f"Year {top_yrS['YEARS_PLAYED']}", f"{top_yrS['PTS']} PPG")
    col2.metric("Top Rebound Year", f"Year {top_yrR['YEARS_PLAYED']}", f"{top_yrR['REB']} RPG")
    col3.metric("Top Assist Year", f"Year {top_yrA['YEARS_PLAYED']}", f"{top_yrA['AST']} APG")
    col4.metric("Top Block Year", f"Year {top_yrB['YEARS_PLAYED']}", f"{top_yrB['BLK']} BPG")
    col5.metric("Top Steal Year", f"Year {top_yrST['YEARS_PLAYED']}", f"{top_yrST['STL']} SPG")

    options = ['Points', 'Rebounds', 'Assists', 'Blocks', 'Steals']
    selected_stat = st.selectbox("Select a stat:", options)
    col_name = col_map[selected_stat]
    fig = px.line(yearly_df,
                  x="YEARS_PLAYED",
                  y=col_name
                  )
    st.plotly_chart(fig) #THE METRIC ISNT DISPLAYING THE CORRECT BLOCK AND STEAL YEAR!!!!!!!!!!!


    st.subheader("Averages by Year")
    st.dataframe(yearly_df, hide_index=True)





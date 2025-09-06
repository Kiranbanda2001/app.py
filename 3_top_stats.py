import streamlit as st
import pandas as pd
import plotly.express as px
from utils.db_connection import get_engine

@st.cache_data # Cache the player data
def fetch_players_data():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM players", engine)
    return df

st.header("📈 Top Players & Analytics")

player_df = fetch_players_data()

if not player_df.empty:
    st.dataframe(player_df.sort_values(by="runs", ascending=False), hide_index=True)
    
    st.markdown("---")
    
    st.subheader("Runs Comparison")
    fig = px.bar(player_df.sort_values(by="runs", ascending=False).head(10), 
                 x="name", 
                 y="runs", 
                 title="Top 10 Players by Runs",
                 labels={"name": "Player", "runs": "Total Runs"})
    st.plotly_chart(fig)
else:
    st.info("No player data available. Use the Admin page to add players.")
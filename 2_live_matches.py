import streamlit as st
from utils.api_handler import fetch_live_scores

st.title("📊 Live Matches")

data = fetch_live_scores()

if not data:
    st.warning("No live matches available right now.")
else:
    for match in data.get("matches", []):
        info = match.get("matchInfo", {})
        score = match.get("matchScore", {})

        team1 = info.get("team1", {}).get("teamName", "Team 1")
        team2 = info.get("team2", {}).get("teamName", "Team 2")

        st.subheader(f"{team1} vs {team2}")
        st.json(score)  # for now, raw score display
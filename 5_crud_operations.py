import streamlit as st
from sqlalchemy import Table, Column, Integer, String, MetaData, insert, select
from utils.db_connection import get_engine

engine = get_engine()
metadata = MetaData()

players = Table('players', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('team', String),
    Column('matches', Integer),
    Column('runs', Integer)
)

metadata.create_all(engine)

st.title("🛠️ Player Analytics CRUD")

# --- Add Player ---
with st.form("add_player"):
    name = st.text_input("Name")
    team = st.text_input("Team")
    matches = st.number_input("Matches", min_value=0)
    runs = st.number_input("Runs", min_value=0)
    submitted = st.form_submit_button("Add Player")
    if submitted:
        try:
            engine.execute(insert(players).values(name=name, team=team, matches=matches, runs=runs))
            st.success(f"Player {name} added successfully!")
        except Exception as e:
            st.error(f"Error: {e}")

# --- View Players ---
st.subheader("📋 Current Players in DB")
result = engine.execute(select(players))
df = pd.DataFrame(result.fetchall(), columns=result.keys())
st.dataframe(df)

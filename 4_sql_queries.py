import streamlit as st
import pandas as pd
from utils.db_connection import get_engine

engine = get_engine()

st.title("📋 SQL Query Interface")
query = st.text_area("Enter your SQL query")

if st.button("Run"):
    try:
        result = engine.execute(query)
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        st.dataframe(df)
    except Exception as e:
        st.error(f"SQL Error: {e}")

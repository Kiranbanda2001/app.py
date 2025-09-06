import requests
import streamlit as st

API_HOST = "cricbuzz-cricket.p.rapidapi.com"
API_KEY = "67e277c289msh8d5cc9c18787256p1b027fjsnad69f0ac51a0"

HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}

BASE_URL = "https://cricbuzz-cricket.p.rapidapi.com"

def fetch_api(endpoint: str):
    """Generic API fetcher with error handling"""
    try:
        url = f"{BASE_URL}{endpoint}"
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API Error: {e}")
        return {}

def fetch_live_scores():
    return fetch_api("/matches/v1/live")

def fetch_series():
    return fetch_api("/series/v1/international")

# minimal redeploy-ready NFL EV app
import streamlit as st
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

st.title("NFL +EV Bets (Minimal Version)")

# Example placeholder table
st.write("This is a placeholder for top +EV bets:")

# Create a sample dataframe
sample_data = {
    "match": ["Team A @ Team B", "Team C @ Team D"],
    "team": ["Team A", "Team C"],
    "odds": [150, -120],
    "model_prob": [0.55, 0.60],
    "alpha": [0.05, 0.08],
}

df = pd.DataFrame(sample_data)

st.table(df)

# Optional: show a simple confirmation that app is live
st.text("App deployed successfully!")

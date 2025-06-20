# https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y3JpY2tldCUyMHN0YWRpdW18ZW58MHx8MHx8fDA%3D

import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load the trained pipeline
pipe = pickle.load(
    open('pipe.pkl', 'rb'))

# Set up the page
st.set_page_config(page_title="IPL Predictor", layout="wide")

# IPL Logo and Title
st.markdown("""
    <div style='text-align: center;'>
        <img src='https://brandlogos.net/wp-content/uploads/2025/05/tata_ipl-logo_brandlogos.net_k2ryd.png' width='180'/>
        <h1 style='color: white; text-shadow: 2px 2px black;'>IPL Win Predictor</h1>
    </div>
""", unsafe_allow_html=True)

# Teams and Cities
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]

cities = sorted([
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
])

# Input: Match Setup
st.markdown("## ⚔️ Match Setup")
col1, col2, col3 = st.columns(3)

with col1:
    batting_team = st.selectbox('🏏 Batting Team', teams)
with col2:
    bowling_team = st.selectbox(
        '🎯 Bowling Team', [team for team in teams if team != batting_team])
with col3:
    selected_city = st.selectbox('📍 Match City', cities)

# Input: Match Situation
st.markdown("## 📊 Match Situation")
target = st.number_input('🎯 Target Score', min_value=0)

col4, col5, col6 = st.columns(3)
with col4:
    score = st.number_input('🏏 Current Score', min_value=0)
with col5:
    wickets = st.number_input('❌ Wickets Fallen', min_value=0, max_value=9)
with col6:
    overs = st.number_input('⏱ Overs Completed',
                            min_value=0.0, max_value=20.0, step=0.1)

# Predict button
if st.button("🔮 Predict Win Probability"):

    # Feature Engineering
    runs_left = target - score
    balls_left = 120 - overs * 6
    wickets_left = 10 - wickets
    crr = score / overs if overs > 0 else 0
    rrr = (runs_left * 6 / balls_left) if balls_left > 0 else 0

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets_left],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    # Predict
    result = pipe.predict_proba(input_df)
    win_percent = round(result[0][1] * 100)
    lose_percent = 100 - win_percent

    # Display Results
    st.markdown("## 🏆 Prediction Result")
    st.success(f"**{batting_team}** Win Chance: **{win_percent}%**")
    st.error(f"**{bowling_team}** Win Chance: **{lose_percent}%**")

    # Extra: image below manage the size 
    st.image("https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y3JpY2tldCUyMHN0YWRpdW18ZW58MHx8MHx8fDA%3D", use_column_width=True, width=500)

    # Display the slogan 
    st.markdown("""
        <h2 style='text-align: center; color: white; text-shadow: 2px 2px black;'>
            "Crciket is not just a game, it's an emotion!"
        </h2>
    """, unsafe_allow_html=True)

# Styling
st.markdown("""
    <style>
    .stSelectbox label, .stNumberInput label {
        font-weight: bold;
        color: white;
    }
    .stButton>button {
        background-color: #f12711;
        background-image: linear-gradient(315deg, #f12711 0%, #f5af19 74%);
        color: white;
        font-weight: bold;
        font-size: 1rem;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

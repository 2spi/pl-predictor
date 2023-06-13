import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

pipe = pickle.load(open('./model/pipe.pkl','rb'))

clubs = ['Aston Villa', 'Manchester United', 'Leeds United', 'Arsenal',
        'Liverpool', 'Chelsea', 'West Ham United', 'Crystal Palace',
        'Tottenham Hotspur', 'Southampton', 'Newcastle United',
        'Sheffield United', 'Fulham', 'Brighton and Hove Albion',
        'Norwich City', 'Leicester City', 'Manchester City',
        'Wolverhampton Wanderers', 'Brentford', 'Nottingham Forest',
        'Burnley', 'Everton', 'Bournemouth', 'West Bromwich Albion',
        'Watford']

opponent_clubs = ['Leeds United', 'Arsenal', 'Everton', 'Leicester City',
       'Tottenham', 'Watford', 'Bournemouth', "Nott'ham Forest",
       'Aston Villa', 'Burnley', 'Manchester City', 'West Brom', 'Wolves',
       'Sheffield Utd', 'Manchester Utd', 'Crystal Palace', 'Chelsea',
       'Newcastle Utd', 'Brentford', 'Fulham', 'Brighton', 'Southampton',
       'Liverpool', 'West Ham', 'Norwich City']

home_away = ['Home', 'Away']

st.title('Premier League Result Prediction')

club = st.selectbox('Select the club',sorted(clubs))
opponent = st.selectbox('Select opposition', sorted(opponent_clubs))

col1, col2, col3 = st.columns(3)

with col1:
    venue = st.selectbox('Venue', home_away)
with col2:
    gf = st.number_input('Goals scored in the last 3 games')
with col3:
    ga = st.number_input('Goals conceded in the last 3 games')

if st.button('Predict Win Percentage'):
    input_df = pd.DataFrame({
        'club': [club], 'opponent': [opponent], 'venue': [venue], 'gf_rolling':[gf], 'ga_rolling':[ga]
    })
    result = pipe.predict_proba(input_df)[0][1] * 100
    st.header("Win percentage - " + str(result))


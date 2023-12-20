import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipe_xgb.pkl','rb'))

teams =  ['England', 'Pakistan', 'Sri Lanka', 'Australia', 'South Africa',
       'New Zealand', 'Bangladesh', 'West Indies', 'India',
       'Afghanistan','Zimbabwe','Ireland',]

venue = ['Old Trafford', 'New Wanderers Stadium', 'Trent Bridge',
       'Shere Bangla National Stadium', 'Rawalpindi Cricket Stadium',
       'Hagley Oval', 'Dubai International Cricket Stadium',
       'Kennington Oval', 'R Premadasa Stadium', 'Newlands',
       'Zayed Cricket Stadium', 'Feroz Shah Kotla',
       'Sharjah Cricket Stadium', 'Gaddafi Stadium',
       'Rajiv Gandhi International Cricket Stadium',
       'Sheikh Abu Naser Stadium', 'Eden Park',
       'Civil Service Cricket Club', 'The Wanderers Stadium',
       'Beausejour Stadium', 'Perth Stadium', 'Bay Oval',
       'Saurashtra Cricket Association Stadium',
       'Maharashtra Cricket Association Stadium',
       'Zahur Ahmed Chowdhury Stadium',
       'Punjab Cricket Association IS Bindra Stadium',
       'Melbourne Cricket Ground', 'Carrara Oval',
       'Himachal Pradesh Cricket Association Stadium',
       'Harare Sports Club', 'Punjab Cricket Association Stadium',
       'Vidarbha Cricket Association Stadium', 'Narendra Modi Stadium',
       'Westpac Stadium', 'The Rose Bowl',
       'Central Broward Regional Park Stadium Turf Ground',
       'Mahinda Rajapaksa International Cricket Stadium', 'Seddon Park',
       'Brisbane Cricket Ground', 'Bellerive Oval', 'Kensington Oval',
       'OUTsurance Oval', 'Kingsmead', 'The Village',
       'Sir Vivian Richards Stadium', 'Sabina Park',
       'Sydney Cricket Ground', 'Brian Lara Stadium', 'John Davies Oval',
       'SuperSport Park', 'Barabati Stadium', "St George's Park",
       'Arnos Vale Ground', 'National Stadium', 'Providence Stadium',
       'Windsor Park', "Lord's", 'Moses Mabhida Stadium',
       'R.Premadasa Stadium', "Queen's Park Oval", 'Wankhede Stadium',
       'Stadium Australia', 'Pallekele International Cricket Stadium',
       'Warner Park', 'AMI Stadium',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium',
       'Sophia Gardens', 'Sky Stadium', 'Sardar Patel Stadium',
       'Castle Avenue', 'M Chinnaswamy Stadium', 'Sheikh Zayed Stadium',
       'Subrata Roy Sahara Stadium',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'Eden Gardens', 'Saxton Oval', 'Holkar Cricket Stadium',
       'Edgbaston', 'Greater Noida Sports Complex Ground',
       'Barsapara Cricket Stadium', 'Queens Sports Club', 'County Ground',
       'Riverside Ground', 'National Cricket Stadium', 'Boland Park',
       'Senwes Park', 'Arun Jaitley Stadium', 'Adelaide Oval',
       'Coolidge Cricket Ground', 'Darren Sammy National Cricket Stadium',
       'McLean Park', 'Green Park', 'Greenfield International Stadium',
       'Buffalo Park', 'Bready Cricket Club',
       'Sylhet International Cricket Stadium', 'Manuka Oval',
       'University Oval', 'Western Australia Cricket Association Ground',
       'Jade Stadium', 'JSCA International Stadium Complex',
       'Maple Leaf North-West Ground', 'Simonds Stadium',
       'De Beers Diamond Oval', 'Rajiv Gandhi International Stadium',
       'Headingley', 'MA Chidambaram Stadium', 'Malahide',
       'M.Chinnaswamy Stadium', 'Sawai Mansingh Stadium',
       'Brabourne Stadium', 'Mangaung Oval', 'Gymkhana Club Ground',
       'Sylhet Stadium']

st.title('T20_Score_Predictor')

col1,col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Please select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Please select the bowling team',sorted(teams))

Venue = st.selectbox('Please select the Venue',sorted(venue))   


col3,col4,col5 = st.columns(3)
with col3:
    current_overs = st.number_input('Please enter Current Over(overs>3)')
with col4:
    current_score = st.number_input('Please enter Current Score')
with col5:
    current_wickets= st.number_input('Please enter Current Wickets')

runs_3ov = st.number_input('Please Enter last 3_overs Runs')
wickets_3ov = st.number_input('Please Enter last 3_overs wickets')

if st.button('Predict score'):

    crr = current_score/current_overs

    input_df = pd.DataFrame(
     {'bat_team': [batting_team], 'bowl_team': [bowling_team],
      'Venue': [Venue], 'cur_overs': [current_overs], 'cur_runs': [current_score],
      'cur_wickets': [current_wickets],
      'crr': [crr],'wickets_last_3ov': [wickets_3ov] ,'runs_last_3ov': [runs_3ov]})
    

    result = pipe.predict(input_df)
    st.header("Predicted Score : "+str(int(result[0])))


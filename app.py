import streamlit as st

from data import load_data
from ratings import update_ratings
from model import expected_goals
from engine import simulate

st.title("⚽ CADIEBET V5 FINAL ENGINE")

df = load_data()
ratings = update_ratings(df)

teams = list(ratings.keys())

home = st.selectbox("Local", teams)
away = st.selectbox("Visitante", teams)

r_h = ratings[home]
r_a = ratings[away]

if st.button("Analizar partido"):

    xg_h, xg_a = expected_goals(r_h, r_a)

    sim = simulate(xg_h, xg_a)

    st.subheader("📊 Predicción")

    st.write("xG:", round(xg_h,2), "-", round(xg_a,2))

    st.write("Prob Local:", round(sim["H"],2))
    st.write("Prob Empate:", round(sim["D"],2))
    st.write("Prob Visitante:", round(sim["A"],2))

    st.write("Rating:", round(r_h,0), "-", round(r_a,0))

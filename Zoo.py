# app.py, run with 'streamlit run app.py'
import pandas as pd
import streamlit as st

zoo = pd.read_csv("./Zoo.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files

st.title("Hi, This is my first app!")  # add a title
st.write(zoo)  # visualize my dataframe in the Streamlit app

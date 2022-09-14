import pandas as pd
import streamlit as st

mc = pd.read_csv("./k-means-clustering/mall_customer.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files

st.title("Hi, This is a dataset of Mall customers!")  # add a title
st.write(mc)  # visualize my dataframe in the Streamlit app

st.line_chart(mc)
st.altair_chart(mc)

import pandas as pd
import streamlit as st

file = "/content/mall_customer (1).csv"

zoo = pd.read_csv("./k-means-clustering/mall_customer.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files

st.title("Hi, This is a dataset of Mall customers!")  # add a title
st.write(zoo)  # visualize my dataframe in the Streamlit app

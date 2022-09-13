import streamlit as st
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

zoo = pd.read_csv("zoo.csv")
zoo = pd.read_csv("https://github.com/zuhairahbasri/Python-Class/blob/main/Zoo.csv")
st.title("Zoo Dataset")
st.write(zoo) 

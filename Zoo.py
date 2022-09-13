import streamlit as st
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings 
warnings.filterwarnings("ignore")

import os
print(os.listdir("../input"))

class_ = pd.read_csv("../input/class.csv")
zoo = pd.read_csv("../input/zoo.csv")

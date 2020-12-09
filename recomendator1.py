# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:13:06 2020

@author: Ernesto
"""
import sklearn
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


vinotfidf = pd.read_csv('vino_var_sab.csv')

st.title('Wine Recommender')

st.write(vinotfidf)


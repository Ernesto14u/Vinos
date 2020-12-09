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

st.slider('sweet:', 1, 10, 1)
st.slider('dry:', 1, 10, 1)
st.slider('character:', 1, 10, 1)
st.slider('soft:', 1, 10, 1)
st.slider('fresh:', 1, 10, 1)
st.slider('spice:', 1, 10, 1)
st.slider('cherry:', 1, 10, 1)
st.slider('strawberry:', 1, 10, 1)
st.slider('apple:', 1, 10, 1)
st.slider('plum:', 1, 10, 1)
st.slider('cinnamon:', 1, 10, 1)
st.slider('vanilla:', 1, 10, 1) 
st.slider('herb:', 1, 10, 1) 
st.slider('oak:', 1, 10, 1)        
              
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


vinotfidf = pd.read_csv('dfcito.csv')

st.title('Wine Recommender')
color=st.selectbox("Select the color of your wine variety desired", ('Red','Rose','White', 'It´s the same'))
if color !='It´s the same':
    vinotfidf= vinotfidf.loc[vinotfidf['Color']== color]
respuestas = list()


st.subheader('Let´s find the variety of wine that most closely matches your tastes')
st.warning('1: is Don´t like and 5 is: Love it')

st.succes('Apple')
respuestas.append(st.slider('', 1, 5, 1))
st.info('Character')
respuestas.append(st.slider('', 1, 5, 1))
respuestas.append(st.slider('cherry:', 1, 5, 1))
respuestas.append(st.slider('cinnamon:', 1, 5, 1))
respuestas.append(st.slider('dry:', 1, 5, 1))
respuestas.append(st.slider('fresh:', 1, 5, 1))
respuestas.append(st.slider('herb:', 1, 5, 1))
respuestas.append(st.slider('oak:', 1, 5, 1))
respuestas.append(st.slider('plum:', 1, 5, 1))
respuestas.append(st.slider('soft:', 1, 5, 1))
respuestas.append(st.slider('spice:', 1, 5, 1))
respuestas.append(st.slider('strawberry:', 1, 5, 1)) 
respuestas.append(st.slider('sweet:', 1, 5, 1))
respuestas.append(st.slider('vanilla:', 1, 5, 1))        
              

algo=vinotfidf.iloc[:,2:-1].values
multiplicación_de_matriz=algo*np.array(respuestas)
salida = np.sum(multiplicación_de_matriz, axis=1)
index_max= np.argmax(salida)
vino_favorito=vinotfidf.iloc[index_max  ,1]
st.write(vino_favorito)



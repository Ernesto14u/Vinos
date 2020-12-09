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
color=st.selectbox("Qué color de vino prefieres?", ('Red','Rose','White', 'It`s the same'))
if color !='It`s the same':
    vinotfidf= vinotfidf.loc[vinotfidf['Colour']== color]
respuestas = list()
st.subheader('Crea tu vino')
respuestas.append(st.slider('apple:', 1, 10, 1))
respuestas.append(st.slider('character:', 1, 10, 1))
respuestas.append(st.slider('cherry:', 1, 10, 1))
respuestas.append(st.slider('cinnamon:', 1, 10, 1))
respuestas.append(st.slider('dry:', 1, 10, 1))
respuestas.append(st.slider('fresh:', 1, 10, 1))
respuestas.append(st.slider('herb:', 1, 10, 1))
respuestas.append(st.slider('oak:', 1, 10, 1))
respuestas.append(st.slider('plum:', 1, 10, 1))
respuestas.append(st.slider('soft:', 1, 10, 1))
respuestas.append(st.slider('spice:', 1, 10, 1))
respuestas.append(st.slider('strawberry:', 1, 10, 1)) 
respuestas.append(st.slider('sweet:', 1, 10, 1))
respuestas.append(st.slider('vanilla:', 1, 10, 1))        
              
st.write(respuestas)

multiplicación_de_matriz=vinotfidf.iloc([2:-4])*respuestas
salida = np.sum(multiplicación_de_matriz, axis=1)
index_max= np.argmax(salida)
variedad[index_max]
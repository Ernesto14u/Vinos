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
st.info('First of all, select the colour of the wine')
color=st.selectbox("Choose one", ('Red','Rose','White', 'It´s the same'))
if color !='It´s the same':
    vinotfidf= vinotfidf.loc[vinotfidf['Color']== color]
respuestas = list()


st.error('Let´s find the variety of wine that most closely matches your tastes')
st.warning('       From 1 to 5     --------      (1) Don´t like it       --------      (5)  Love it')
st.subheader('Let´s play now!!')
st.success('Apple')
respuestas.append(st.slider('Manzana', 1, 5, 1))
st.info('Character')
respuestas.append(st.slider('Carácter', 1, 5, 1))
st.warning('Cherry')
respuestas.append(st.slider('Cereza', 1, 5, 1))
st.error('Cinnamon')
respuestas.append(st.slider('Canela', 1, 5, 1))
st.success('Dry')
respuestas.append(st.slider('Seco', 1, 5, 1))
st.info('Fresh')
respuestas.append(st.slider('Fresco, Ligero', 1, 5, 1))
st.warning('Herb')
respuestas.append(st.slider('Herbal', 1, 5, 1))
st.error('Oak')
respuestas.append(st.slider('Roble', 1, 5, 1))
st.success('Plum')
respuestas.append(st.slider('Ciruela', 1, 5, 1))
st.info('Soft')
respuestas.append(st.slider('Suave, Delicado', 1, 5, 1))
st.warning('Spice')
respuestas.append(st.slider('Picante', 1, 5, 1))
st.error('Strawberry')
respuestas.append(st.slider('Frutillas', 1, 5, 1)) 
st.success('Sweet')
respuestas.append(st.slider('Dulce', 1, 5, 1))
st.info('Vanilla')
respuestas.append(st.slider('Vainilla', 1, 5, 1))        
              

algo=vinotfidf.iloc[:,2:-1].values
multiplicación_de_matriz=algo*np.array(respuestas)
salida = np.sum(multiplicación_de_matriz, axis=1)
index_max= np.argmax(salida)
vino_favorito=vinotfidf.iloc[index_max  ,1]
st.title('La variedad de vino que buscas es:')
st.subheader(vino_favorito)



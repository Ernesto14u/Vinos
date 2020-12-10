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
from PIL import Image
image = Image.open('Vino.jpg')
image1 = Image.open('Vino2.jpg')
image2 = Image.open('Vino1.jpg')
vinotfidf = pd.read_csv('dfcito.csv')
vino = pd.read_csv('mis_vinos.csv')


st.title('Wine Recommender')
st.image(image,width=700)
st.subheader('Let´s find the wine variety that most closely matches your taste!')


st.warning('First of all, select the colour of the wine')
st.image(image1,width=300)
color=st.selectbox("Selecciona el color", ('Red','Rose','White', 'It´s the same'))
if color !='It´s the same':
    vinotfidf= vinotfidf.loc[vinotfidf['Color']== color]



respuestas = list()

st.subheader('NOW ...Start your taste trip!!')
st.info('From 1 to 5     --------      (1) Don´t like it       --------      (5)  Love it')
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
st.title('Finally... ')
st.image(image2,width=700)
st.title('The wine variety that best suits your taste is:')
st.subheader(vino_favorito)
###########

vino.set_index('Wine Id', inplace=True)
variedad = vino['Variety'].unique()
Varie=variedad[index_max]

reco_wine = vino.loc[vino['Variety'] == vino_favorito]
reco_wine1=reco_wine.iloc[0].Title 
reco_wine2=reco_wine.iloc[1].Title 
reco_wine3=reco_wine.iloc[5].Title 

st.text(reco_wine1)
st.text(reco_wine2)
st.text(reco_wine3)

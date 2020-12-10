# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:50:52 2020

@author: Ernesto
"""

import sklearn
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer


vino = pd.read_excel('vino.xlsx')
vino.set_index('Wine Id', inplace=True)

# Función para ponerle la caliad al vino, mediante sus puntos, en una nueva columna
def nuevafun(a):
   if a>=95 :
       return(" Excepcional")
   elif(a>=90) and (a< 95):
       return(" Excelente")
   elif(a>=80) and (a< 90):
       return(" Muy Bueno")
   else:
       return("No Compiten")


vino['Rank']= vino['Points'].apply(nuevafun)

vino['Year'].fillna(vino['Year'].mode()[0], inplace=True)

vino =vino.dropna()

#Prueba recomendador

#Nos quedamos sólo con la columna description

#descriptions = vino.description
sabores = ['cherry','spice','apple','sweet','fresh',
           'strawberry','cinnamon','herb','oak','vanilla',
           'dry','plum','character','soft']

variedad = vino['Variety'].unique()

mi_lista=[]
for variety in variedad:
    tipo_vino = vino.loc[vino['Variety']== variety]   
    descriptions = tipo_vino['Description'].str.lower().str.cat(sep=' ')
    descriptions = descriptions.replace(",", " ")
    descriptions = descriptions.replace("."," ")
    descriptions = descriptions.split()
    
    descriptions = filter(lambda w: w in sabores, descriptions)
                    
    descriptions = list(descriptions)
    
    descriptions =  " ".join(descriptions)
    
    mi_lista.append(descriptions)
    
    
# ln(N+1/df+1) +1


test = TfidfVectorizer()
matriz_tfidf = test.fit_transform(mi_lista)


col = test.get_feature_names()

val =matriz_tfidf.A 

vino_var_sab = pd.DataFrame(val, index=variedad, columns= col)
vino_var_sab.reset_index(inplace=True)

vinotfidf['Colour'] = vino_var_sab.iloc[:,-1].values 

vino_var_sab.to_csv('vino_var_sab.csv')

  

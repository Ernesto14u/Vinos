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
sabores = ['cherry','spice','apple','sweet','fresh','smoky',
           'cinnamon','herb','tobacco','vanilla','berry','dry',
           'plum','blend','character','aromatic','soft']

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
    
    from sklearn.feature_extraction.text import TfidfVectorizer
# ln(N+1/df+1) +1


test = TfidfVectorizer()
matriz_tfidf = test.fit_transform(mi_lista)


col = test.get_feature_names()

val =matriz_tfidf.A 

vino_var_sab = pd.DataFrame(val, index=variedad, columns= col)

vector=np.array([4,3,0,2,3,3,3,5,5,4,4,1,1,0,0,4,4])

multiplicación_de_matriz = matriz_tfidf.A*vector

salida = np.sum(multiplicación_de_matriz, axis=1)

index_max= np.argmax(salida)


variedad[index_max]




"""
@author: Fábio Mori
"""

#Escola Matriz - Class 29: NETFLIX

#Import the libraries
import numpy as np
from math import sqrt
from math import dist

#Define the function that calculates the similarity between two users
def euclidiano (usuario1, usuario2):
    dist_inv=1/(1+dist(usuario1,usuario2))
    return dist_inv

#Import .csv ratings files of films that you watched 
filmes_vistos=np.array([])
filmes_vistos=np.loadtxt('vistos_netflix.csv',
                 delimiter=',',
                 unpack=True,
                 dtype='str')

#Import .csv ratings files of films that you did not watch
filmes_novos=np.array([])
filmes_novos=np.loadtxt('novos_netflix.csv',
                 delimiter=',',
                 unpack=True,
                 dtype='str')

#Transform datas into arrays
notas=filmes_vistos[1:,1:]
notas=notas.astype(float)
notas_taina=np.transpose(filmes_novos[1,1:])
notas_taina=notas_taina.astype(float)

#Calculating the similarity
fabio=notas[0,:]
taina=notas[1,:]
similaridade=euclidiano(fabio,taina)

#Calculating the recomendation throught of linear combination
recomendacao=notas_taina*similaridade

#Print the result
print('Os filmes recomendados para você pela Tainá são:')
for i in range (np.size(recomendacao)):
    x=recomendacao[i]
    if x>=0.5:
        print(filmes_novos[0,(i+1)])
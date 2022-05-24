"""
@author: Fábio Mori
"""

#Escola Matriz - Class 28: Economy and Stock Market

#Import the libraries
import numpy as np
from numpy import linalg as linalg

#Create matrices and solving a linear system
A=np.array([[0.12, 0.04, 0.01], [1, 1, 1],[1, -1, -1]])
b=np.array([[2625],[37500],[0]])
x=linalg.solve(A,b)

#Print the answer of linear system
print('Para obter o retorno desejado é necessário investir:\n',
      'R$', round(x[0,0]), 'em empresas de baixo crescimento\n',
      'R$', round(x[1,0]), 'em empresas de médio crescimento\n',
      'R$', round(x[2,0]), 'em empresas de alto crescimento')

            
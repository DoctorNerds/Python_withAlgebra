"""
@author: Fábio Mori
"""

#Escola Matriz - Class 21: Programming Linear Algebra

#Import libraries into the algorthim
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#Explore this functions on oficial website Numpy
#Documentation - Tutorials - Data types
#Documentation - Tutorials - Array creation
#Documentation - Tutorials - Numpy for Matlab users
#Documentation - Numpy Reference - Array objects
#Documentation - Numpy Reference - Linear Algebra

#Criate arrays and matrices with Numpy
x1=np.array([[2],[1],[5]])   #column vector
x2=np.array([1, 2, 4, 5, 6, 9]) #column vector
x3=np.array([[1, 2, 4, 5, 6, 9]])  #row vector
x4=np.array([[1, 2, 4],[5, 6, 9],[6, 5, 1]])  #matrix 3x3
x5=np.array([[1, 11, 4, 5, 9], [3, 1, 1, 0, 0], [8, 8, 1, 8, 2]])  #matrix 3x5

#Arithimetic operations with arrays and matrices with Numpy
c1=np.array([1, 4, 6])
c2=np.array([3, 5, 9])
c3=c1+c2                        #sum of column vectors
c4=np.array([[1, 2, 4]])
c5=np.array([[4, 4, 2]])
c6=c4+c5                        #sum of row vectors
c7=c4*c5                        #multiplication of row vectors
m1=np.array([[1, 4, 0], [3, 9, 1], [4, 3, 1]])
m2=np.array([[3, 3, 2], [3, 4, 4], [5, 2, 1]])
m3=m1+m2                        #sum of matrices
m4=m1-m2                        #subtraction of matrices
m5=m1*m2                        #multiplication of matrices
m6=m1/m2                        #division of matrices

#Explore this functions on oficial website Matplotlib
#Documentation - Tutorials - Pyplot tutorial

#Exemple 1
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

#Exemple 2
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

#Exemple 3
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

#Exemple 4
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()





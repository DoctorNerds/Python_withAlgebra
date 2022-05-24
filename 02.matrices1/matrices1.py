"""
@author: Fábio Mori
"""

#Escola Matriz - Class 22: Matrices I

#Import libraries into the algorthim
import numpy as np

#Criate diagonal matrix, indentity, null and their transposes
x=np.arange(1, 10, 3)
diag=np.diag(x)
iden=np.eye(4, dtype=int)
null=np.zeros((3,3))
tdiag=np.transpose(diag)
tiden=np.transpose(iden)
tnull=np.transpose(null)

#Operation with matrices 4x4
A=np.array([[2, 3, 2, 1], [3, 4, 3, 2], [3, 4, 3, 1 ], [0, 1, 0, 4]])
B=np.array([[0, 3, 0, 5], [1, 1, 0, 2], [3, 3, 2, 0 ], [0, 0, 0, 1]])
ind1=A[0,:]+B[2,:]
ind2=B[:,0]-A[:,1]
soma=A+B
sub=A-B
k=2
esc=k*A
mult1=A*B
mult2=A.dot(B)





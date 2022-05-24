"""
@author: Fábio Mori
"""

#Escola Matriz - Class 27: Message Encryption

#Importing libraries
import numpy as np
from numpy import linalg as linalg

#Function for cryptography
def converter_numeros(texto):
    seq_num = []
    #Ensuring even number of characters in the message
    if(len(texto)%2 != 0):
        texto += ' '
    #Convert characters in numbers throught the table
    for i in texto:
        for j in tab:
            if(tab[j]==i):
                seq_num.append(j)
    return seq_num

def converter_texto(numero):
    mensagem = ''
    for i in numero:
        mensagem += str(tab[round(i)])
    return mensagem

#Matrix for encryption a message [C*A]
Ce = np.array(([7,4],[2,6]))

#Matrix for decrypt a message [C*A*C^-1]
Cd = np.linalg.inv(Ce)

#Simplified ASCII table for this example
tab = {1:'A', 2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',
       9:'I',10:'J',11:'K', 12:'L',13:'M',14:'N',15:'O',
       16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',
       23:'W',24:'X',25:'Y',26:'Z',27:'.',28:',',29:'?',
       30:'!',31:' ',32:';', 33:'@', 34:'&', 35:'%', 36:'#'}

#Read a message from sender
mensagem_rem=input('Digite uma mensagem: ')

#Convert characters in numbers
seq_num=converter_numeros(mensagem_rem)

#Convert into array for operation with Numpy
seq_num = np.array(seq_num)  
                
#Convert into matrix for operation with Ce(2x2)
mat_num = seq_num.reshape(2,int(seq_num.size/2))

#Encrypt the message
encrip = Ce.dot(mat_num) 
                   
#Decrypt the message
decrip = Cd.dot(encrip) 
                   
#Convert into array for use simplified ASCII 
seq_num2 = decrip.reshape(1,decrip.size)

#Decrypted message to addressee
mensagem_dest=converter_texto(seq_num2[0,:])

#Print the decrypted message that addressee will see
print(mensagem_rem)

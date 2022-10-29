# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:42:13 2019

@author: USUARIO
"""

filename = input("Enter file name: ")
filehandle = open(filename)
dictio = dict()

#Ciclo para encontrar correo que se repite con
#mayor frecuencia, despues de la palabra From
#usando la funcion diccionario

for X in filehandle:
    if "From" in X:
        especificword = X.split()
        if especificword[0] == "From":
            email = especificword[1]
            dictio[email] = dictio.get(email,0)+1

bigcount = None
bigword = None
for key,value in dictio.items():
    if (bigcount is None) or (value > bigcount):
        bigcount = value
        bigword = key
print(bigword, bigcount)
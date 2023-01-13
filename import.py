import pickle

import Serializar_objetos 

"""Rescatar la info que hay en el ficherdClaseVehiculos"""

ficheroApertura=open("FicherdClaseVehiculos", "rb")#Se abre el fichero con rb= lectura de binario
lista_coches=pickle.load(ficheroApertura)#guardo en la variable lista lo que se carga del metodo pickle.load que jala de la variable en 
#memoria ficheroApertura
#print(lista_coches)#Imprimo lo que se guardo en la variable lista

ficheroApertura.close()

for i in lista_coches:
    print(i.estado())#Manda a llamar por cada iteracion del for el metodo estado
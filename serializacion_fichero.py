"""Que es la serializacion """
#Consiste en guardar en un fichero externo una coleccion un diccionario, o un objeto, guardandolo en un fichero externo codificado
#en binaroio, con el objetivo de distribur un paquete que se ha construido en python por internet para que sea mas facil
"""Para poder realizar la serializacion se debe ocupar la biblioteca de python """
#pickle > dump ó load
#dump= permite hacer un volcado de datos al fichero binario externo
#load=Cargar los datos que se almacenaron con anterioridad en binario en un fichero externo


"""Eje: Guardar nombres en una lista"""
import pickle 
lista_nombres=["Pedro", "Ana","Maria","Jose"]

#luego crear un fichero externo 
fichero_binario=open("lista_nombres", "wb")#El parametro wb siginifca que se va a guardar en escritura binaria

#Luego hacer el volcado del fichero usando el metodo dump
pickle.dump(lista_nombres, fichero_binario)#este metodo requerie dos argumentos, la informacion que se quiere volcar, y el nombre del fichero
#al que se quier volcar

fichero_binario.close()

#del fichero_binario()Funcion para borrar el fichero que se crea en memoria que en este caso se llama fichero_binario   



"""Recueperar el archivo que se creo con escritura binaria"""

#variable fichero es un fichero en memoria
fichero=open("lista_nombres", "rb")#parametro rb para que pueda leer informacion binaria

lista=pickle.load(fichero)#metodo para cargar la informacion del fichero del archivo que se creo con escritura binaria
print(lista)
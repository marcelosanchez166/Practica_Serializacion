import pickle


class vehiculos():
    # Constructor, recibe dos parametros que tienen en comun todos los vehiculos
    def __init__(self, marca, modelo):
        self.marca = marca  # Carasteristicas de todo tipo de vehiculo
        self.modelo = modelo  # Carasteristicas de todo tipo de vehiculo
        self.enmarcha = "Detenido"  # Carasteristicas de todo tipo de vehiculo
        self.acelera = "No"  # Carasteristicas de todo tipo de vehiculo
        self.frena = "NO"  # Carasteristicas de todo tipo de vehiculo

    def arrancar(self, marcha):  # Metodos de todo tipo de vehiculo
        self.enmarcha = marcha
        if self.enmarcha == marcha:
            print()
        else:
            print("La moto esta detenida")

    def acelera(self):  # Metodos (o cosas que hacen) de los tipo de vehiculo
        self.acelera = "si"

    def frenar(self):  # Metodos de todo tipo de vehiculo
        self.frena = "si"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEl vehiculo esta:  ", self.enmarcha,
        "\nAcelerando: ", self.acelera, "\nfrenando: ", self.frena)


# Intanciar la clase o contruccion de metodos
carro1 = vehiculos("honda", "hasba")
carro2 = vehiculos("hilux", "frontier")
carro3 = vehiculos("mazda", "velozter")

# para no llamarlos uno a uno los meto dentro de una lista
coches = [carro1, carro2, carro3]

fichero = open("FicherdClaseVehiculos", "wb")  # wb= escritutra de binario

# hacer volcado de informacion del fichero
pickle.dump(coches, fichero)
fichero.close()


# """Rescatar la info que hay en el ficherdClaseVehiculos"""

# ficheroApertura=open("FicherdClaseVehiculos", "rb")#Se abre el fichero con rb= lectura de binario
# lista_coches=pickle.load(ficheroApertura)#guardo en la variable lista lo que se carga del metodo pickle.load que jala de la variable en memoria
# #ficheroApertura
# #print(lista_coches)#Imprimo lo que se guardo en la variable lista

# ficheroApertura.close()

# for i in lista_coches:
#           print(i.estado())#Manda a llamar por cada iteracion del for el metodo estado

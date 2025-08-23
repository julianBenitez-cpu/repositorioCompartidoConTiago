"""
Crea una clase vehículo que permita llevar el kilometraje
recorrido. Agrega atributos para definir color, marca, modelo y patente del vehículo
y métodos para: 1- conducir el auto (debe aceptar la cantidad de kilómetros y
sumarlo al kilometraje recorrido) y 2- muestre en pantalla los datos del vehículo y el
correspondiente kilometraje. Además, escribe una aplicación de consola que permita
al usuario conducir varios kilómetros y mostrar el kilometraje actual hasta que
decida detenerse. Al finalizar deberá mostrar los datos del vehículo y el kilometraje
recorrido.
"""

class vehiculo:
    def __init__(self, color, marca, modelo, patente, kilometraje = 0):
        self.__color = color
        self.__marca = marca
        self.__modelo = modelo
        self.__patente = patente
        self.__kilometraje = kilometraje 

    def get_color(self):
        return self.__color
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_patente(self):
        return self.__patente
    
    def get_kilometraje(self):
        return self.__kilometraje
    
    def conducir(self, kilometros):
        if kilometros > 0:
            self.__kilometraje += kilometros

    def mostrarDatos(self):
        return f'Marca: {self.__marca} Modelo: {self.__modelo}  Patente: {self.__patente}  Color:  {self.__color}  Kilometraje:  {self.__kilometraje}'
    

        
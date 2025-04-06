class Vehiculo:
 
    def __init__(self, velocidad: int):
        self.__velocidad = velocidad

    def get_velocidad(self):
        return self.__velocidad

    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad

    def acelerar(self):
        print(f"El vehiculo acelera a velocidad  { self.__velocidad } ")   
        
        
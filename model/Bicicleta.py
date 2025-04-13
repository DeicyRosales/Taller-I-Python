from model.Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, velocidad: int, tipo: str):
        super().__init__(velocidad)
        self.__tipo = tipo  
    

    def get_tipo(self) -> str:
        return self.__tipo
    
    def set_tipo(self, tipo: str):
        self.__tipo = tipo
    
    def pedalear(self):
        print("Pedaleando") 
         
    @classmethod
    def crear_bicicleta(cls):
        velocidad = input("Ingrese la velocidad de la bicicleta: ")
        tipo = input("Ingrese el tipo de la bicicleta: ")
        
        return cls((int(velocidad), tipo))
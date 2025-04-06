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
         
    
    
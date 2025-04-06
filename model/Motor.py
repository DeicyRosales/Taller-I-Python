
class Motor:
    def __init__(self, potencia: int, tipo: str):
        self.__potencia = potencia
        self.__tipo = tipo
        
    def get_potencia(self):     
        return self.__potencia


    def set_potencia(self, potencia):
        self.__potencia = potencia 
        
    def get_tipo(self):
        return self.__tipo
        
    def set_tipo(self, tipo):
        self.__tipo = tipo                      
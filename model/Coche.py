from model.Vehiculo import Vehiculo
from model.Motor import Motor  
from model.ExcesoVelocidadException import ExcesoVelocidadException

class Coche (Vehiculo):
    def __init__(self, marca: str, modelo: str, año: int, velocidad: int, motor: Motor):
        super().__init__(velocidad)
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__motor = motor
        
    def get_motor(self) -> Motor:   
        return self.__motor

    def set_motor(self, motor: Motor):
        self.__motor = motor 
        
    def get_marca(self) -> str:
        return self.__marca
        
    def set_marca(self, marca: str):
        self.__marca = marca 
        
    def get_año(self) -> int:   
        return self.__año
    
    def set_modelo(self, modelo: str):
        self.__modelo = modelo 
        
    def get_modelo(self) -> str:   
        return self.__modelo

    def set_año(self, año: int):
        self.__año = año 
              
    def describir(self):
        print(f"Este coche es un {self.__marca} {self.__modelo} del año {self.__año}")
        
    def describir_con_motor(self):
        print(f"Este coche es un {self.__marca} {self.__modelo} del año {self.__año} velocidad {self.get_velocidad()}")
        print(f"El motor es de tipo {self.__motor.get_tipo()} y una potencia {self.get_motor().get_tipo()}")
        
    def acelerar(self):
        print(f"El vehiculo marca {self.__marca} acelera hasta velocidad  { self.get_velocidad()} ") 
        
    def incrementar_velocidad(self, velocidad: int):
           if(velocidad > 200):
               raise ExcesoVelocidadException("La velocidad no puede ser mayor a 200 kl/h")
           else:
               vel = self.get_velocidad() + velocidad
               self.set_velocidad(vel)
          
    @classmethod
    def crear_coche(cls):
        marca = input("Ingrese la marca del vehiculo: ")
        modelo = input("Ingrese el modelo del motor: ")
        año = int(input("Ingrese el año del coche : "))
        velocidad = int(input("Ingrese la velocidad del coche: "))
        potencia_motor = int(input("Ingrese la potencia del motor: "))
        tipo_motor = input("Ingrese el tipo de motor: ")
      
        return  cls(marca, modelo , año, velocidad, Motor(potencia_motor, tipo_motor))
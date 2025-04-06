from model.Coche import Coche
from model.Motor import Motor
from model.Bicicleta import Bicicleta

def ejemplo_punto1_al_4():
    print("_______________")
    print("Ejemplo clases, encasulamiento, modificadores, constructores, herencia")
    print("_______________")

    # Creación de objetos
    coche1 = Coche("Toyota", "Corolla", 2020, 200, Motor(300, "electrico"))
    coche2 = Coche("Ford", "Mustang", 2022, 250, Motor(350, "gasolina"))
    coche3 = Coche("Tesla", "Model S", 2023, 80, Motor(280, "acpm"))

    # Mostrar descripción de los coches
    coche1.describir()
    coche2.describir()
    coche3.describir()

def ejemplo_polimorfismo():
    print("_______________")
    print("Ejemplo Polimorfismo")
    print("_______________")
    
    lista_medios_de_transporte = []
    
    coche1 = Coche("Toyota", "Corolla", 2020, 200, Motor(300, "electrico"))
    coche2 = Coche("Ford", "Mustang", 2022, 250, Motor(350, "gasolina"))
    bicicleta1 = Bicicleta("20 kl/h", "Ruta")
    bicicleta2 = Bicicleta("15 kl/h", "Ruta")
    
    lista_medios_de_transporte.append(coche1)
    lista_medios_de_transporte.append(coche2)
    lista_medios_de_transporte.append(bicicleta1)
    lista_medios_de_transporte.append(bicicleta2)
    
    for vehiculo in lista_medios_de_transporte: 
        vehiculo.acelerar()
        
    
    
    
    

ejemplo_punto1_al_4()
ejemplo_polimorfismo()
    
    
    





    



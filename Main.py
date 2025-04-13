from model.Coche import Coche
from model.Motor import Motor
from model.Bicicleta import Bicicleta
from model.Perro import Perro
from model.Gato import Gato
from model.Pajaro import Pajaro
from model.Avion import Avion
from model.ExcesoVelocidadException import ExcesoVelocidadException

lista_medios_de_transporte = []

def acelerar_vehiculos():
    print("_______________")
    print("Acelerar vehiculos")
    print("_______________")
    
    for vehiculo in lista_medios_de_transporte:
        vehiculo.acelerar() 

def describir_coches():
    print("_______________")
    print("Describir coches")
    print("_______________")
    
    for vehiculo in lista_medios_de_transporte:
        if(isinstance(vehiculo, Coche)):
            vehiculo.describir_con_motor()     
            
        
def ejemplo_abstractas():
    print("_______________")
    print("Ejemplo Abstractas")
    print("_______________")        
    
    perro1 = Perro()
    perro2 = Perro()
    gato1 = Gato()
    gato2 = Gato()
    
    lista_animales = [perro1, perro2, gato1, gato2]
    
    for animal in lista_animales:
        animal.hacer_sonido() 

def ejemplo_interface():
    print("_______________")
    print("Ejemplo Interfaces")
    print("_______________") 
    
    pajaro1 = Pajaro()
    pajaro1.volar()
    
    avion1 = Avion()
    avion1.volar()
            
def incrementar_velocidad():
    print("_______________")
    print("Incrementar velocidad a todos los coches")
    print("_______________")
    
    velocidad = input("Ingrese la velocidad que desea incrementar: ")
  
    for vehiculo in lista_medios_de_transporte:
        if(isinstance(vehiculo, Coche)):
            try:
                vehiculo.incrementar_velocidad(int(velocidad))
            except ExcesoVelocidadException as e:
                print(e)
         
    
while True:
    print("\nMain menu")
    print("1. Crear coche (Encapsulamiento, Poimofirmos, Herencia, composicion)")
    print("2. Crear Bicicleta (Encapsulamiento, Poimofirmos, Herencia)")
    print("3. Describir coches con motor")
    print("4. Acelerar todos los vehiculos (Sobreescribir metodo)")
    print("5. Ejemplo Animales (abstractas)")
    print("6. Ejemplo Volar (interfaces)")
    print("7. Incrementar velocidad (Excepciones)")
    print("8. Exit")
    main_option = input("Seleccione una opcion: ")

    if main_option == "1":
        coche = Coche.crear_coche()
        lista_medios_de_transporte.append(coche)
    elif main_option == "2":
        bicicleta = Bicicleta.crear_bicicleta()
        lista_medios_de_transporte.append(bicicleta)
    elif main_option == "3":
        describir_coches()
    elif main_option == "4":
        acelerar_vehiculos()
    elif main_option == "5":
        ejemplo_abstractas()
    elif main_option == "6":
        ejemplo_interface()
    elif main_option == "7":
        incrementar_velocidad()
    elif main_option == "8":
        break
    else:
        print("Opcion invalida")








    



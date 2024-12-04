
import random

numero_secreto=random.randint(1,11)
cantidad_de_intentos= 0
cantidad_max_de_intentos= 3 
adivinado= False

print("bienvenido al juego de adivinar el numero secreto")

while not  adivinado and cantidad_de_intentos < cantidad_max_de_intentos:
    numero= int(input("introduce un numero del 1 al 10: "))#TODO convertir a numero
    if numero == numero_secreto:
        print("FELICIDADES HAS ACERTADO!")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero que buscas es mayor al ingresado")
    else:
        print("el numero que buscas es menor al ingresado")
    cantidad_de_intentos += 1

if not cantidad_de_intentos < cantidad_max_de_intentos:
    print("GAME OVER!")

    

    


    


    
      
   


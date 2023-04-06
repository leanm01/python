#  EJERCICIO 1 
# Escribir un programa que le pida al 
# usuario que ingrese un número entero positivo, y luego 
# imprima "El número ingresado es positivo" si el número es mayor que cero, 
# o "El número ingresado es cero o negativo" si el número es menor o igual a cero.

'''
while True:
    try:
        numero = int(input("Ingrese un numero entero: "))
        break
    except ValueError:    
        print("ERROR... ingrese un numero entero")


if numero > 0:
    print("El numero ingresado es un entero positivo:",numero)

else:
    print("El numero ingresado es cero o negativo:",numero)

'''

#  EJERCICIO 2 
# Escribir un programa que le pida al usuario que ingrese su edad, 
# y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18, 
# o "Eres menor de edad" si la edad es menor a 18.

'''
while True:
    try:
        numero = int(input("Ingrese su edad: "))
        break
    except ValueError:    
        print("ERROR... reingrese su edad")


if numero >=18:
    print("Eres mayor de edad:",numero)

else:
    print("Eres mmenor de edad:",numero)

'''

#  EJERCICIO 3 
# Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima 
# "El número ingresado es par" si el número es divisible por 2, 
# o "El número ingresado es impar" si el número no es divisible por 2.

'''
while True:
    try:
        numero = input("Ingrese un numero entero: ")
        numero_entero = int(numero)
        break
    except ValueError:    
        print("ERROR... un numero entero: ")
        
if numero_entero % 2 == 0:
    print("el numero ingresado es par: ",numero_entero)

else:
    print("el numero ingresado es impar: ",numero_entero)        

'''

#  EJERCICIO 4 
# Escribir un programa que le pida al usuario que ingrese dos números enteros, 
# y luego imprima "El primer número es mayor" si el primer número es mayor que el segundo, "El segundo número es mayor" 
# si el segundo número es mayor que el primero, o "Los dos números son iguales" si los dos números son iguales.

'''
while True:
    try:
        numero_uno = int(input("Ingrese el primer numero entero: "))
        numero_dos = int(input("Ingrese el segundo numero entero: "))
        break
    except ValueError:    
        print("ERROR... un numero entero")

if numero_uno > numero_dos:
    print("el primer numero es mayor al dos")

elif numero_uno == numero_dos:
    print("los dos numeros son iguales")  

else:
    print("el segundo numero es mayor al primero")  

'''

#  EJERCICIO 5 
# Escribir un programa que le pida al usuario que ingrese su nombre, y luego imprima "Hola [nombre]" 
# si el nombre ingresado es "Juan", "María" o "Pedro", o "Hola desconocido" si el nombre ingresado no es uno de esos tres.
    
'''
nombres = []

nombre = input("ingrese su nombre: ")
    
if nombre.lower() in ("juan", "maria", "pedro") and nombre not in nombres: #verifica si los nombres son los permitidos
    nombres.append(nombre)
        
    print("hola,", nombre)
else:
    print("hola desconocido")

'''    
            
#  EJERCICIO 6 
# Escribir un programa que le pida al usuario que ingrese su nombre y su edad, y luego imprima "Puedes votar" 
# si la edad es mayor o igual a 18 y menor o igual a 65, o "No puedes votar" si la edad es menor a 18 o mayor a 65.

'''
nombre = input("ingrese su nombre: ")

edad = input("ingrese su edad: ")
edad_entero = int(edad)

if edad_entero >=18 and edad_entero <=65:
    print(nombre,", puedes votar")
else:
    print(nombre,", no puedes votar")

'''

#  EJERCICIO 7 
# Escribir un programa que le pida al usuario que ingrese un número entero positivo, 
# y luego imprima "El número es primo" si el número es primo, o "El número no es primo" si el número no es primo.

'''
numero = input("ingrese un numero: ")
numero_entero = int(numero)

if numero_entero >=1:
    for indice in range(2,numero_entero):
        if(numero_entero % indice) == 0:
            print("no es un numero primo")
            break
        else:
            print("es un numero primo")    

'''



#  EJERCICIO 8 
# Escribir un programa que le pida al usuario que ingrese un número entero positivo, 
# y luego imprima "El número es un cuadrado perfecto" 
# si el número es un cuadrado perfecto, o "El número no es un cuadrado perfecto" si el número no es un cuadrado perfecto.


#  EJERCICIO 9 
# Escribir un programa que le pida al usuario que ingrese una letra, 
# y luego imprima "Es una vocal" si la letra es una vocal (a, e, i, o, u), 
# o "Es una consonante" si la letra es una consonante.

'''
letra = input("ingrese una letra: ")

if letra == 'a' or letra == 'e' or  letra == 'i' or letra == 'o' or letra == 'u':
    print("la letra que ingreso es una vocal")
else:
    print("la letra que ingreso es una consonante")

'''



#  EJERCICIO 10 
# Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima 
# "El número es positivo y par" si el número es positivo y divisible por 2, 
# o "El número no cumple ninguna condición" si el número no cumple ninguna de las dos condiciones anteriores.

'''
numero = input("ingrese un numero: ")
numero_entero = int(numero)

if numero_entero > 0 and numero_entero % 2 == 0:
    print("el numero positivo es par")
else:
    print("el numero no cumple ninguna condicion")

'''


#  EJERCICIO 11 
# Escribir un programa que le pida al usuario que ingrese su edad, 
# y luego imprima "Eres un niño" si la edad es menor a 12, 
# "Eres un adolescente" si la edad está entre 12 y 17 inclusive, "Eres un adulto" si la edad está entre 18 y 64

'''
edad = input("ingrese su edad: ")
edad_entero = int(edad)

if edad_entero < 12:
    print("eres un niño")
elif edad_entero > 12 and edad_entero < 18:
    print("eres un adolescente")
elif edad_entero >=18 and edad_entero < 64:
    print("eres un adulto")

'''

#  EJERCICIO 12 
# Escribir un programa que le pida al usuario que ingrese dos números enteros, 
# y luego imprima "El primer número es positivo" si el primer número es mayor que cero, 
# "El segundo número es positivo" si el segundo número es mayor que cero, o "Ambos números son negativos" si los dos números son negativos.

'''

numero_uno = input("ingrese el primer numero: ")
nuermo_entero_uno= int(numero_uno)

numero_dos = input("ingrese el segundo numero: ")
nuermo_entero_dos= int(numero_dos)

if nuermo_entero_uno > 0:
    print("el primer numero es positivo")
if nuermo_entero_dos > 0:
    print("el segundo numero es positivo")  
else:
    print("ambos numeros son negativos")   

'''


#  EJERCICIO 13 
# Escribir un programa que le pida al usuario que ingrese un número entero, 
# y luego imprima "El número es divisible por 3 y por 5" si el número es divisible por 3 y por 5, 
# o "El número no es divisible por 3 y por 5" si el número no es divisible por 3 y por 5

'''
numero = input("ingrese un numero: ")
numero_entero = int(numero)

if numero_entero % 3 == 0 and numero_entero % 5 == 0:
    print("el numero es divisible por 3 y 5")
else:
    print("el numero no es divisible por 3 y 5")

'''

 
#  EJERCICIO 14 
# Escribir un programa que le pida al usuario que ingrese un número entero, 
# y luego imprima "El número es múltiplo de 4 y de 6" 
# si el número es múltiplo de 4 y de 6, o "El número no es múltiplo de 4 y de 6" si el número no es múltiplo de 4 y de 6.

'''
numero = input("ingrese un numero: ")
numero_entero = int(numero)

if numero_entero % 4 == 0 and numero_entero % 6 == 0:
    print("el numero es multiplo de 4 y 6")
else:
    print("el numero no es multiplo de 4 y 6")

'''

#  EJERCICIO 15 
# Escribir un programa que le pida al usuario que ingrese un número entero positivo, 
# y luego imprima "El número es primo" si el número es primo, o "El número no es primo" si el número no es primo.

#  EJERCICIO 16 
# Escribir un programa que le pida al usuario que ingrese su nombre y su edad, 
# y luego imprima "Eres adolescente" si la edad está entre 13 y 17 inclusive, 
# "Eres adulto" si la edad está entre 18 y 64 inclusive, o "Eres adulto mayor" si la edad es mayor o igual a 65.

'''
nombre = input("ingrese su nombre: ")

edad = input("ingrese su edad: ")
edad_entero = int(edad)

if edad_entero > 13 and edad_entero < 18:
    print(nombre,",Eres adolescente")
elif edad_entero >=18 and edad_entero < 65:
    print(nombre,",Eres adulto")
elif edad_entero >=65:
    print(nombre,",Eres adulto mayor")

'''


#  EJERCICIO 17 
# Escribir un programa que le pida al usuario que ingrese un número entero, 
# y luego imprima "El número es negativo" si el número es menor que cero, 
# "El número es cero" si el número es igual a cero, o "El número es positivo" si el número es mayor que cero.

'''
numero_uno = input("ingrese el primer numero: ")
nuermo_entero_uno= int(numero_uno)


if nuermo_entero_uno < 0:
    print("El número es negativo")
elif nuermo_entero_uno == 0:
    print("El número es cero")  
else:
    print("El número es positivo")   

'''

#  EJERCICIO 18 
# Escribir un programa que le pida al usuario que ingrese un número entero, 
# y luego imprima "El número es par y es múltiplo de 3" si el número es par y es múltiplo de 3, 
# o "El número no cumple ninguna de las dos condiciones" si el número no cumple ninguna de las dos condiciones.

'''
numero = input("ingrese un numero: ")
numero_entero = int(numero)

if numero_entero % 2 == 0 and numero_entero % 3 == 0:
    print("El número es par y es múltiplo de 3")
else:
    print("El número no cumple ninguna de las dos condiciones")

'''

#  EJERCICIO 19 
# Escribir un programa que le pida al usuario que ingrese su edad, 
# y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18, 
# "Eres adolescente" si la edad está entre 13 y 17 inclusive, o "Eres menor de edad" si la edad es menor que 13.

'''
edad = input("ingrese su edad: ")
edad_entero = int(edad)

if edad_entero >= 18:
    print("Eres mayor de edad")
elif edad_entero >=13 and edad_entero < 18:
    print("Eres adolescente")
elif edad_entero < 13:
    print("Eres menor de edad")

'''

#  EJERCICIO 20 
# Escribir un programa que le pida al usuario que ingrese dos números enteros, 
# y luego imprima "Los dos números son iguales" si los dos números son iguales, "El primer número es mayor" 
# si el primer número es mayor que el segundo, o "El segundo número es mayor" si el segundo número es mayor que el primero.

'''
numero = input("ingrese un numero: ")
numero_entero = int(numero)

numero_dos = input("ingrese un segundo numero: ")
numero_entero_dos = int(numero_dos)


if numero_entero == numero_entero_dos:
    print("Los dos números son iguales")
elif numero_entero > numero_entero_dos:
    print("El primer número es mayor")
else:
    print("El segundo número es mayor")
    

'''

       
       
        
#  EJERCICIO 1 Dado un número entero n, imprimir todos los números desde n hasta 1 en orden descendente.

'''
numero = input("ingrese un numero entero: ")
numero_entero = int(numero)

while numero_entero > 0:
    print(numero_entero)
    numero_entero -= 1

'''
#  EJERCICIO 2 Dado un número entero n, imprimir todos los números desde 1 hasta n en orden ascendente.

'''
numero = 1
numero_limite = input("ingrese un numero entero: ")
numero_limite_entero = int(numero_limite)

while numero <=numero_limite_entero:
    print(numero)
    numero += 1

'''

#  EJERCICIO 3 Dada una cadena de texto, imprimir cada uno de los caracteres en la cadena.

'''
indice = 0
cadena = input("ingrese la palabra que desee: ")


while indice < len(cadena):
    print(cadena[indice])
    indice += 1

'''
#  EJERCICIO 4 Dada una lista de números, imprimir la suma de todos los elementos de la lista.

''' 
lista_numeros = [5,5,10,10,15]
indice = 0
suma= 0

while indice < len(lista_numeros): # mientras el índice sea menor que la longitud de la lista
    suma += lista_numeros[indice]
    indice += 1
print("la suma de los numeros es: ", suma)

'''

#  EJERCICIO 5 Dado un número entero n, imprimir si el número es primo o no.

'''
numero = input("Ingrese un numero: ")
numero_entero= int(numero)
es_primo = True
divisor = 2

while divisor < numero_entero: 
   if numero_entero % divisor == 0:
       es_primo = False
       break
   divisor +=1 # pasamos al siguiente posible divisor

if es_primo:
    print("El numero es primo: ",numero_entero) #son aquellos que solo son divisibles entre ellos mismos y el 1
else:
    print("no es un numero primo: ",numero_entero)
    

'''

#  EJERCICIO 6 Dado un número entero n, imprimir la suma de todos los números pares menores o iguales a n.

'''
numero = input("ingrese un numero: ")
numero_entero = int(numero)
suma = 0
contador = 0

while contador <= numero_entero:
    if contador % 2 == 0:
        suma += 1
    contador += 1
    
print("La suma de los numeros pares menores o iguales al numero:", numero_entero, "es:", suma)

'''   

#  EJERCICIO 7 Dada una lista de números, imprimir todos los números que son mayores que el promedio de la lista.
       
'''
lista_numeros = [5,6,9,10,7,2]     

promedio = sum(lista_numeros) / len(lista_numeros) # suma los numeros de la lista y lo divide por la cantidad de numeros de la lista

indice = 0 # indice = posicion de un elemento dentro de una lista

while indice < len(lista_numeros): # mientras el indice sea menor a la longitud de la lista
    if lista_numeros[indice] > promedio: #comprueba si el elemento actual es mayor al promedio
        print(lista_numeros[indice])
    indice += 1

'''       
    
#  EJERCICIO 8  Dada una cadena de texto, imprimir la cantidad de vocales en la cadena.

'''
texto = input("ingrese una palabra: ")
vocales ="aeiou"

cantidad_de_vocales = 0
indice = 0

while indice < len(texto):
    if texto[indice] in vocales:
        cantidad_de_vocales +=1
    indice += 1

print("la cantidad de vocales es: ",cantidad_de_vocales)

'''

#  EJERCICIO 9 Dado un número entero n, imprimir todos los números impares menores o iguales a n.

'''
numero = input("ingrese un numero: ")
numero_entero = int(numero)
indice = 0

while indice <= numero_entero:
    if indice % 3 == 0:
        print(indice)
    indice += 1
    
print("La suma de los numeros impares o iguales al numero:", numero_entero)

'''

# EJERCICIO 10 Dada una lista de números, imprimir la cantidad de números pares en la lista.

'''
lista_numeros = [2,3,4,5,6,7,8,9]
cantidad_pares = 0
indice = 0

while indice < len(lista_numeros):
    if lista_numeros[indice] % 2 == 0:
        cantidad_pares += 1
    indice += 1
    
print("La cantidad de pares en la lista es: ",cantidad_pares )

'''
# EJERCICIO 11 Dada una lista de palabras, imprimir todas las palabras que tengan una longitud mayor a 5 caracteres.

'''
lista_palabras = ["necesito", "algo", "ayudame", "mi", "loco"]

indice = 0

while indice < len(lista_palabras):
    if len(lista_palabras[indice]) > 5:
        print(lista_palabras[indice])
    indice +=1

'''



# EJERCICIO 12 Dado un número entero n, imprimir la suma de todos los números impares menores o iguales a n.

'''
numero = input("ingrese un numero: ")
numero_entero = int(numero)
suma = 0
contador = 0

while contador <= numero_entero:
    if contador % 3 == 0:
        suma += 1
    contador += 1
    
print("La suma de los numeros impares menores o iguales al numero:", numero_entero, "es:", suma)

'''

# EJERCICIO 13 Dada una lista de números, imprimir la cantidad de números negativos en la lista.

'''
lista_numeros = [-1,2,3,20,-10,-4,5]
contador_negativos = 0
indice = 0

while indice < len(lista_numeros):
    if lista_numeros[indice] < 0:
        contador_negativos += 1
    indice += 1
    
print("la cantidad de negativos es: ", contador_negativos)

'''


# EJERCICIO 14 Dada una cadena de texto, imprimir la cantidad de veces que aparece una letra específica en la cadena.

'''
cadena = "hola como estan"
letra = "a"
contador = 0
indice = 0

while indice < len(cadena):
    if cadena[indice] == letra:
        contador += 1
    indice +=1

print("la letra:", letra, "aparece: ", contador, "vez/veces en la cadena", cadena)

'''

# EJERCICIO 15 Dado un número entero n, imprimir todos los números primos menores o iguales a n.

# EJERCICIO 16 Dada una lista de números, imprimir todos los números que son múltiplos de 3.

'''
lista_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,26,23]

indice = 0

while indice < len(lista_numeros):
    if lista_numeros[indice] % 3 == 0:
        print(lista_numeros[indice])
    indice += 1

'''
    

# EJERCICIO 17 Dada una cadena de texto, imprimir la cadena al revés.

'''
cadena = "hola desconocido"
indice = len(cadena) - 1 
cadena_invertida = ""

while indice >= 0:
    cadena_invertida += cadena[indice]
    indice -= 1
print(cadena_invertida)

'''

# EJERCICIO 18 Dado un número entero n, imprimir la suma de todos los números que son múltiplos de 5 menores o iguales a n.

'''
numero = 100
suma = 0
indice = 1

while indice <= numero:
    if indice % 5 == 0:
        suma += 1
    indice += 1

print("La suma de los multiplos de 5 menores o iguales al numero:", numero, "es:", suma)

'''

# EJERCICIO 19 Dada una lista de números, imprimir todos los números que son mayores que el número anterior en la lista.

'''
lista_numeros = [3,5,7,8,9,6,4,20,14]
numero_anterior = lista_numeros[0]
indice = 1

while indice < len(lista_numeros):
    if lista_numeros[indice] > numero_anterior:
        print(lista_numeros[indice])
    numero_anterior = lista_numeros[indice]
    indice += 1

'''


# EJERCICIO 20 
# Dado un número entero n, imprimir todos los números perfectos menores o iguales a n. 
# Los números perfectos son aquellos números enteros positivos que son iguales a la suma de sus divisores 
# propios (excluyendo al propio número). En otras palabras, si sumamos todos los divisores propios de un número 
# (excluyendo el número en sí mismo) y el resultado es igual al número, entonces ese número se considera un número perfecto.
# Por ejemplo, el primer número perfecto es 6, ya que sus divisores propios son 1, 2 y 3, y 1 + 2 + 3 = 6. O
# tros ejemplos de números perfectos son 28, 496 y 8128. Actualmente se conocen más de 50 números perfectos, 
# y se cree que existen infinitos números perfectos, aunque no se ha podido demostrar matemáticamente esta afirmación.



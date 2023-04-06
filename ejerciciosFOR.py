#  EJERCICIO 1 Dada una lista de números, imprimir el número más grande de la lista.
'''
numeros = [2, 63, 58, 35, 12, 5]

numero_maximo = 0

for numero in numeros:
    if numero > numero_maximo:
        numero_maximo = numero
        

print("el numero mas grande de la lista es: ",numero_maximo)

'''
#  EJERCICIO 2 Dada una lista de palabras, imprimir la palabra más larga de la lista.

'''
lista_palabras = ["hola", "diario", "palabra", "tridente", "blasfemia"] 
palabra_mas_larga = ""

for palabra in lista_palabras:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

print("la palabra mas larga es: ", palabra_mas_larga)

'''

#  EJERCICIO 3 Dado un número entero n, imprimir la secuencia de números pares menores o iguales a n.

'''
limite_de_numeros = 20

for indice in range(2, limite_de_numeros+1,2): # empieza desde el 2, hasta el numero 19 + 1, y lo hace de dos en dos que es PAR
    print(indice)

'''
 
#  EJERCICIO 4 Dado un número entero n, imprimir la suma de los números impares menores o iguales a n.

'''
numero_limite = 30
suma_impares = 0

for indice in range(1, numero_limite+1, 2):
    suma_impares +=1

print("la suma de los numeros impares menores o iguales al numero: ",numero_limite, "es: ",suma_impares)

'''



#  EJERCICIO 5 Dada una lista de números, imprimir el número más pequeño de la lista.

'''
lista_numeros = [6,7,50,3,4,10,15,13,23]
numero_mas_pequeño = lista_numeros[0]

for indice in lista_numeros:
    if indice < numero_mas_pequeño:
        numero_mas_pequeño = indice #si encuentra un numero mas pequeño lo actualiza 
    
print("el numero mas pequeño de la lista es: ", numero_mas_pequeño)

'''


#  EJERCICIO 6 Dada una lista de palabras, imprimir la cantidad total de vocales en la lista.

'''
lista_palabras = ["palabra","maldicion","destino","forma","final","guardian"]
vocales = "aeiou"
total_vocales = 0

for palabra in lista_palabras:
    for letra in palabra:
        if letra in vocales:
            total_vocales += 1

print("la cantidad total de vocales en la lista es: ", total_vocales)

'''


#  EJERCICIO 7 Dado un número entero n, imprimir la secuencia de números impares menores o iguales a n.

'''
numero = input("ingrese un numero: ")
numero_entero = int(numero)

for indice in range(1, numero_entero+1, 2):
    print(indice)

'''


#  EJERCICIO 8 Dado un número entero n, imprimir la suma de los números pares menores o iguales a n.

'''
numero_limite = 50
suma_pares = 0

for indice in range(2, numero_limite+1, 2):
    suma_pares +=1

print("la suma de los numeros impares menores o iguales al numero: ",numero_limite, "es: ",suma_pares)
 

'''
#  EJERCICIO 9 Dada una lista de números, imprimir la cantidad de números negativos en la lista.

'''
lista_numeros = [-1,-2,-8,-6,-7,4,2,3,7,5,4]
contador = 0 

for numero in lista_numeros:
    if numero < 0:
        contador +=1

print("la cantidad de numeros negativos en la lista es: ", contador)

'''

#  EJERCICIO 10 Dada una lista de palabras, imprimir las palabras que comienzan y terminan con la misma letra.

'''
lista_palabras = ["palabra", "serpientes", "cosas", "oso", "soportes"]

for palabra in lista_palabras:
    if palabra[0] == palabra[-1]:
        print(palabra)

'''
 
#  EJERCICIO 11 Dado un número entero n, imprimir la secuencia de números primos menores o iguales a n.

#  EJERCICIO 12 Dada una lista de números, imprimir la cantidad de números pares en la lista.

'''
lista_numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
contador = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        contador += 1

print("la cantidad de numeros pares en la lista es: ", contador)

'''

#  EJERCICIO 13 Dada una lista de palabras, imprimir las palabras que tienen una longitud impar.

'''
lista_palabras = ["casa", "mueble", "comedor", "terraza", "cocina", "cuarto"]

for palabra in lista_palabras:
    if len(palabra) % 2 == 0:
        print(palabra)

'''

#  EJERCICIO 14 Dado un número entero n, imprimir la secuencia de números perfectos menores o iguales a n.

#  EJERCICIO 15 Dada una lista de números, imprimir la cantidad de números impares en la lista.

'''
lista_numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
contador = 0

for numero in lista_numeros:
    if numero % 3 == 0:
        contador += 1

print("la cantidad de numeros pares en la lista es: ", contador)

'''

#  EJERCICIO 16 Dada una lista de palabras, imprimir las palabras que tienen una letra específica.

'''
lista_palabras = ["hola","señores","increible","viajero","luz"]
letra = "o"
contador = 0

for palabra in lista_palabras:
    if letra in palabra:
        print(palabra)

'''


#  EJERCICIO 17 Dado un número entero n, imprimir la secuencia de números de Harshad menores o iguales a n.

#  EJERCICIO 18 Dada una lista de números, imprimir la suma de los números en la lista que son mayores que el promedio de la lista.

'''
lista_numeros = [2,3,4,5,6,7,8,9,12,15]
promedio = sum(lista_numeros) / len(lista_numeros)
suma = 0

for numero in lista_numeros:
    if numero > promedio:
        suma += numero

print("la suma de los numeros mayores que el promedio es: ", suma)

'''

#  EJERCICIO 19 Dada una lista de palabras, imprimir las palabras que tienen una letra mayúscula.

'''
lista_palabras = ["Hola","Leandro","como","estas"]

for palabra in lista_palabras:
    if palabra.isupper(): # si hay una letra mayuscula devuelve TRUE
        print(palabra)

'''

#  EJERCICIO 20 Dado un número entero n, imprimir la secuencia de números triangulares menores o iguales a n.

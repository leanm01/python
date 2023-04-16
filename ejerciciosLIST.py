#  EJERCICIO 1 Crea una lista con los números del 1 al 10 e imprime solo los números impares.

'''
lista_numeros = list(range(1, 11))
numeros_imapres = []

for numero in lista_numeros:
    if numero % 3 == 0:
        numeros_imapres.append(numero) # el append lo agrega a numero si es impar, en este caso
        
print("Los numeros impares son: ", numeros_imapres)

'''


#  EJERCICIO 2 
# Crea una lista con 5 números enteros. Luego solicita un nuevo número y 
# reemplaza el tercer elemento de la lista por el número ingresado. Finalmente imprime todos los números

'''
lista_numeros = [1,2,3,4,5]

nuevo_numero = input("ingrese el nuevo numero: ")
nuevo_numero_entero = int(nuevo_numero)

lista_numeros[2] = nuevo_numero_entero

print("la lista es: ", lista_numeros)

'''

#  EJERCICIO 3 
# Crea una lista vacía y 
# pide al usuario que ingrese números enteros hasta que 
# ingrese un número negativo. Luego, muestra la suma de todos los números ingresados.

'''
lista_numeros = []

while True:
    numero = input("ingrese un numero (ingrese un numero negativo para salir): ")
    numero_entero = int(numero)
    if numero_entero < 0:
        break
    lista_numeros.append(numero_entero)
    
suma = sum(lista_numeros)

print("la suma de los numero ingresados es: ", suma)    

'''

#  EJERCICIO 4 
# Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, 
# muestra la primera letra de la palabra. Repite este proceso hasta que el usuario ingrese una palabra que comience con la letra "z".

'''
palabras = []

while True:
    palabra = input("Ingresa una palabra: ")
    palabras.append(palabra)
    if palabra.startswith("z"): # verifica si empieza con z
        break

for palabra in palabras:
    print(palabra[0]) #posicion 0 o sea primer letra 

'''

#  EJERCICIO 5 Crea una lista con los nombres de 5 ciudades y luego imprime el último elemento de la lista.

'''
nombre_ciudades = ["buenos aires","rosario","los angeles","la plata","tokio"]

print(nombre_ciudades[-1])

'''

#  EJERCICIO 6 Crea una lista con 3 números enteros y luego agrega un nuevo número al final de la lista.

'''
numeros_enteros = list([1,2,3])
numero_nuevo = 4

numeros_enteros.append(numero_nuevo)

print(numeros_enteros)

'''


#  EJERCICIO 7 Crea una lista con los nombres de tus 3 deportes favoritos y luego agrega otro deporte al final de la lista.

'''
lista_deportes = list(["futbol","basquet","natacion"])
deporte_nuevo = "paddle"

lista_deportes.append(deporte_nuevo)

print(lista_deportes)

'''

#  EJERCICIO 8 Crea una lista con los nombres de tus 5 libros favoritos y luego imprime solo los primeros 3 libros de la lista.

'''
lista_libros = list(["LORD OF THE RINGS","THE HOBBIT","LOTR RETURN OF THE KING","JURASSIC PARK","LOTR TWO TOWERS"])

print(lista_libros[:3])

'''

#  EJERCICIO 9 
# Crea una lista de números enteros y pide al usuario que ingrese otro número entero. 
# Luego, busca el número ingresado en la lista y 
# muestra la posición en la que se encuentra. Si el número no se encuentra en la lista, muestra un mensaje indicando que no se encontró

'''
lista_numeros = [5,4,3,7,9,10]

numero_ingresado = input("ingrese un numero: ")
numero_ingresado_entero = int(numero_ingresado)

if numero_ingresado_entero in lista_numeros:
    print("el numero", numero_ingresado_entero, "se encuentra en la posicion:",lista_numeros.index(numero_ingresado_entero),"de la lista")
else:
    print("el numero", numero_ingresado_entero, "no se encuentra en la lista")

'''

#  EJERCICIO 10 Crea una lista de palabras y muestra las palabras que tienen más de 5 letras.

'''
lista_palabras = ["pelota","futbol","araña","hola","pera","uva","melon","ave"]

palabras_largas = []

for palabra in lista_palabras:
    if len(palabra) > 5:
        palabras_largas.append(palabra)

print("las palabras con mas de 5 letras son: ",palabras_largas)

'''
        

#  EJERCICIO 11 
# Crea una lista de palabras y pide al usuario que ingrese una palabra. Luego, 
# muestra todas las palabras de la lista que tienen la misma longitud que la palabra ingresada.

'''
lista_palabras = ["pelota","futbol","araña","hola","pera","uva","melon","triton"]

palabra_ingresada = input("ingrese una palabra: ")

longitud_palabra = len(palabra_ingresada)

palabra_misma_longitud = [palabra for palabra in lista_palabras if len(palabra) == longitud_palabra]

print("Las palabras de la lista con la misma longitud que '{}' son: {}".format(palabra_ingresada, palabra_misma_longitud))

'''


#  EJERCICIO 12 
# Crea una lista con los nombres de tus 3 películas favoritas y 
# luego imprime los elementos en orden inverso (sin utilizar el método reverse())

'''
lista_libros = ["LORD OF THE RINGS","THE HOBBIT","LOTR RETURN OF THE KING"]

peliculas_inversas = [lista_libros[i] for i in range(len(lista_libros)-1, -1, -1)]

print(peliculas_inversas)

'''

#  EJERCICIO 13 Crea una lista de números y encuentra el promedio de todos los números en la lista

'''
lista_numeros = [12,5,6,4,78,10,65]

promedio = sum(lista_numeros) / len(lista_numeros)

print("lista de nuemeros: ",lista_numeros)
print("promedio de numeros: ",promedio)

'''

#  EJERCICIO 14 
# Crea dos listas de 10 números enteros cada una y 
# realiza una multiplicación de los elementos con el mismo índice en ambas listas.

'''
lista_numeros = [12,5,6,4,78,10,65]

promedio = sum(lista_numeros) * len(lista_numeros)

print("lista de nuemeros: ",lista_numeros)
print("la multiplicacion de numeros: ",promedio)

'''

#  EJERCICIO 15 Crea una lista de números enteros y luego encuentra la suma de los números en índices impares.

'''
lista_numeros = [1,2,3,4,5,6,7,8,9]

impares = lista_numeros[1::2] #[start:stop:step]

suma_impares = sum(impares)

print("la suma de los numeros impares es: ",suma_impares)

'''

#  EJERCICIO 16 
# Crea dos listas con la misma cantidad de elementos y 
# luego crea una tercera lista que contenga los elementos de ambas listas intercalados. 
# Por ejemplo, si las dos listas son [1, 2, 3] y ["a", "b", "c"], la tercera lista debería ser [1, "a", 2, "b", 3, "c"].

'''
lista_uno = [3,2,1]
lista_dos = ["c","b","a"]

lista_tres = []

for elemnto1, elemento2 in zip(lista_uno,lista_dos): # la función zip para recorrer ambas listas al mismo tiempo y obtener los elementos correspondientes
    lista_tres.append(elemnto1) 
    lista_tres.append(elemento2) 
    
print(lista_tres)

'''

#  EJERCICIO 17 Crea dos listas de números y encuentra los elementos que se encuentran en ambas listas.

'''
lista_uno = [1,2,3,4,5]
lista_dos = [6,7,8,9,10]

elementos_comunes = list(set(lista_uno) & set(lista_dos)) # la función set() para convertir cada lista en un conjunto

print("los elementos comunes son: ",elementos_comunes)

'''


#  EJERCICIO 18 
# Solicitar al usuario números enteros hasta que ingrese el 0. 
# Almacenar los números en una lista y luego imprimir el mayor (sin utilizar la función max())

'''
numeros = []

while True:
    numero = input("ingrese un numero (0 para salir): ")
    numero_entero = int(numero)
    if numero_entero == 0:
        break
    numeros.append(numero_entero)

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero
        
print("el numero mayor es: ", mayor)

'''

#  EJERCICIO 19 
# Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, 
# agrega la palabra a la lista si no se encuentra ya en la lista. 
# Repite este proceso hasta que la lista tenga al menos 5 palabras.

#  EJERCICIO 20 A partir de la lista: [1,80,5,0,15,-5,1,79] determinar, el mayor, el menor, el promedio y la suma total de todos los elementos

'''
lista_nuemeros = [1,80,5,0,15,-5,1,79]

mayor = max(lista_nuemeros)
menor = min(lista_nuemeros)

promedio = sum(lista_nuemeros) / len(lista_nuemeros)

suma_total = sum (lista_nuemeros)

print("el numero mayor es: ",mayor)
print("el numero menor es: ",menor)
print("el promedio es: ",promedio)
print("la suma total es: ",suma_total)

'''

#  EJERCICIO 21 
# Crear un programa que solicite al usuario ingresar precio unitario y 
# cantidad de 5 productos. Almacenar cada valor en dos listas distintas. Luego imprimir el precio total de cada artículo.

#  EJERCICIO 22 
# Crear un programa que solicite al usuario ingresar: 
# nombre del producto, cantidad y precio unitario. Guardar los datos en 3 listas distintas. 
# Solicitar productos hasta que el nombre del producto sea ‘xxx’. 
# Luego imprimir la lista de artículos con el siguiente formato 
# :nombre_articulo	cantidad $precio_unitario $total Ejemplo: alfajor capitan del espacio 6 $ 150 $ 900


#  EJERCICIO 1 
# Crea un diccionario que represente los días de la semana, 
# donde las claves son los nombres de los días y los valores son los números correspondientes 
# (por ejemplo, {"lunes": 1, "martes": 2, ...}). Imprime el valor correspondiente al día "miércoles".

'''
lista_dias = {'Lunes': 1, 'martes': 2,'miercoles': 3,'jueves': 4,'viernes': 5,'sabado': 6,'domingo': 7}

print(lista_dias['miercoles'])

'''

#  EJERCICIO 2 
# Crea un diccionario que represente los meses del año, donde las claves son los nombres de los meses y los valores son sus 
# números correspondientes (por ejemplo, {"enero": 1, "febrero": 2, ...}). Imprime el número correspondiente al mes "julio".

'''
lista_meses = {'enero': 1, 'febrero': 2,'marzo': 3,'abril': 4,'mayo': 5,'junio': 6,'julio': 7,'agosto': 8,'septiembre': 9,'octubre': 10,'noviembre': 11,'diciembre': 12}

print(lista_meses['julio'])

'''

#  EJERCICIO 3 
# Crea un diccionario que contenga la información de una película, 
# como título, director y año de estreno. Luego, imprime el título de la película.

'''
datos_peliculas = {'LORD OF THE RINGS': 1, 'Peter Jackson': 2,'2001': 3}

for clave in datos_peliculas.keys():
    print("informacion de la pelicula: {0}".format(clave,datos_peliculas[clave]))

'''

#  EJERCICIO 4 
# Crea un diccionario que contenga la información de una dirección: nombre de la calle, altura, 
# localidad, código postal, partido y provincia. Luego, imprime el nombre de la calle, seguido de su altura.

'''
datos_direccion = {'calle': "illia", 'altura': "1234",'localidad': "burzaco",'codigo postal': "1875", 'partido': "almirante brown",'provincia':"buenos aires"}

print(datos_direccion["calle"] + " " + str(datos_direccion["altura"]))

'''


#  EJERCICIO 5 
# Crea un diccionario que represente los continentes, donde las claves son los nombres de los continentes 
# y los valores son los números correspondientes (por ejemplo, {"América": 1, "Europa": 2, ...}). 
# Imprime el valor correspondiente al continente "África".

'''
lista_paises = {'america': 1, 'europa': 2, 'asia': 3, 'africa': 4, 'oceania': 5, 'antartida': 6}

print(lista_paises['africa'])

'''


#  EJERCICIO 6 
# Crea un diccionario que represente las estaciones del año, donde las claves son los nombres de las estaciones 
# y los valores son los números correspondientes 
# (por ejemplo, {"primavera": 1, "verano": 2, ...}). Imprime el valor correspondiente a la estación "invierno".

'''
lista_paises = {'primavera': 1, 'verano': 2, 'invierno': 3, 'otoño': 4}

print(lista_paises['invierno'])

'''

#  EJERCICIO 7 
# Crea un diccionario que contenga la información de una canción: título, artista y duración. Luego, imprime la duración de la canción.

'''
lista_paises = {'título': "cliffs of dover", 'artista': "eric", 'duración': "4:10"}

print(lista_paises['duración'])

'''

#  EJERCICIO 8 
# Crea un diccionario que represente las edades de varias personas, 
# donde las claves son los nombres de las personas y los valores son sus edades. Imprime la edad de la persona más joven.

'''
lista_paises = {'pepe': 30, 'lisandro': 20 , 'juan': 10 , 'julia': 13 , 'agustina': 54}

edad_mas_joven = min(lista_paises.values())

print("la edad del mas joven: ", edad_mas_joven)

'''

#  EJERCICIO 9 
# Crea un diccionario que contenga las capitales de los países de América del Sur. 
# Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.

'''
diccionario_paises = {'argentina': "buenos aires", 'bolivia': "la paz", 'brasil': "rio", 'colombia': "bogota", 'chile': "santiago"}

ingreso_pais = input("ingrese un pais de america del sur: ")
capital = diccionario_paises.get(ingreso_pais)

if capital:
    print(f"La capital de {ingreso_pais} es {capital}.")
else:
    print("El país ingresado no se encuentra en la lista.")

'''

#  EJERCICIO 10 
# Crea un diccionario que represente las notas de un examen de varios estudiantes, donde las claves son los nombres de los estudiantes 
# y los valores son sus notas. Imprime el promedio de las notas.

'''
dict_alumnos = {'pedro': [5,9,3], 'lucia': [7,4,6], 'ezequiel': [8,8,9], 'roberto': [3,5,2], 'tenma': [4,7,7]}

promedios = {}

for alumno, notas in dict_alumnos.items():
    promedio = sum(notas) / len(notas)
    promedios[alumno] = promedio
    
print("promedios: ", promedios)

'''
#  EJERCICIO 11 
# Crea un diccionario que represente una lista de tareas por hacer. 
# Cada clave del diccionario debe ser el nombre de una tarea y cada valor debe ser su estado (los estados son:  
# pendiente, en proceso, completada). Imprimir todas las tareas seguido de su estado

'''
tareas = {"Limpiar la cocina": "completada","Hacer la compra": "pendiente","Pagar las facturas": "en proceso","Hacer ejercicio": "pendiente"}

for tarea, estado in tareas.items():
    print(f"{tarea}: {estado}") # as f-strings permiten incrustar directamente el valor de una variable dentro de una cadena utilizando llaves

'''

#  EJERCICIO 12 
# Crea un diccionario que represente una lista de las compras. 
# Cada clave del diccionario debe ser el nombre de un producto y cada valor debe ser su cantidad. 
# Pedir al usuario que ingrese el nombre del producto e imprimir la cantidad

'''
lista_compras = {}

while True:
    producto = input("Ingrese el nombre del producto (o 'fin' para salir): ")
    
    if producto == 'fin':
        break
    
    cantidad = int(input("Ingrese la cantidad: "))
    
    lista_compras[producto] = cantidad
    
print("La lista de compras es:")
for producto, cantidad in lista_compras.items():
    print(producto, cantidad)

'''

#  EJERCICIO 13 
# Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa. 
# Luego, pedirle al usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres

'''
juegos_de_mesa = {"Monopoly": "medio","Risk": "difícil", "Catan": "medio","Scrabble": "facil","Ajedrez": "difícil","Dominó": "facil"}

nivel = input("Ingrese un nivel de dificultad (facil, medio, difícil): ")

juegos_coincidentes = [juego for juego, nivel_juego in juegos_de_mesa.items() if nivel_juego == nivel]

print("Los juegos de nivel", nivel, "son:")
for juego in juegos_coincidentes:
    print(juego)

'''

#  EJERCICIO 14 
# Crea un diccionario que contenga el nombre como clave y el puntaje como valor de varios jugadores en un juego. 
# Luego, pedirle al usuario el nombre del jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.

'''
jugadores = {'pepe': 10, 'tilin': 20, 'robert': 15}

nombre = input("ingrese el nombre del jugador: ")
puntaje = input("ingrese el puntaje del jugador: ")
puntaje_entero = int(puntaje)

jugadores[nombre] = puntaje_entero

print(jugadores)

'''

#  EJERCICIO 15 
# Crea un diccionario que contenga el nombre y el sueldo de varios empleados. 
# Luego, permite al usuario aumentar el sueldo de un empleado y actualizar el valor correspondiente en el diccionario.

'''
empleados = {'pepe': 50000, 'tilin': 20000, 'robert': 15000}

nombre = input("ingrese el nombre del jugador: ")
salario = input("ingrese el puntaje del jugador: ")
salario_entero = int(salario)

empleados[nombre] = salario_entero

print(empleados)

'''

#  EJERCICIO 16 
# Crea un diccionario que represente una lista de tareas pendientes, 
# donde las claves son las tareas y los valores son "True" si están completadas y "False" si no lo están. 
# Solicita al usuario el nombre de una tarea y modifica el valor para marcarla como completada. Imprimir el listado de tareas pendientes

#  EJERCICIO 17 
# Crea un diccionario que represente las películas de un cine, donde las claves son los nombres de las películas y 
# los valores son los horarios correspondientes. 
# Modifica el horario de la película "Avengers: Endgame" a las 19:30.

#  EJERCICIO 18 
# Crea un diccionario que represente los juegos de una consola, donde las claves son los nombres de los juegos y 
# los valores son las puntuaciones correspondientes. 
# Solicita al usuario el nombre de un juego y luego su puntuación, si el juego no existe agregarlo y si existe actualizar su puntuación 

#  EJERCICIO 19 
# Crea un diccionario que represente las temperaturas de una ciudad durante una semana, 
# donde las claves son los días de la semana y los valores son las temperaturas correspondientes. 
# Calcula la temperatura promedio de la semana.

#  EJERCICIO 20 
# Crea un diccionario que represente los asientos de un avión, donde las claves son los números de asientos y 
# los valores son "True" si están ocupados y "False" si no lo están. Solicita al usuario un número de asiento y 
# modifica su valor para marcarlo como ocupado. 
# Luego imprimí la lista de asientos libres

#  EJERCICIO 21 
# Crea un diccionario que represente los gastos de una persona en diferentes categorías, 
# donde las claves son los nombres de las categorías y 
# los valores son los gastos correspondientes. Calcula el total de gastos de la persona.

#  EJERCICIO 22 
# Crea un diccionario que represente los gastos de una persona en diferentes categorías, 
# donde las claves son los nombres de las categorías y los valores son los gastos correspondientes. 
# Calcula el total de gastos de la persona en el mes.

#  EJERCICIO 23 
# Crea un diccionario que represente los contactos de un teléfono, 
# donde las claves son los nombres de las personas y los valores son los números de teléfono correspondientes. Solicitar al usuario el nombre de un contacto: agregarlo al diccionario en caso de que no exista. 
# En caso de que exista modificar el número de teléfono del contacto.


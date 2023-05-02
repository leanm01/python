#  EJERCICIO 1 
# Crear una función que convierta grados Celsius a grados Fahrenheit. 
# Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.

'''
def de_celcius_a_farenheit(valor_celcius):
    """
    calculo para pasar de celcius a farenheit
    valor de celcius como parametro
    retorna el valor en farenheit
    
    """
    
    valor_farenheit = (valor_celcius * 9/5) +32
    return valor_farenheit

'''





#  EJERCICIO 2 Crear una función que calcule el área de un círculo. Recibe un parámetro (radio) y devuelve el área del círculo.

'''
def area_de_circulo(radio):
    """  
    calcula el area de un circulo a partir de un radio
    el radio como parametro
    retorna el area de un circulo

    """
    
    area = 3.141592653589793238 * radio ** 2
    return area

'''

  

#  EJERCICIO 3 
# Crear una función que calcule el descuento aplicado a un producto. 
# Recibe dos parámetros (precio original y precio con descuento) y devuelve el porcentaje de descuento aplicado.
'''
def calcular_descuento(precio_original,precio_con_descuento):
    """ 
    calcula el descuento aplicado a un producto
    precio original y el precio con descuento como parametro
    retorna el precio con el decuento aplicado    
    """
    descuento = precio_original - precio_con_descuento
    precio_con_descuento = (descuento / precio_original) * 100
    return precio_con_descuento

'''

#  EJERCICIO 4 Crear una función que calcule el promedio de edad de un grupo de personas. Recibe una lista de edades y devuelve el promedio.
'''
def calcular_promedio_edad(edades):
    """
    Esta función toma una lista de edades como entrada y devuelve el promedio de edad.
    las edades como parametro
    retorna el promedio de edades
    """
    suma_edades = sum(edades)
    cantidad_personas = len(edades)
    promedio = suma_edades / cantidad_personas
    return promedio

'''

#  EJERCICIO 5 
# Crear una función que determine si un número es primo o no. 
# Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.
'''
def es_primo_o_noprimo(valor_numero):
    """
    determina si es primo o no
    el numero como parametro
    retorna o true o flase
    """
    if valor_numero % 2 == 0:
        return True
    else:
        return False

'''

#  EJERCICIO 6 Crear una función que calcule el área de un triángulo. Recibe dos parámetros (base y altura) y devuelve el área.
'''
def area_triangulo(base, altura):
    """
    calcula el area de un triangulo
    la base y la altura como parametro
    retorna el area
    """
    area = (base * altura) / 2
    return area

'''

#  EJERCICIO 7 
# Crear una función que calcule el máximo común divisor de dos números. 
# Recibe dos parámetros (números) y devuelve el máximo común divisor.
'''
def calcula_maximo_divisor_comun(numero_uno, numero_dos):
    """
    Calcula el máximo común divisor de dos números enteros
    dos numeros como parametros
    retorna el maximo comun divisor
    """
    while numero_dos != 0:
        numero_uno, numero_uno = numero_uno, numero_uno % numero_uno
    return numero_uno

'''

#  EJERCICIO 8 
# Crear una función que verifique si un número es par o impar. 
# Recibe un número como parámetro y devuelve True si es par o False si es impar.
'''
def es_par_o_impar(numero):

    """
    verifica si es par o impar
    numero como parametro
    retorna true o false
    """
    if numero % 2 == 0:
        return True
    else:
        return False

'''

#  EJERCICIO 9 
# Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. 
# Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.
'''
def contar_elemento(lista, elemento):
    """
    cuenta la cantidad de veces que aparece un elemento en la lista
    lista y elemnto por parametro
    retorna la cantidad de veces que aparece un elemento en la lista
    """
    return lista.count(elemento)

'''

#  EJERCICIO 10 Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.
'''
def palabra_mas_larga(lista):
    """
    busca la palabra mas larga
    lista como parametro
    retorna la palabra mas larga
    """
    palabra_mas_larga = ""
    for palabra in lista:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga

'''

#  EJERCICIO 11 Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.
'''
def contar_vocales(cadena):
    """
    Esta función cuenta la cantidad de vocales en una cadena de texto
    cadena como parametro
    retorna la cantidad de vocales que tiene
    
    """
    vocales = "aeiouAEIOU"  
    cantidad = 0  
    for caracter in cadena:  
        if caracter in vocales:  
            cantidad += 1
    return cantidad  

'''

#  EJERCICIO 12 Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas

#  EJERCICIO 13 
# Crear una función que recibe una lista de palabras y 
# devuelve un diccionario con las palabras como llaves y su longitud como valores.

#  EJERCICIO 14 
# Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo, 
# el valor máximo y el promedio de los números en la lista.

#  EJERCICIO 15 
# Crear una función que recibe una lista de diccionarios con información de películas (título, género, director) 
# y devuelve un diccionario con la cantidad de películas por género.

lista_peliculas =\
[
  {
    "titulo": "pepe",
    "genero": "hola",
    "director": "jose"
  },
  {
    "titulo": "pepe",
    "genero": "hola",
    "director": "jose"
  },
  {
    "titulo": "pepe3",
    "genero": "hola2",
    "director": "jose"
  },
  {
    "titulo": "pepe8",
    "genero": "hola4",
    "director": "jose"
  }
  
]


def calcular_pelicula_por_genero(lista_de_peliculas):
    
    contador_diccionario = {}
    
    for pelicula in lista_de_peliculas:
        clave_pelicula = pelicula['genero']
        
        if clave_pelicula in contador_diccionario:
            contador_diccionario[clave_pelicula] += 1
        else:
            contador_diccionario[clave_pelicula] = 1
    
    return contador_diccionario

imprimir = calcular_pelicula_por_genero(lista_peliculas)
print(imprimir)
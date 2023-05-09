import re
import json

def imprimir_dato(dato:str)->None:
    print(dato)

# PRIMER PARTE

#1.1
def imprimir_menu_desafio_5():
    '''
    imprime el menu de opciones por pantalla
    '''
    imprimir_dato("Menú de opciones:")
    imprimir_dato("A - Funcionalidad A")
    imprimir_dato("B - Funcionalidad B")
    imprimir_dato("C - Funcionalidad C")
    imprimir_dato("D - Funcionalidad D")
    imprimir_dato("E - Funcionalidad E")
    imprimir_dato("F - Funcionalidad F")
    imprimir_dato("G - Funcionalidad G")
    imprimir_dato("H - Funcionalidad H")
    imprimir_dato("I - Funcionalidad I")
    imprimir_dato("J - Funcionalidad J")
    imprimir_dato("K - Funcionalidad K")
    imprimir_dato("L - Funcionalidad L")
    imprimir_dato("M - Funcionalidad M")
    imprimir_dato("N - Funcionalidad N")
    imprimir_dato("O - Funcionalidad O")
    imprimir_dato("Z - Salir")
    
#1.2
def stark_menu_principal_desafio_5():
    '''
    llama a la funcion que imprime la opciones
    podes elegir las opciones
    '''
    imprimir_menu_desafio_5()
    letra_elegida = input("Ingrese la letra de la opción elegida: ")
    if re.match(r'^[a-zA-Z]$', letra_elegida):
        return letra_elegida()
    else:
        return -1
#1.3  
def stark_marvel_app_5():
    '''
    llama a la funcion en la que podes elegir 
    selecciones la opcion
    '''
    while True:
        
        opcion = stark_menu_principal_desafio_5()
        
        
        if re.match("[a-zA-Z]", opcion):
            opcion = opcion.upper()
            
            
            if opcion == "A":
                pass
            elif opcion == "B":
                pass
            elif opcion == "C":
                pass
            elif opcion == "D":
                pass
            elif opcion == "E":
                pass
            elif opcion == "F":
                pass
            elif opcion == "G":
                pass
            elif opcion == "H":
                pass
            elif opcion == "I":
                pass
            elif opcion == "J":
                pass
            elif opcion == "K":
                pass
            elif opcion == "L":
                pass
            elif opcion == "M":
                pass
            elif opcion == "N":
                pass
            elif opcion == "O":
                pass
            elif opcion == "Z":
                print("Saliendo del programa...")
                break
        else:
            print("Opción inválida. Intente nuevamente.")
            opcion = -1
    return

#1.4
def leer_archivo(nombre_archivo):
    '''
    lee un archivo json
    '''
    with open(nombre_archivo, 'r') as archivo:
        contenido = json.load(archivo)
    return contenido

#1.5    
def guardar_archivo(nombre_archivo:str, contenido:str):
    '''
    se crea un archivo y se guarda
    '''
    try:
        with open(nombre_archivo, 'w+') as archivo:
           datos_chequeados =  archivo.write(contenido)
        print(f"Se creó el archivo: {nombre_archivo}")
        return True
    except:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False
    
#1.6
def capitalizar_palabras(texto:str): # capitalizarla significaría transformarla en "Hola Mundo".
    '''
    la primer letra de cada palabra tiene mayuscula
    '''
    resultado = ""
    capitalizar_siguiente = True
    for letra in texto:
        if capitalizar_siguiente and letra.isalpha():
            resultado += letra.upper()
            capitalizar_siguiente = False
        else:
            resultado += letra
        if letra.isspace():
            capitalizar_siguiente = True
    return resultado
#1.7
def obtener_nombre_capitalizado(heroe:str):
    '''
    utilizamos la funcion de capitalizar palabra para los nombres
    '''
    nombre = heroe.get('name', '')
    nombre_capitalizado = capitalizar_palabras(nombre)
    return f"Nombre: {nombre_capitalizado}"

#1.8 

def obtener_dato_y_dato(heroe, key:str):
    '''
    devuelve los datos de un heroe
    '''
    nombre = obtener_nombre_capitalizado(heroe)
    if key in heroe:
        dato = str(heroe[key])
        return f"Nombre: {nombre} | {key}: {dato}"
    else:
        return f"No se encontró la key {key} en el diccionario del héroe."
    
#SEGUNDA PARTE

#2.1

def es_genero(heroe, genero):
    """
    Determina si un héroe es del género buscado
    diccionario que representa al héroe
    return True si el héroe es del género buscado, False de lo contrario
    """
    if 'genero' in heroe and heroe['genero'] == genero:
        return True
    else:
        return False
    
#2.2

def stark_guardar_heroe_genero(heroes, genero ):
    '''
    reutiliza otra funciones 
    guarda archivos 
    '''
    nombres = []
    for heroe in heroes:
        if es_genero(heroe, genero):
            nombre = capitalizar_palabras(heroe['nombre'])
            nombres.append(nombre)
            print(obtener_nombre_capitalizado(heroe), "|", imprimir_dato(heroe, 'genero'))
    nombre_archivo = f"heroes_{genero}.csv"
    return guardar_archivo(nombre_archivo, nombres)

#TERCERA PARTE 

#3.1

def calcular_min_genero(heroes, key, genero):
    
    valor_min = float('inf')
    heroe_min = None

    encontrado_genero = False

    for heroe in heroes:
        
        if heroe['genero'] == genero or genero == 'NB':
            
            if not encontrado_genero:
                encontrado_genero = True
                valor_min = heroe[key]
                heroe_min = heroe
            else:
               
                if heroe[key] < valor_min:
                    valor_min = heroe[key]
                    heroe_min = heroe
    
    return heroe_min

#3.2

def calcular_max_genero(heroes, key, genero):
    max_valor = None
    max_heroe = None
    
    
    for heroe in heroes:
        if es_genero(heroe, genero):
            max_valor = heroe.get(key)
            max_heroe = heroe
            break
    
    for heroe in heroes:
        if es_genero(heroe, genero):
            valor_actual = heroe.get(key)
            if valor_actual > max_valor:
                max_valor = valor_actual
                max_heroe = heroe
    
    return obtener_nombre_capitalizado(max_heroe)
    
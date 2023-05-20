import json
import re
import csv

def leer_archivo(ruta_archivo:str):

    with open(ruta_archivo,'r') as archivo:
        datos = json.load(archivo)
    return datos

def listar_heroes(heroes:str,cantidad):
    if cantidad > len(heroes):
        print("la cantidad que ingreso excede a la lista.")
    else:
        print(f"Los primeros {cantidad} héroes son: ")
        for indice in range(cantidad):
            print(heroes[indice])
            
            
def ordenar_por_altura(lista_heroes:str, orden)->list:
    '''
    la funcion va a ordenar segun lo que desee el usuario, de forma asc o desc
    la lista de heroes como parametro
    retorna la lista ordenada
    '''
    cantidad = len(lista_heroes)-1
    
    for indice in range(cantidad-1):
        for elemento in range(cantidad - indice - 1):
            if orden == 'asc':
                if lista_heroes[elemento]['altura'] > lista_heroes[elemento+1]['altura']:
                    lista_heroes[elemento],lista_heroes[elemento+1] = lista_heroes[elemento+1],lista_heroes[elemento]
            elif orden == 'desc':
                if lista_heroes[elemento]['altura'] < lista_heroes[elemento+1]['altura']:
                    lista_heroes[elemento],lista_heroes[elemento+1] = lista_heroes[elemento+1],lista_heroes[elemento]
    
    return lista_heroes
                
            
def ordenar_por_fuerza(lista_heroes:str, orden)->list:
    '''
    la funcion va a ordenar segun lo que desee el usuario, de forma asc o desc
    la lista de heroes como parametro
    retorna la lista ordenada
    '''
    cantidad = len(lista_heroes)
    
    for indice in range(cantidad-1):
        for elemento in range(cantidad - indice - 1):
            if orden == 'asc':
                if lista_heroes[elemento]['fuerza'] > lista_heroes[elemento+1]['fuerza']:
                    lista_heroes[elemento],lista_heroes[elemento+1] = lista_heroes[elemento+1],lista_heroes[elemento]
            elif orden == 'desc':
                if lista_heroes[elemento]['fuerza'] < lista_heroes[elemento+1]['fuerza']:
                    lista_heroes[elemento],lista_heroes[elemento+1] = lista_heroes[elemento+1],lista_heroes[elemento]
    
    return lista_heroes   


def calcular_promedio(lista:list,key:str)->float:
    acumulador = 0
    contador = 0
    resultado = 0
    
    if(len(lista) == 0):
        return 0
    for elemento in lista:
        if key in elemento:
            acumulador += elemento[key]
            contador += 1

    if(contador > 0):
        resultado = acumulador / contador
        
    return resultado



          
while True:
    
    print("1.Listar los primeros N héroes")
    print("2.Ordenar y Listar héroes por altura")
    print("3.Ordenar y Listar héroes por fuerza")
    print("4.Calcular promedio de cualquier key numérica")
    print("5.Buscar héroes por inteligencia")
    print("6.Exportar a CSV ")
    
    print("0.Salir.")
    
    opcion = input("ingrese una opcion: ")
    
    
    
    if opcion == "1":
        
        ruta_archivo = "data_stark.json"
        datos = leer_archivo(ruta_archivo)
        
        heroes = datos.get("heroes", [])
        
        cantidad = int(input("Ingrese el la cantidad que quiera ver: "))

        listar_heroes(heroes, cantidad)
        
    elif opcion == "2":
        
        ruta_archivo = "data_stark.json"
        datos = leer_archivo(ruta_archivo)
        
        heroes = datos.get("heroes", [])
       
        cantidad = int(input("Ingrese el la cantidad que quiera ver: "))
       
        orden = input("Ingrese el orden de clasificación ('asc' o 'desc'): ")
        if orden != 'asc' and orden != 'desc':
            print("Orden inválido. Debe ser 'asc' o 'desc'.")
        
        heroes_ordenados = ordenar_por_altura(heroes, orden)
        
        listar_heroes(heroes_ordenados, cantidad)
        
    elif opcion == "3":
       
        ruta_archivo = "data_stark.json"
        datos = leer_archivo(ruta_archivo)
        
        heroes = datos.get("heroes", [])
       
        cantidad = int(input("Ingrese el la cantidad que quiera ver: "))
       
        orden = input("Ingrese el orden de clasificación ('asc' o 'desc'): ")
        if orden != 'asc' and orden != 'desc':
            print("Orden inválido. Debe ser 'asc' o 'desc'.")
        
        heroes_ordenados = ordenar_por_fuerza(heroes, orden)
        
        listar_heroes(heroes_ordenados, cantidad)
       
    elif opcion == "4":
        
        ruta_archivo = "data_stark.json"  
        datos = leer_archivo(ruta_archivo)

        lista_valores = datos["heroes"]  
        clave = "fuerza"  

        promedio = calcular_promedio(lista_valores, clave)
        print(f"El promedio de los valores de la clave '{clave}' es: {promedio}")
       
    elif opcion == "5":
        
        pass
    
    elif opcion == "6":
        
        pass

      
    elif opcion == "0":
        print("gracias por usar el programa...")
        break
    else:
        print("ingrese una opcion valida (1 al6 y salir 0)!!")


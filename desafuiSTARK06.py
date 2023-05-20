import json

def leer_archivo(ruta_archivo:str):

    with open(ruta_archivo,'r') as archivo:
        datos = json.load(archivo)
    return datos
'''
datos = leer_archivo('data_stark.json')
print(datos)

'''

def ordenar_por_altura(lista_heroes:str):
    '''
    como parametro tiene una variable de heroes 
    va a ordenar la lista por altura de manera ascendente
    va a retornar la lista ordenada por altura
    '''
    n = len(lista_heroes)
    
    for indice in range(n):
        for elemento in range(0,n-indice-1):
            if lista_heroes[elemento]['altura'] > lista_heroes[elemento+1]['altura']:
                lista_heroes[elemento],lista_heroes[elemento+1] = lista_heroes[elemento+1],lista_heroes[elemento]
    return lista_heroes

def ordenar_por_peso(lista_heroes:str):
    '''
    como parametro tiene una variable de heroes 
    va a ordenar la lista por peso de manera ascendente
    va a retornar la lista ordenada por peso
    '''
    n = len(lista_heroes)
    
    for indice in range(n):
        for elemento in range(0,n-indice-1):
            if lista_heroes[elemento]['peso'] > lista_heroes[elemento+1]['peso']:
                lista_heroes[elemento],lista_heroes[elemento+1] = lista_heroes[elemento+1],lista_heroes[elemento]
    return lista_heroes

def ordenar_por_nombre(lista_heroes:str):
    '''
    como parametro tiene una variable de heroes 
    va a ordenar la lista por nombre de manera ascendente
    va a retornar la lista ordenada por nombre
    '''
    n = len(lista_heroes)
    
    for indice in range(n):
        for elemento in range(0,n-indice-1):
            if lista_heroes[elemento]['nombre'].lower() > lista_heroes[elemento+1]['nombre'].lower():
                lista_heroes[elemento],lista_heroes[elemento+1] = lista_heroes[elemento+1],lista_heroes[elemento]
    return lista_heroes

def ordenar_por_largo_nombre(lista_heroes:str):
    '''
    Recibe como parámetro una lista de héroes y devuelve la lista ordenada por el largo de los nombres de forma descendente
    '''
    n = len(lista_heroes)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if len(lista_heroes[j]['nombre']) < len(lista_heroes[j+1]['nombre']):
                lista_heroes[j], lista_heroes[j+1] = lista_heroes[j+1], lista_heroes[j]
                
    return lista_heroes

def ordenar_por_key(lista_heroes, key, ascendente=True):
    '''
    Ordena la lista de heroes según la key especificada.
    El sentido de ordenamiento lo determina el tercer parámetro.
    '''
    n = len(lista_heroes)
    
    for indice in range(n):
        for elemento in range(0, n-indice-1):
            if ascendente:
                if lista_heroes[elemento][key] > lista_heroes[elemento+1][key]:
                    lista_heroes[elemento], lista_heroes[elemento+1] = lista_heroes[elemento+1], lista_heroes[elemento]
            else:
                if lista_heroes[elemento][key] < lista_heroes[elemento+1][key]:
                    lista_heroes[elemento], lista_heroes[elemento+1] = lista_heroes[elemento+1], lista_heroes[elemento]
                    
    return lista_heroes

while True:
    
    print("1.ordenar por altura")
    print("2.ordenar por peso")
    print("3.ordenar por nombre")
    print("4.ordenar por largo de nombre")
    print("5.ordenar por key")
    
    print("0.Salir.")
    
    opcion = input("ingrese una opcion: ")
    
    
    
    if opcion == "1":
        
        datos = leer_archivo('data_stark.json')
        datos_ordenados = ordenar_por_altura(datos['heroes'])
        for heroe in datos_ordenados:
            print(heroe['altura'])
        
    elif opcion == "2":
         
        datos = leer_archivo('data_stark.json')
        datos_ordenados = ordenar_por_peso(datos['heroes'])
        for heroe in datos_ordenados:
            print(heroe['peso'])
        
    elif opcion == "3":
       
        datos = leer_archivo('data_stark.json')
        datos_ordenados = ordenar_por_nombre(datos['heroes'])
        for heroe in datos_ordenados:
            print(heroe['nombre'])
       
    elif opcion == "4":
        
        datos = leer_archivo('data_stark.json')
        datos_ordenados = ordenar_por_largo_nombre(datos['heroes'])
        for heroe in datos_ordenados:
            print(heroe['nombre'])
       
    elif opcion == "5":
        
       # heroes_ordenados = ordenar_por_key(lista_heroes, 'altura', ascendente=False)
        pass

      
    elif opcion == "0":
        print("gracias por usar el programa...")
        break
    else:
        print("ingrese una opcion valida (1 al 5 y salir 0)!!")
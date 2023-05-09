from data_stark import lista_personajes


def stark_normalizar_datos(lista_heroes:list)->list:
    """
    recorre la lista y valida los tipos de datos
    muestra si se modifico un dato
    que la lista no este vacia 
    el parametro el la lista de superheroes
    """
    bandera = False
    if len(lista_heroes) != 0:
        for heroe in lista_heroes:
            for informacion in heroe:
                if type(heroe[informacion]) != float:
                    if heroe[informacion].replace(".", "").isdigit():
                        heroe[informacion] = float(heroe[informacion])
                        bandera = True
    else:
        print("ERROR: la lista esta vacia")
    if bandera:
        print("datos normalizados")
     
    return lista_heroes 
    
def obtener_nombre(lista_heroes:dict):
    """
    obtiene el nombre del personaje
    como parametro el listado de heroes
    """
    para_retorno = lista_heroes["nombre"]
    return  para_retorno

def imprimir_dato(cadena: str):
    """
    imprime los datos
    como parametro un diccionario de tipo string
    """
    print(cadena)


def stark_imprimir_nombres_heroes(heroes:str):
    if not heroes:
        return -1
    else:
        for heroe in heroes:
            nombre = obtener_nombre(heroe)
            print(nombre)

def obtener_nombre_y_dato(heroe, dato):
    nombre = heroe.get('nombre', '')
    valor = dato.get('fuerza', '')
    return f"Nombre: {nombre} | {dato}: {valor}"

while True:
    
    print("1.normalizar datos")
    print("2.obtener nombre")
    print("3.imprimir datos")
    print("4.imprimir nombres")
    print("5.obtiene el nombre y un dato")
    print("6.")
    print("7.")
    print("8.")
    print("9.")
    print("10.")
    print("11.")
    print("12.")
    print("13.")
    print("14.")
         
    print("0.Salir.")
    
    opcion = input("ingrese una opcion: ")
    
    
    
    if opcion == "1":

       datos =  stark_normalizar_datos(lista_personajes)  
       print(datos)
       
    elif opcion == "2":
         
       dato = obtener_nombre(lista_personajes[0])
       print(dato)
        
    elif opcion == "3":
       
        imprimir_dato(lista_personajes)
       
    elif opcion == "4":
        
       dato = stark_imprimir_nombres_heroes(lista_personajes)
       print(dato)
       
    elif opcion == "5":
        
        obtener_nombre_y_dato(lista_personajes, dato)
        
        
    elif opcion == "6":
       
        pass
       
    
    elif opcion == "7":
       
        pass
       

    elif opcion == "8":
       
       pass
       
    elif opcion == "9":
       
        pass
        
    elif opcion == "10":
       
      pass
       
    elif opcion == "11":
       
      pass
       
    elif opcion == "12":
       
       pass
       
    elif opcion == "13":
       
       pass
       
    elif opcion == "14":
       
       pass
            
    elif opcion == "0":
        print("gracias por usar el programa...")
        break
    else:
        print("ingrese una opcion valida (1 al 14) (0 para salir)!!")
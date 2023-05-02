# MERINO LEANDRO 1E

from data_stark import lista_personajes


def imprimir_superheroe_masculino(lista_superheroes):
    '''
    imprime el nombre de los heroes masculinos
    lista de heroes como parametro
    '''
    for heroe in lista_superheroes:
        if heroe['genero'] == 'M':
            print(heroe['nombre'])
            
def imprimir_superheroe_femeninos(lista_superheroes):
    '''
    imprime el nombre de los heroes femeninos
    lista de heroes como parametro
    '''
    for heroe in lista_superheroes:
        if heroe['genero'] == 'F':
            print(heroe['nombre'])
 
"""
def imprimir_mas_alto_genero(personaje:list, genero:str):
    superheroe_mas_alto = None
    altura_maxima = 0
    for personaje in lista_personajes:
        if personaje["genero"] == genero:
            altura = float(personaje["altura"])
            if altura > altura_maxima:
                altura_maxima = altura
                superheroe_mas_alto = personaje["nombre"]

    print(f"El superhéroe más alto de género {genero} es: {superheroe_mas_alto} con una altura de {altura_maxima} cm")
    imprimir_mas_alto_genero(lista_personajes,"M")
    imprimir_mas_alto_genero(lista_personajes,"F") 
"""


  
def heroe_mas_alto_masculino(lista_superheroes):
    '''
    imprime el nombre de los heroes mas altos masculinos
    lista de heroes como parametro
    '''
    altura_maxima = ""
    superheroe_mas_alto = None

    for superheroe in lista_superheroes:
        
        if superheroe["genero"] == 'M':
            if superheroe["altura"] > altura_maxima:
                altura_maxima = superheroe["altura"]
                superheroe_mas_alto = superheroe["nombre"]

    return superheroe_mas_alto


def heroe_mas_alto_femenino(lista_superheroes):
    '''
    imprime el nombre de los heroes mas altos femeninos
    lista de heroes como parametro
    retorna femenino mas alto
    '''
    altura_maxima = ""
    superheroe_mas_alto = None

    for superheroe in lista_superheroes:
        
        if superheroe["genero"] == 'F':
            if superheroe["altura"] > altura_maxima:
                altura_maxima = superheroe["altura"]
                superheroe_mas_alto = superheroe["nombre"]

    return superheroe_mas_alto

def heroe_mas_bajo_masculino(lista_superheroes):
    '''
    imprime el nombre de los heroes mas bajos masculinos
    lista de heroes como parametro
    retorna masculino mas bajo
    '''
    altura_mainima = ""
    superheroe_mas_bajo = ""

    for superheroe in lista_superheroes:
        
        if superheroe["genero"] == 'M':
            if superheroe["altura"] < altura_mainima:
                altura_mainima = superheroe["altura"]
                superheroe_mas_bajo = superheroe["nombre"]

    return superheroe_mas_bajo

def heroe_mas_bajo_femenino(lista_superheroes):
    
    '''
    imprime el nombre de los heroes mas bajos femeninos
    lista de heroes como parametro
    retorna femenino mas bajo
    '''
    altura_mainima = ""
    superheroe_mas_bajo = ""

    for superheroe in lista_superheroes:
        
        if superheroe["genero"] == 'F':
            if superheroe["altura"] < altura_mainima:
                altura_mainima = superheroe["altura"]
                superheroe_mas_bajo = superheroe["nombre"]

    return superheroe_mas_bajo


def calcular_promedio_altura_masculinos(lista_superheroes):
    '''
    calcula el promedio de la altura de masculinos
    lista de heroes como parametro
    retorna el promedio de la altura
    '''
    cantidad_masculinos = 0
    suma_alturas_masculinos = 0
    
    for heroe in lista_superheroes:
        
        if heroe['genero'] == 'M':
            suma_alturas_masculinos += float(heroe['altura'])
            cantidad_masculinos += 1
     
    altura_promedio = suma_alturas_masculinos / cantidad_masculinos
    
    return altura_promedio

def calcular_promedio_altura_femeninos(lista_superheroes):
    '''
    calcula el promedio de la altura de femeninos
    lista de heroes como parametro
    retorna el promedio de la altura
    '''
    cantidad_femeninos = 0
    suma_alturas_femeninos = 0
    
    for heroe in lista_superheroes:
        
        if heroe['genero'] == 'F':
            suma_alturas_femeninos += float(heroe['altura'])
            cantidad_femeninos += 1
     
    altura_promedio = suma_alturas_femeninos / cantidad_femeninos
    
    return altura_promedio


def contador_de_ojos_cada_tipo(lista_superheroes):
    """
    cuenta la cantidad de ojos de cada tipo de los heroes
    devuelve la cantidad de tipos de ojos 
    """
    
    contador_ojos = {}
    
    for superheroe in lista_superheroes:
        color_ojos = superheroe.get("color_ojos", "desconocido") # el desconocido se utiliza para los que no tienen color de ojos
        if color_ojos in contador_ojos:
            contador_ojos[color_ojos] +=1
        else:
            contador_ojos[color_ojos] = 1
    
    return contador_ojos


def contador_de_pelo_cada_tipo(lista_superheroes):
    """
    cuenta la cantidad de tipos de pelo de los heroes
    devuelve la cantidad de tipos de pelo
    """
    
    contador_pelo = {}
        
    for superheroe in lista_superheroes:
        color_de_pelo = superheroe.get("color_pelo", "desconocido") # el desconocido se utiliza para los que no tienen color de pelo
        if color_de_pelo in contador_pelo:
            contador_pelo[color_de_pelo] +=1
        else:
            contador_pelo[color_de_pelo] = 1
        
    return contador_pelo

def contador_tipo_de_inteligencia(lista_superheroes):
    """
    cuenta la cantidad de inteligencia que tienen los heroes
    devuelve la cantidad de inteligencia
    """
    
    contador_inteligencia = {}
        
    for superheroe in lista_superheroes:
        tipo_de_inteligencia = superheroe.get("inteligencia", "no_tiene") # el desconocido se utiliza para los que no tienen color de pelo
        if tipo_de_inteligencia in contador_inteligencia:
            contador_inteligencia[tipo_de_inteligencia] +=1
        else:
            contador_inteligencia[tipo_de_inteligencia] = 1
        
    return contador_inteligencia

def listado_por_grupo_ojos(lista_superheroes):
    """
    lista en grupos por sus ojos
    devuelve el listado
    """
    color_ojos = {}
    
    for heroe in lista_superheroes:
        if 'color_ojos' in heroe:
            color = heroe['color_ojos']
        if color in color_ojos:
            
            color_ojos[color].append(heroe['nombre'])
        else:
            color_ojos[color] = [heroe['nombre']]
    return color_ojos

def listado_por_grupo_pelo(lista_superheroes):
    """
    lista en grupos por su pelo
    devuelve el listado
    """
    color_pelo = {}
    
    for heroe in lista_superheroes:
        if 'color_pelo' in heroe:
            color = heroe['color_pelo']
        if color in color_pelo:
            
            color_pelo[color].append(heroe['nombre'])
        else:
            color_pelo[color] = [heroe['nombre']]
    
    return color_pelo

def listado_por_grupo_inteligencia(lista_superheroes):
    """
    lista en grupos por su inteligencia
    devuelve el listado
    """
    color_inteligencia = {}
    
    for heroe in lista_superheroes:
        if 'inteligencia' in heroe:
            tipo = heroe['inteligencia']
        if tipo in color_inteligencia:
            
            color_inteligencia[tipo].append(heroe['nombre'])
        else:
            color_inteligencia[tipo] = [heroe['nombre']]
    
    return color_inteligencia

while True:
    
    print("1.Imprimir el nombre de los superheroes masculinos")
    print("2.Imprimir el nombre de los superheroes femeninos")
    print("3.heroe mas alto masculino")
    print("4.heroe mas alto femenino")
    print("5.heroe mas bajo masculino")
    print("6.heroe mas bajo femenino")
    print("7.promedio altura masculinos")
    print("8.promedio altura femeninos")
    print("9.color de ojos de cada heroe")
    print("10.color de pelo de cada heroe")
    print("11.tipo de inteligencia")
    print("12.agrupados por color de ojos")
    print("13.agrupados por color de pelo")
    print("14.agrupados por inteligencia")
         
    print("0.Salir.")
    
    opcion = input("ingrese una opcion: ")
    
    
    
    if opcion == "1":

        imprimir_superheroe_masculino(lista_personajes)
        
    elif opcion == "2":
         
        imprimir_superheroe_femeninos(lista_personajes)
        
    elif opcion == "3":
       
        superheroe_mas_alto = heroe_mas_alto_masculino(lista_personajes)
        print("El superhéroe más alto del género 'M' es:", superheroe_mas_alto)
       
    elif opcion == "4":
        
        superheroe_mas_alto_femenino = heroe_mas_alto_femenino(lista_personajes)
        print("El superhéroe más alto del género 'F' es:", superheroe_mas_alto_femenino)
        
       
    elif opcion == "5":
        
        superheroe_mas_bajo = heroe_mas_bajo_masculino(lista_personajes)
        print("El superhéroe más bajo del género 'M' es:", superheroe_mas_bajo)
        
    elif opcion == "6":
       
        superheroe_mas_bajo_femenino = heroe_mas_bajo_femenino(lista_personajes)
        print("El superhéroe más bajo del género 'F' es:", superheroe_mas_bajo_femenino)
       
    
    elif opcion == "7":
       
        promedio_altura = calcular_promedio_altura_masculinos(lista_personajes)
        print("El promedio de la altura de los heroes 'M' es:", promedio_altura)
       

    elif opcion == "8":
       
       promedio_altura = calcular_promedio_altura_femeninos(lista_personajes)
       print("El promedio de la altura de los heroes 'F' es:", promedio_altura)
       
    elif opcion == "9":
       
        recuento = contador_de_ojos_cada_tipo(lista_personajes)
        print(recuento)
        
    elif opcion == "10":
       
       recuento = contador_de_pelo_cada_tipo(lista_personajes)
       print(recuento)
       
    elif opcion == "11":
       
       recuento = contador_tipo_de_inteligencia(lista_personajes)
       print(recuento)
       
    elif opcion == "12":
       
       listado = listado_por_grupo_ojos(lista_personajes)
       print(listado)
       
    elif opcion == "13":
       
       listado = listado_por_grupo_pelo(lista_personajes)
       print(listado)
       
    elif opcion == "14":
       
       listado = listado_por_grupo_inteligencia(lista_personajes)
       print(listado)
            
    elif opcion == "0":
        print("gracias por usar el programa...")
        break
    else:
        print("ingrese una opcion valida (1 al 14) (0 para salir)!!")
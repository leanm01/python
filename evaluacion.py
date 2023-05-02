# MERINO LEANDRO 1E

def recibir_string_mayuscula(texto):
    """
    transforma de minuscula a mayuscula
    retorna el texto en mayuscula
    """
    texto_a_mayusc = texto.upper()
    return texto_a_mayusc
    
def recibir_string_minuscula(texto):
    """
    transforma de mayuscula a minuscula
    retorna el texto en minuscula
    """
    texto_a_minuscula = texto.lower()
    return texto_a_minuscula


def concatenar_string(string_uno, string_dos):
    """
    concatena dos strings
    dos parametros para los string
    retorna esos strings concatenados
    
    """
    concatenar = ", ".join([string_uno, string_dos]) 
    return concatenar


def de_cadena_a_numero(cadena):
    """
    transforma de cadena a cantidad de caracteres 
    devuelve el la cantidad de los caracteres en numeros
    """
    tamanio = len(cadena)
    return tamanio

def contar_el_caracter(cadena, caracter):
    """
    cuenta la cantidad de caracteres de una cadena en especifico
    devuelva la cantidad de un caracter
    """
    
    contador = cadena.count(caracter)
    return contador   

def contador_palabras_de_cadena(texto,caracter):
    """
    devuelve todas las palabras de la cadena
    """
    palabras = texto.split()
    palabras_para_contar = []
    
    for palabra in palabras:
        if palabra.count(caracter) > 0:
            palabras_para_contar.append(palabra)
    
    return palabras_para_contar

def espacio_eliminados(cadena):
    """
    elimina los espacios de la cadena
    """
    sin_espacios = cadena.replace(" ","")
    return sin_espacios


def sin_espacios_con_diccionario(nombre,apellido):
    """
    devuelve sin espacios el diccionario
    """
    nombre = nombre.strip()
    apellido = apellido.strip()
    
    nombre = nombre[0].upper() + nombre[1:]
    apellido = apellido[0].upper() + apellido[1:]
    
    diccionario_aux = {"nombre":nombre, "apellido":apellido}
    
    return diccionario_aux

def unir_lista(nombres):
    """
    une los nombres con un salto de linea
    """
    salto = "\n".join(nombres)
    return salto

def devolver_email(nombre,apellido):
    """
    devuelve un email
    """
    email = "{}_{}@utn-fra.com.ar".format(nombre,apellido)
    return email

'''
11
'''

'''
def digitos_ocultos(numero_tarjeta):
    """
    oculta los digitos de una tarjeta de credito
    """
    
    numeros = numero_tarjeta.isdigit()
    numeros_ocultos = "**** **** ****" +numeros[-4:] 

    return numeros_ocultos
'''
    
    
def eliminar_caracteres_email(email):
    """
    elimina lo que le sigue a @
    """
    email_aux = email.split("@")[0] # @ es el separador y 0 el nombre
    return email_aux
    
'''
14
'''

'''
15
'''

'''
16
'''

'''
17
'''

def cambio_minusculas_por_mayusculas(cadena):
    """
    cambia de minusculas a mayusculas o vice versa
    """
    cambio = cadena.swapcase()
    return cambio

'''
19
'''

'''
20
'''

def contador_de_palabras(texto):
    """
    cuenta la cantidad de palabras
    retorna esa cantidad
    """
    diccionario = {}
    
    palabras = texto.split()
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    
    return diccionario
    
while True:
    
    print("1.de minuscula a mayuscula")
    print("2.de mayuscula a minuscula")
    print("3.para concatenar dos cadenas")
    print("4.de cadena a cantidad de caracteres")
    print("5.contar los caracteres de una cadena en especifico")
    print("6.contador de palabras")
    print("7.eliminar los espacios de la cadena")
    print("8.sin espacios y con minusculas")
    print("9.unir lista en una sola cadena con salto de linea")
    print("10.devuelve un email")
    print("11.")
    print("12.numeros de tarjeta ocultos")
    print("13.elimina caracteres despues del @")
    print("14.")
    print("15.")
    print("16.")
    print("17.")
    print("18.cambia minusculas por mayusculas o vice versa")
    print("19.")
    print("20.")
    print("21.cuenta las palabras")
         
    print("0.Salir.")
    
    opcion = input("ingrese una opcion: ")
    
    
    
    if opcion == "1":

        texto = "hola profe"
        texto_a_mayuscula = recibir_string_mayuscula(texto)
        print(texto_a_mayuscula)
        
    elif opcion == "2":
         
        texto = "HOLA PROFE"
        texto_a_minuscula = recibir_string_minuscula(texto)
        print(texto_a_minuscula)
        
    elif opcion == "3":
       
        cadena_uno = "hola"
        cadena_dos = "profe"
        para_concatenar = concatenar_string(cadena_uno, cadena_dos)
        print(para_concatenar)
       
    elif opcion == "4":
        
        cadena = "hola, profe"
        a_cantidad = de_cadena_a_numero(cadena)
        print("La cantidad es: ",a_cantidad)
        
       
    elif opcion == "5":
        
        texto = "hola profe"
        caracter = "o"
        contador = contar_el_caracter(texto,caracter)
        print(texto,contador)
        
    elif opcion == "6":
       
        texto = "hola profe como estas"
        letra = "o"
        contador_palabras_con_caracter = contador_palabras_de_cadena(texto, letra)
        print(contador_palabras_con_caracter)
       
    
    elif opcion == "7":
       
        cadena = "h o l a"
        sin_espacios = espacio_eliminados(cadena)
        print(sin_espacios)

    elif opcion == "8":
       
        nombre = "pepe"
        apellido = "perez"
        
        nombre_apellido = sin_espacios_con_diccionario(nombre,apellido)
        print(nombre_apellido)
       
    elif opcion == "9":
       
        lista_nombres = {"pepe","juan","luis"}
        cadena_con_salto = unir_lista(lista_nombres)
        print(cadena_con_salto)

    elif opcion == "10":
       
        print(devolver_email("juan", "perez"))
       
    elif opcion == "11":
       
      pass
       
    elif opcion == "12":
       '''
      numero = "1231123112311234"
      ocutlos = digitos_ocultos(numero)
      print(ocutlos)
       '''
    elif opcion == "13":
       
       correo = "juan@gmail.com"
       eliminacion_caracteres = eliminar_caracteres_email(correo)
       print(eliminacion_caracteres)
       
    elif opcion == "14":
       
       pass
   
    elif opcion == "15":
       
       pass
   
    elif opcion == "16":
       
       pass
   
    elif opcion == "17":
       
       pass
   
    elif opcion == "18":
       
       cadena = "HoLa"
       invertir = cambio_minusculas_por_mayusculas(cadena)
       print(invertir)
   
    elif opcion == "19":
       
       pass
   
    elif opcion == "20":
       
       pass
   
    elif opcion == "21":
       
       texto = "perro perro gato escudo guardia guardia guardia hola"
       texto_contado = contador_de_palabras(texto)
       print(texto_contado)
            
    elif opcion == "0":
        print("gracias por usar el programa...")
        break
    else:
        print("ingrese una opcion valida (1 al 21) (0 para salir)!!")
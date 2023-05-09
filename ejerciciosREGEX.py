#  EJERCICIO 1 
# Crear una función llamada es_mayuscula que reciba un string y 
# devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario

'''
import re

def es_mayuscula(cadena:str):
    if re.match(r'^[A-Z]+$', cadena):
        print("tiene mayusculas")
        return True
    else:
        print("no tiene mayusculas")
        return False
    
texto = input("ingresar palabra en mayuscula: ")
es_mayuscula(texto)

'''



#  EJERCICIO 2 
# Crear una función llamada es_minuscula que reciba un string y 
# devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario
'''
import re

def es_mayuscula(cadena:str):
    if re.match(r'^[a-z]+$', cadena):
        print("tiene minusculas")
        return True
    else:
        print("no tiene minusculas")
        return False
    
texto = input("ingresar palabra en minuscula: ")
es_mayuscula(texto)

'''

#  EJERCICIO 3 
# Crear una función llamada es_entero que reciba un string y 
# devuelva True en caso de que se trate de un número entero y False en caso contrario.
'''
import re

def es_entero(cadena:str):
    
    if re.match(r'^\d+$',cadena):
        print("es entero")
        return True
    else:
        print("no es entero")
        return False
    
entero = input("ingresar palabra entero: ")
es_entero(entero)

'''

#  EJERCICIO 4 
# Crear una función llamada es_solo_texto que reciba un string y 
# devuelva True en caso de que trate solo de caracteres alfabéticos y el espacio y False en el caso contrario
'''
import re

def es_solo_texto(cadena:str):
    
    if re.search(r'^[a-zA-Z ]+$', cadena):
        print("solo de caracteres alfabéticos y el espacio")
        return True
    else:
        print("no es solo de caracteres alfabéticos y el espacio")
        return False
    
texto = input("ingresar palabra: ")
es_solo_texto(texto)

'''
#  EJERCICIO 5 
# Crear una función llamada es_decimal que reciba dos strings: el primero representa la expresión a evaluar y 
# el segundo el separador decimal (puede ser punto . o coma ,). 
# Debe devolver True en caso que se trate de un número decimal y False en el caso contrario.
'''
import re

def es_decimal(expresion, separador):
    if separador == '.':
        patron = r'\d+\.\d+'
    elif separador == ',':
        patron = r'\d+,\d+'
    else:
       print("El separador debe ser punto o coma")

    return re.match(patron, expresion)

expresion = "3.14159"
separador = "."
entero = es_decimal(expresion, separador)
print(entero)

'''

#  EJERCICIO 6 
# Crear una función llamada es_alfanumerico que devuelva True en caso de tratarse de solo letras y 
# números y False en el caso contrario (es decir que contenga caracteres especiales) 
'''
import re

def es_alfanumerico(cadena:str):
    if re.match(r'^[a-zA-Z0-9]+$',cadena):
        print("esta bien")
        return True
    else:
        print("esta mal")
        return False
    
cadenas = input("ingresar palabra o numero: ")
es_alfanumerico(cadenas)

'''

#  EJERCICIO 7
# Crear una función llamada es_binario que devuelva True en caso de un número binario válido 
# (solo ceros y unos) o False en el caso contrario


'''
import re

def es_binario(cadena:str):
    if re.match(r'^[0-1]+$',cadena):
        print("esta bien")
        return True
    else:
        print("esta mal")
        return False

cadenas = input("ingresar numero: ")
es_binario(cadenas)

'''

#  EJERCICIO 8 Crear una función que reciba una lista de palabras y devuelva otra lista con las palabras  que comienzan con la letra ‘U’
'''
import re

def palabras_con_U(lista_palabras:str)-> list:
    
    palabras_con_U = []
    for palabra in lista_palabras:
        if re.match('^U\w*', palabra):
            palabras_con_U.append(palabra)
    return palabras_con_U

lista_palabras = ["Uva", "Manzana", "Uña", "Perro", "Universidad"]
palabra_con_U = palabras_con_U(lista_palabras)
print(palabra_con_U)

'''
#  EJERCICIO 9 Crear una función que reciba un texto y devuelva una lista con las palabras que contienen entre 3 y 6 caracteres de largo
'''
import re

def palabras_3_6_caracteres(texto:str)->list:
    
    palabras_largas = re.findall(r'\b\w{3,6}\b',texto)
    
    return palabras_largas 
       


textoaux = "Esta es una prueba de texto para encontrar palabras de 3 a 6 caracteres"
palabra_con_U = palabras_3_6_caracteres(textoaux)
print(palabra_con_U)

'''
   

#  EJERCICIO 10 
# Crear una función que reciba un texto y devuelva una lista de todas las palabras que terminan con ‘ción’. 
# Ejemplo de texto: https://onlinegdb.com/swyremkF6
'''
import re 

def encontrar_palabra_con_cion(texto:str):
    palabra= re.findall(r'\b\w+ción\b',texto)
    return palabra

texto_ejemplo = "https://onlinegdb.com/UMdr3hI3G"
palabras_con_cion = encontrar_palabra_con_cion(texto_ejemplo)
print(palabras_con_cion)

'''
 
#  EJERCICIO 11 Crear una función que reciba un texto y devuelva una la lista de palabras encuentra que comienzan con una vocal
'''
import re

def palabras_con_vocal(palabras:str):
    palabra = re.findall(r'\b[aeiouAEIOU]\w*\b',palabras)
    return palabra
    
texto = "El elefante entra en el edificio."
palabras_vocales = palabras_con_vocal(texto)
print(palabras_vocales)

'''
#  EJERCICIO 12 
# Crear una función llamada obtener_oraciones que reciba como parámetro un string y que devuelva una lista con las oraciones 
# (delimitadores, ‘.’, ‘!’, ‘?’). Ejemplo de texto: https://onlinegdb.com/UMdr3hI3G
'''
import re

def obtener_oracion(texto:str):
    oracion = re.split(r'^[.!?]+$',texto)
    return oracion
    
texto = "https://onlinegdb.com/UMdr3hI3G"
oraciones = obtener_oracion(texto)
print(oraciones)

'''
#  EJERCICIO 13 Crear una función que reciba un texto como parámetro y que corrija los errores de ortografía q
# ue no cumplan con la regla ortográfica que indica que antes de V se escribe N y que antes de B se escribe M.  
# Por ejemplo, si el texto es: "Mi comvicción me hace sentir que es el momento de imvertir tiempo para finalmente envarcar en esta nueva aventura." 
# La función debería devolver: “Mi convicción me hace sentir que es el momento de invertir tiempo para finalmente embarcar en esta nueva aventura."

#  EJERCICIO 14  
# Crear la función es_fecha que reciba dos string, el primero representa la expresión a evaluar y el segundo el separador de la fecha 
# (puede ser la barra / o el guión -) y 
# que devuelva True en caso de tratarse de una fecha válida y False en el caso contrario. Los formatos admitidos son: ‘dd/mm/aaaa’ o ‘dd-mm-aaaa’

#  EJERCICIO 15 
# Crear la función es_hora que reciba un string y que devuelva True en caso de tratarse de una hora válida y 
# False en el caso contrario. El formato admitido es ‘hh:mm:ss’

#  EJERCICIO 16 
# Crear la función validar_codigo_postal que reciba un string como parámetro y 
# devuelva True en caso de tratarse de código postal válido o False en caso contrario. 
'''
import re

def validar_codigo_postal(codigo:str):
    postal = re.match(r'^\d{5}$',codigo)
    return postal

codigo_postal = "12345"
if validar_codigo_postal(codigo_postal):
    print("El código postal es válido")
else:
    print("El código postal no es válido")

'''
#  EJERCICIO 17 
# Crear la función validar_patente que reciba un string como parámetro y 
# devuelva True en caso de tratarse de un número de patente válido o False en caso contrario.  
# Debe poder admitir estos dos tipos:
'''
import re

def validar_petente(patente:str):
    if re.match(r'[A-Z]{2}\d{3}[A-Z]{2}$',patente):
        print("esta bien")
        return True
    else:
        print("esta mal")
        return False

'''



#  EJERCICIO 18 
# Crear una función que se llame obtener_direcciones_email que reciba un texto y 
# devuelva una lista con todas las direcciones de email válidas que encuentren en el mismo. 
# Acá dejamos un texto de ejemplo: https://onlinegdb.com/Ln0jhatKeI

'''
import re

def obtener_direcciones_email(texto:str):
    email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',texto)
    return email

texto = """
Este es un ejemplo de texto juan.perez@example.com, maria.garcia@ejemplo.com, etc.
También hay algunas direcciones que no son válidas, como @example.com, juan@.com, etc.
"""
direcciones = obtener_direcciones_email(texto)
print(direcciones)

'''


#  EJERCICIO 19 
# Crear una función llamada validar_password que reciba un string y 
# verifique si se trata de una contraseña cumple con los requisitos mínimos de seguridad:
# Al menos 8 caracteres 
# Al menos una letra mayúscula y una letra minúscula 
# Un número  
# Un carácter especial En caso de no cumplir con alguno de los requisitos, 
# imprimir un mensaje informando cual no se cumplio

#  EJERCICIO 20 
# Crear una función llamada validar_ip que reciba un string como parámetro y verifique si se trata de una dirección IP v4 válida, 
# en caso de serlo retornar True de lo contrario retornar False.  
# Se considera una dirección IP válida si tiene el formato xxx.xxx.xxx.xxx, donde xxx es un número entero entre 0 y 255.
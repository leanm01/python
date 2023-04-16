# MERINO LEANDRO 1E

from data_stark import lista_personajes

def imprimir_nombre_superheroe():
    for superheroe in lista_personajes:
            print("\nNombre: {}\n".format(superheroe["nombre"]))
            

def imprimir_nombre_y_altura_superheroe():
    for superheroe in lista_personajes:
            print("\nNombre: {} \nAltura: {}\n".format(superheroe["nombre"],superheroe["altura"]))
            

def imprimir_superheroe_mas_alto() :
    mas_alto = 0
    for indice in range(len(lista_personajes)):
        if(indice == 0 or float(lista_personajes[mas_alto]["altura"]) < float(lista_personajes[indice]["altura"])):
            mas_alto = indice
        
    print("\nAltura: {} \nNombre: {}\n".format(lista_personajes[mas_alto]["altura"],lista_personajes[mas_alto]["nombre"]))
    
    
def imprimir_superheroe_mas_bajo():
    mas_bajo = 0
    for indice in range(len(lista_personajes)):
        if(indice == 0 or float(lista_personajes[mas_bajo]["altura"]) > float(lista_personajes[indice]["altura"])):
            mas_bajo = indice
    
    print("\nAltura: {} \nNombre: {}\n".format(lista_personajes[mas_bajo]["altura"],lista_personajes[mas_bajo]["nombre"]))   
    
    
def imprimir_identidad_superheroe():
    mas_alto = 0
    mas_bajo = 0
    
    for indice in range(len(lista_personajes)):
        if(indice == 0 or float(lista_personajes[mas_alto]["altura"]) < float(lista_personajes[indice]["altura"])):
            mas_alto = indice
        
        
         
    for indice in range(len(lista_personajes)):
        if(indice == 0 or float(lista_personajes[mas_bajo]["altura"]) > float(lista_personajes[indice]["altura"])):
            mas_bajo = indice
        
    print("\nAltura: {} \nIdentidad: {}\n".format(lista_personajes[mas_alto]["altura"],lista_personajes[mas_alto]["identidad"]))
    print("\nAltura: {} \nIdentidad: {}\n".format(lista_personajes[mas_bajo]["altura"],lista_personajes[mas_bajo]["identidad"])) 
    
    
            
def imprimir_superheroe_mas_y_menos_pesados():
    mas_pesado = 0
    menos_pesado = 0
    
    for indice in range(len(lista_personajes)):
        if(indice == 0 or float(lista_personajes[mas_pesado]["peso"]) > float(lista_personajes[indice]["peso"])):
            mas_pesado = indice
    
    for indice in range(len(lista_personajes)):
        if(indice == 0 or float(lista_personajes[menos_pesado]["peso"]) < float(lista_personajes[indice]["peso"])):
            menos_pesado = indice
            
    print("\nMenos pesado: {}\n".format(lista_personajes[mas_pesado]["peso"]))  
    print("\nMas pesado: {}\n".format(lista_personajes[menos_pesado]["peso"])) 

while True:
    
    print("1.Imprimir el nombre de los superheroes")
    print("2.Imprimir el nombre de los superheroes con su altura")
    print("3.Superheroe mas alto")
    print("4.Superheroe mas bajo")
    print("5.Identidad de cada superheroe")
    print("6.El mas y menos pesado")
    print("0.Salir.")
    
    opcion = input("ingrese una opcion: ")
    
    
    
    if opcion == "1":

        imprimir_nombre_superheroe()
        
    elif opcion == "2":
         
        imprimir_nombre_y_altura_superheroe()
        
    elif opcion == "3":
       
        imprimir_superheroe_mas_alto()
       
    elif opcion == "4":
        
        imprimir_superheroe_mas_bajo()
       
    elif opcion == "5":
        
        imprimir_identidad_superheroe()
        
    elif opcion == "6":
       
        imprimir_superheroe_mas_y_menos_pesados()
      
    elif opcion == "0":
        print("gracias por usar el programa...")
        break
    else:
        print("ingrese una opcion valida (1 al 7)!!")
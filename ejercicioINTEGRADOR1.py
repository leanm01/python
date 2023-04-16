lista_identificación = [1222, 2333]
lista_nombres = ["pepe","rogelio"]
lista_edades  = [25, 29]
lista_tipos_de_membresía = ["mensual","anual"]


while True:
    
    print("1.Agregar miembro")
    print("2.Mostrar miembros")
    print("3.Actualizar membresia")
    print("4.Buscar informacion de miembro")
    print("5.Calcular promedio de edad")
    print("6.Miembro mas joven y mas viejo")
    print("0.Salir.")
    
    opcion = input("ingrese una opcion: ")
    
    
    
    if opcion == "1":
        
        miembro_id = input("ingrese su id: ")
        miembro_id_entero = int(miembro_id)

        miembro_nombre = input("ingrese su nombre: ")

        miembro_edad = input("ingrese su edad: ")
        miembro_edad_entero = int(miembro_edad)

        miembro_membresia = input("ingrese el tipo de membresia (anual - mensual): ")


        lista_identificación.append(miembro_id_entero)
        lista_nombres.append(miembro_nombre)
        lista_edades.append(miembro_edad_entero)
        lista_tipos_de_membresía.append(miembro_membresia)
        
        print("El miembro ha sido agregado con éxito!!")
    
    elif opcion == "2":
        
        for indice in range(len(lista_identificación)):
            print("\nid: {}\nNombre: {}\nEdad: {}\nTipo de membresía: {}\n".format(lista_identificación[indice], lista_nombres[indice], lista_edades[indice], lista_tipos_de_membresía[indice]))
            
    elif opcion == "3":
        
        miembro_id = input("ingrese el id a actualizar: ")
        miembro_id_entero = int(miembro_id)
        
        nuevo_tipo_de_membresia = input("ingrese el nuevo tipo de membresia (anual - mensual): ")
        
        
        for indice in range(len(lista_identificación)):
            
            if lista_identificación[indice] == miembro_id_entero:
                lista_tipos_de_membresía[indice] = nuevo_tipo_de_membresia
            
        
    
    elif opcion == "4":
        
        miembro_id = input("ingrese el id a buscar: ")
        miembro_id_entero = int(miembro_id)
        
        flag = 0
        
        for indice in range(len(lista_identificación)):
            
            if lista_identificación[indice] == miembro_id_entero:
                flag = 1
                break

        
        if flag == 1:
            print("\nNombre: {}\nEdad: {}\nTipo de membresía: {}\n".format( lista_nombres[indice], lista_edades[indice], lista_tipos_de_membresía[indice]))
        
        else:
            print("El miembro no se encontró en la lista.")
        
        
    elif opcion == "5":
        
        if len(lista_edades) > 0:
            suma_edades = sum(lista_edades)
            promedio_edad = suma_edades / len(lista_edades)
        
        print("El promedio de edad de los miembros es:", promedio_edad)
        
    elif opcion == "6":
        if len(lista_edades) > 0:
            
            edad_mas_joven = lista_edades[0]
            edad_mas_vieja = lista_edades[0]
            
            nombre_mas_joven = lista_nombres[0]
            nombre_mas_vieja = lista_nombres[0]

            for i in range(len(lista_edades)):
                if lista_edades[i] < edad_mas_joven:
                    
                    edad_mas_joven = lista_edades[i]
                    nombre_mas_joven = lista_nombres[i]
                
                if lista_edades[i] > edad_mas_vieja:
                    
                    edad_mas_vieja = lista_edades[i]
                    nombre_mas_vieja = lista_nombres[i]

            print("El miembro más joven es {} y tiene {} años".format(nombre_mas_joven, edad_mas_joven))
            print("El miembro más viejo es {} y tiene {} años".format(nombre_mas_vieja, edad_mas_vieja))
    
    
    elif opcion == "0":
        print("gracias por usar el programa...")
        break
    else:
        print("ingrese una opcion valida (1 al 7)!!")
           
    
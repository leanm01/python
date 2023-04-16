lista_miembros = [{"id": 1000, "nombre": "pepe", "edad": 25, "membresia": "anual"},
                  {"id": 2000, "nombre": "jose", "edad": 52, "membresia": "mensual"}]



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


        nuevo_miembro = {"id":miembro_id_entero, "nombre":miembro_nombre, "edad": miembro_edad_entero, "membresia": miembro_membresia}
        
        lista_miembros.append(nuevo_miembro)
        
        print("se agrego un miembro!!")
        
      
    
    elif opcion == "2":
        
        for miembro in lista_miembros:
            print("\nid: {}\nNombre: {}\nEdad: {}\nTipo de membresía: {}\n".format(miembro["id"], miembro["nombre"], miembro["edad"], miembro["membresia"]))
            
    elif opcion == "3":
        
        miembro_id = input("ingrese el id a actualizar: ")
        miembro_id_entero = int(miembro_id)
        
        nuevo_tipo_de_membresia = input("ingrese el nuevo tipo de membresia (anual - mensual): ")
            
        for miembro in lista_miembros:
            
            if miembro['id'] == miembro_id_entero:
                
                miembro['membresia'] = nuevo_tipo_de_membresia
                
                print("\nid: {}\nNombre: {}\nEdad: {}\nTipo de membresía: {}\n".format(miembro["id"], miembro["nombre"], miembro["edad"], miembro["membresia"]))

                
    
    elif opcion == "4":
        
        miembro_id = input("ingrese el id a buscar: ")
        miembro_id_entero = int(miembro_id)
        
        
        for miembro in lista_miembros:
            
            if miembro["id"] == miembro_id_entero:
                print("\nNombre: {}\nEdad: {}\nTipo de membresía: {}\n".format( miembro["nombre"], miembro["edad"], miembro["membresia"]))
                break
            
            else:
                print("El miembro no se encontró en la lista.")
        
        
        
    elif opcion == "5":
        
       suma_edades = 0
       for miembro in lista_miembros:
           
           suma_edades += miembro["edad"]
           
       promedio_edad = suma_edades / len(lista_miembros)
    
       print("El promedio de edad de los miembros es:", promedio_edad)
        
    elif opcion == "6":
       
        miembro_mas_joven = lista_miembros[0]
        
        for miembro in lista_miembros:
            if miembro["edad"] < miembro_mas_joven["edad"]:
                miembro_mas_joven = miembro
        
        print(f"El miembro más joven es {miembro_mas_joven['nombre']} con {miembro_mas_joven['edad']} años.")


        miembro_mas_viejo = lista_miembros[0]
        
        for miembro in lista_miembros:
            if miembro["edad"] > miembro_mas_viejo["edad"]:
                miembro_mas_viejo = miembro
        
        print(f"El miembro más viejo es {miembro_mas_viejo['nombre']} con {miembro_mas_viejo['edad']} años.")

    
    elif opcion == "0":
        print("gracias por usar el programa...")
        break
    else:
        print("ingrese una opcion valida (1 al 7)!!")
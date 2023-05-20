'''
#ascendente
lista_numeros = [3,5,4,9,6,7,1,2,8]
lista_ordenada_ascendente = sorted(lista_numeros) # esto devuelve la lista ordenada, no la modifica
print(lista_ordenada_ascendente)
lista_numeros.sort()# esto la modifica
print(lista_numeros)

#descendente
lista_numeros_dos = [3,5,4,9,6,7,1,2,8]
lista_ordenada_descendente = sorted(lista_numeros_dos, reverse = True)#reverse hace que sea descendente
print(lista_ordenada_descendente)
lista_numeros_dos.sort(reverse=True)
print(lista_numeros_dos)

#orden de cadenas
lista_cadenas = ['abeja','hola','buenas','efecto','todos','cejas']
lista_ordenada = sorted(lista_cadenas)
print(lista_ordenada)
lista_cadenas.sort()
print(lista_cadenas)

'''
lista = [1,5,4,7,8,9,3,6,2]

def burbujeo_ordenamiento(lista:list):
    n = len(lista)
    for indice in range(n):
        #print(indice)
        for elemento in range(0,n-indice-1):
            print(elemento)
            if lista[elemento] > lista[elemento+1]:
                lista[elemento],lista[elemento+1] = lista[elemento+1],lista[elemento]
    return lista
                
print(burbujeo_ordenamiento(lista))
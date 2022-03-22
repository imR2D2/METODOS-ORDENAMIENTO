import random
import time
#--------SELECCION------------
'''100 valores entre 1 y 200'''
inicio1 = time.time()
lista = [random.randint(1, 500) for n in range(5000)]
longuitud = len(lista)
'''El menos 1 es porque no tenemos que llegar hasta el ultimo numero del arreglo por ende el bucle
 nada mas se ejecutara en desde la primer posicion hasta la penultima'''
for i in range(longuitud -1):
    '''Guardara el elemento con el cual estamos comparando los demas'''
    menor = i
    '''Aqui lo que sucede es que se pone un mas 1 porque ya tenemos guardado el primer valor a comparar
    en MENOR entonces comienza a buscar en los demas numeros de la lista'''
    for j in range (i+1, longuitud):
        if lista[j] < lista[menor]:
            menor = j
    #Vamos a almacenar el valor que es menor al primero aqui
    temporal = lista[menor]
    #Cambiamos valor primero a la posicion del valor menor
    lista[menor] = lista[i]
    #Agarramos la posicion primera que quedo sola y metemos el valor menor guardado en temporal
    lista[i] = temporal
fin1 = time.time()


#-------------BURBUJA---------------------
inicio2 = time.time()
lista2 = [random.randint(1, 500) for n in range(5000)]
'''El bucle determinara las vueltas que tenemos que dar a la lista'''
for a in range(len(lista2) -1):
    '''Este bucle sera para ir comparando cada elemento con el siguiente de la lista'''
    for b in range(len(lista2) -1):
        if lista2[b] > lista2[b+1]:
            '''Intercambiaremos los valores'''
            #Usamos la asignacion multiple de Python
            lista2[b], lista2[b+1] = lista2[b+1], lista2[b]
fin2 = time.time()

#------------INSERCION--------------------
inicio3 = time.time()
lista3 = [random.randint(1, 500) for n in range(5000)]
'''La coma indica _desde_ posicion 1 _hasta_ len(lista)'''
for i in range(1, len(lista3)):
    '''Numero despues del primero ehhh'''
    actual = lista3[i]
    indice = i

    while indice > 0 and lista3[indice -1] >actual:
        lista3[indice] = lista3[indice -1]
        indice = indice - 1

    lista3[indice] = actual
fin3 = time.time()


#-------------QUICK SORT--------------------------
inicio4 = time.time()
lista4 = [random.randint(1, 500) for n in range(100000)]
def particionado(lista4):
    '''Seleccionamos el primer elemento de la lista'''
    pivote = lista4[0]
    menores = []
    mayores = []
    '''Ahora haremos lo que sigue con los numeros sucesores de la posicion 0'''
    '''La posicion 0 ya no hay que recorrecla porque es el povote entonces empezamos desde la posicion 1'''
    for i in range(1, len(lista4)):
        if lista4[i] < pivote:
            menores.append(lista4[i])
        else:
            mayores.append(lista4[i])

    return menores, pivote, mayores

def quicksort(lista4):
    if len(lista4) < 2:
        return lista4

    menores, pivote, mayores = particionado(lista4)
    '''los mandamos a llamar de forma recursiva'''
    return quicksort(menores) + [pivote] + quicksort(mayores)
fin4 = time.time()


#---------------SHELL SORT------------------------
inicio5 = time.time()
def shell(lista5):
    mitad = len(lista5)//2

    while mitad > 0:
        for p in range(mitad):
            reducir_busqueda(lista5, p, mitad)
        mitad = mitad//2

def reducir_busqueda(lista5, incio, salto):
    for q in range(incio + salto, len(lista5), salto):
        valor = lista5[q]
        posicion = q

        while posicion >= salto and lista5[posicion - salto] > valor:
            lista5[posicion] = lista5[posicion-salto]
            posicion = posicion-salto
        lista5[posicion] = valor
numeros = [random.randint(1, 500) for n in range(100000)]

fin5 = time.time()

#------------MERGE SORT-------------------------------
inicio6 = time.time()
def merge_sort(lista6):
    if len(lista6) > 1:
        mitad = len(lista6)//2
        primera_mitad = lista6[:mitad]
        segunda_mitad = lista6[mitad:]
        '''Haremos una invocacion recursiva a merge sort'''
        merge_sort(primera_mitad)
        merge_sort(segunda_mitad)
        '''Creamos 3 variables auxiliares'''
        x = 0
        y = 0
        z = 0

        while x < len(primera_mitad) and y < len(segunda_mitad):
            if primera_mitad[x] < segunda_mitad[y]:
                lista6[z] = primera_mitad[x]
                x+=1
            else:
                lista6[z] = segunda_mitad[y]
                y+=1
            z+=1

        while x <len(primera_mitad):
            lista6[z] = primera_mitad[x]
            x+=1
            z+=1

        while y < len(segunda_mitad):
            lista6[z] = segunda_mitad[y]
            y += 1
            z += 1
numeros2 = [random.randint(1, 500) for n in range(100000)]
fin6 = time.time()

#-------------------MENU--------------------------
while (True):
    print("\n" +
          "\t\t---METODOS DE ORDENAMIENTO---\n" +
          "\n" +
          "\t\t\t1. Seleccion\n" +
          "\t\t\t2. Burbuja\n" +
          "\t\t\t3. Insercion\n"+
          "\t\t\t4. Quick Sort\n" +
          "\t\t\t5. Shell Sort\n" +
          "\t\t\t6. Merge Sort\n" +
          "\t\t\t7. SALIR\n")
    num = input("\t\tIngresa la opcion:\n ")

    if num == "1":
        while (True):
            print("\n" +
                  "\t\t\t---SELECCIONA ALGO DE SELECCION---\n" +
                  "\n" +
                  "\t\t\t1. Datos dentro del arreglo aleatorio:\n" +
                  "\t\t\t2. Ordenamiento de arreglo:\n" +
                  "\t\t\t3. REGRESAR AL MENU PRINCIPAL\n")
            num = input("\t\tIngresa la opcion:\n ")

            if num == "1":
                print(longuitud)
            elif num == "2":
                print(lista)
                print("")
                print("Se tardo en ordenar el arreglo", (fin1 - inicio1) * 1000, "milisegundos")
            elif num == "3":
                break
            else:
                print("\t\tIngresa una opcion correcta porfavor...\n")
                print("")

    elif num == "2":
        while (True):
            print("\n" +
                  "\t\t\t---SELECCIONA ALGO DE BURBUJA---\n" +
                  "\n" +
                  "\t\t\t1. Datos dentro del arreglo aleatorio:\n" +
                  "\t\t\t2. Ordenamiento de arreglo:\n" +
                  "\t\t\t3. REGRESAR AL MENU PRINCIPAL\n")
            num = input("\t\tIngresa la opcion:\n ")

            if num == "1":
                print(len(lista2))
            elif num == "2":
                print(lista2)
                print("")
                print("Se tardo en ordenar el arreglo", (fin2 - inicio2) * 1000, "milisegundos")
            elif num == "3":
                break
            else:
                print("\t\tIngresa una opcion correcta porfavor...\n")
                print("")

    elif num == "3":
        while (True):
            print("\n" +
                  "\t\t\t---SELECCIONA ALGO DE INSERCION---\n" +
                  "\n" +
                  "\t\t\t1. Datos dentro del arreglo aleatorio:\n" +
                  "\t\t\t2. Ordenamiento de arreglo:\n" +
                  "\t\t\t3. REGRESAR AL MENU PRINCIPAL\n")
            num = input("\t\tIngresa la opcion:\n ")

            if num == "1":
                print(len(lista3))
            elif num == "2":
                print(lista3)
                print("")
                print("Se tardo en ordenar el arreglo", (fin3 - inicio3) * 1000, "milisegundos")
            elif num == "3":
                break
            else:
                print("\t\tIngresa una opcion correcta porfavor...\n")
                print("")

    elif num == "4":
        while (True):
            print("\n" +
                  "\t\t\t---SELECCIONA ALGO DE QUICK SORT---\n" +
                  "\n" +
                  "\t\t\t1. Datos dentro del arreglo aleatorio:\n" +
                  "\t\t\t2. Ordenamiento de arreglo:\n" +
                  "\t\t\t3. REGRESAR AL MENU PRINCIPAL\n")
            num = input("\t\tIngresa la opcion:\n ")

            if num == "1":
                print(lista4)
            elif num == "2":
                print(quicksort(lista4))
                print("")
                print("Se tardo en ordenar el arreglo", (fin4 - inicio4) * 1000, "milisegundos")
            elif num == "3":
                break
            else:
                print("\t\tIngresa una opcion correcta porfavor...\n")
                print("")
    elif num == "5":
        while (True):
            print("\n" +
                  "\t\t\t---SELECCIONA ALGO DE SHELL SORT---\n" +
                  "\n" +
                  "\t\t\t1. Datos dentro del arreglo aleatorio:\n" +
                  "\t\t\t2. Ordenamiento de arreglo:\n" +
                  "\t\t\t3. REGRESAR AL MENU PRINCIPAL\n")
            num = input("\t\tIngresa la opcion:\n ")

            if num == "1":
                print(numeros)
                shell(numeros)
            elif num == "2":
                shell(numeros)
                print(numeros)
                print("")
                print("Se tardo en ordenar el arreglo", (fin5 - inicio5) * 1000, "milisegundos")
            elif num == "3":
                break
            else:
                print("\t\tIngresa una opcion correcta porfavor...\n")
                print("")
    elif num == "6":
        while (True):
            print("\n" +
                  "\t\t\t---SELECCIONA ALGO DE MERGE SORT---\n" +
                  "\n" +
                  "\t\t\t1. Datos dentro del arreglo aleatorio:\n" +
                  "\t\t\t2. Ordenamiento de arreglo:\n" +
                  "\t\t\t3. REGRESAR AL MENU PRINCIPAL\n")
            num = input("\t\tIngresa la opcion:\n ")

            if num == "1":
                print(numeros2)
            elif num == "2":
                merge_sort(numeros2)
                print(numeros2)
                print("")
                print("Se tardo en ordenar el arreglo", (fin6 - inicio6) * 1000, "milisegundos")
            elif num == "3":
                break
            else:
                print("\t\tIngresa una opcion correcta porfavor...\n")
                print("")

    elif num == "7":
        exit()
    else:
        print("\t\tIngresa una opcion correcta porfavor...\n")
        print("")

import random

def numeros_aleatorios():
    lista_numeros = []

    for i in range (100):
        numero_aleatorio = random.randint(1,100)
        lista_numeros.append(numero_aleatorio)
    print(lista_numeros)


def matriz_aleatoria():
    
    matriz = [[0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0]]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]=random.choice("az")
    
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")

def ordenar_lista_ASC(lista_numeros):

    
    n = len(lista_numeros)
    for i in range(n):
        ordenamiento = False
        for j in range(0, n-i-1):
            if lista_numeros[j] > lista_numeros[j+1]:
                lista_numeros[j], lista_numeros[j+1] = lista_numeros[j+1], lista_numeros[j]
                ordenamiento = True
        if not ordenamiento: break


def ordenar_lista_DESC(lista_numeros):


    n = len(lista_numeros)
    for i in range(n):
        ordenamiento = False
        for j in range(0, n-i-1):
            if lista_numeros[j] < lista_numeros[j+1]:
                lista_numeros[j], lista_numeros[j+1] = lista_numeros[j+1], lista_numeros[j]
                ordenamiento = True
        if not ordenamiento: break


def cadena_caracteres():

    cadena = input("Ingrese una palabra con solo caracteres alfabeticos")

    while not cadena.isalpha():
        cadena = input("Ingrese una palabra CON SOLO caracteres alfabeticos")

def registro_numeros(lista_numeros):
    cantidad_de_ceros = 0
    cantidad_de_unos = 0
    cantidad_de_dos = 0
    cantidad_de_tres = 0
    cantidad_de_cuatros = 0
    cantidad_de_cincos = 0
    cantidad_de_seis = 0
    cantidad_de_siete = 0
    cantidad_de_ocho = 0
    cantidad_de_nueve = 0
    for i in range(lista_numeros):
        if i == 0:
            cantidad_de_ceros += 1
        elif i == 1:
            cantidad_de_unos +=1
        elif i == 2:
            cantidad_de_dos +=1
        elif i == 3:
            cantidad_de_tres +=1
        elif i == 4:
            cantidad_de_cuatros +=1
        elif i == 5:
            cantidad_de_cincos +=1
        elif i == 6:
            cantidad_de_seis +=1
        elif i == 7:
            cantidad_de_siete +=1
        elif i == 8:
            cantidad_de_ocho +=1
        elif i == 9:
            cantidad_de_nueve +=1
    print(f'''
    Se ingresaron {cantidad_de_ceros} CEROS
    Se ingresaron {cantidad_de_unos} UNOS
    Se ingresaron {cantidad_de_dos} DOS
    Se ingresaron {cantidad_de_tres} TRES
    Se ingresaron {cantidad_de_cuatros} CUATROS
    Se ingresaron {cantidad_de_cincos} CINCOS
    Se ingresaron {cantidad_de_seis} SEIS
    Se ingresaron {cantidad_de_siete} SIETES
    Se ingresaron {cantidad_de_ocho} OCHOS
    Se ingresaron {cantidad_de_nueve} NUEVES   
    ''')
    "Perdon que no respete el formato solicitado, otra vez, por falta de tiempo hago esto"

def maximo_num(lista_numeros):
    registro_numeros()

    numero_maximo = cantidad_de_ceros

    if cantidad_de_unos > numero_maximo:
        numero_maximo = cantidad_de_unos
    elif cantidad_de_dos > numero_maximo:
         numero_maximo = cantidad_de_unos
    elif cantidad_de_tres > numero_maximo:
         numero_maximo = cantidad_de_tres
    elif cantidad_de_cuatros > numero_maximo:
         numero_maximo = cantidad_de_cuatros
    elif cantidad_de_cincos > numero_maximo:
         numero_maximo = cantidad_de_cincos
    elif cantidad_de_seis > numero_maximo:
         numero_maximo = cantidad_de_seis
    elif cantidad_de_siete > numero_maximo:
         numero_maximo = cantidad_de_siete
    elif cantidad_de_ocho > numero_maximo:
         numero_maximo = cantidad_de_ocho
    elif cantidad_de_ocho > numero_maximo:
         numero_maximo = cantidad_de_nueve
        
    print (f"el número que mas salió, lo hizo {numero_maximo} veces")


def minimo_num(lista_numeros):
    registro_numeros()

    numero_minimo = cantidad_de_ceros

    if cantidad_de_unos < numero_minimo:
        numero_minimo = cantidad_de_unos
    elif cantidad_de_dos < numero_minimo:
         numero_minimo = cantidad_de_unos
    elif cantidad_de_tres < numero_minimo:
         numero_minimo = cantidad_de_tres
    elif cantidad_de_cuatros < numero_minimo:
         numero_minimo = cantidad_de_cuatros
    elif cantidad_de_cincos < numero_minimo:
         numero_minimo = cantidad_de_cincos
    elif cantidad_de_seis < numero_minimo:
         numero_minimo = cantidad_de_seis
    elif cantidad_de_siete < numero_minimo:
         numero_minimo = cantidad_de_siete
    elif cantidad_de_ocho < numero_minimo:
         numero_minimo = cantidad_de_ocho
    elif cantidad_de_ocho < numero_minimo:
         numero_minimo = cantidad_de_nueve
        
    print (f"el número que menos salió, lo hizo {numero_minimo} veces")
            

     
        
        

def menu():
    "PERDON POR ESTO, CREÍ QUE PODÍA TOMARLO ESCRIBIENDO ''' PERO LO COMENTÓ Y ME DI CUENTA TARDE, CUANDO YA NO TENÍA TIEMPO"
    opcion_elegida = input("Hola, bienvenido al menu de opciones!:\n ingrese la opcion deseada\n 1 – Generar la lista aleatoria de números enteros utilizando la función desarrollada.\n 2 – Ordenar la lista de números generada anteriormente, utilizando la función desarrollada.\n  3 – Buscar e informar cuantas veces se repite cada uno de los números del 0 al 9. El informe deberá realizarse con un registro debajo del otro y el mismo tendrá el siguiente encabezado: NÚMERO | CANTIDAD\n 4 – Del ítem anterior, obtener: \nEl número que más veces se repite e informar la cantidad. \nl número que menos veces se repite e informar la cantidad \n5 – Generar la matriz aleatoria de caracteres alfabéticos (letras minúsculas), utilizando la función desarrollada.\n6 – Se debe ingresar una palabra por consola, validando que la misma sea una cadena de caracteres alfabética. Luego buscar en la matriz si existen las letras necesarias para poder armar la palabra ingresada.\n Por último informar: \nEn caso negativo informar por pantalla: “La palabra <palabra> no se puede armar en la matriz.\n En caso positivo, informar por pantalla: “La palabra <palabra> se puede armar en la matriz.\n 7 – Salir.")


    if opcion_elegida == 1:
        numeros_aleatorios()
    elif opcion_elegida == 2:
            consulta = input("Para orden ASC presione A, para orden DESC presione B")
            while consulta != "A" and consulta != "B":
                consulta = input("Para orden ASC presione A, para orden DESC presione B")
            if consulta == "A":
                ordenar_lista_ASC(lista_numeros)
            elif consulta == "B":
                ordenar_lista_DESC(lista_numeros)
    elif opcion_elegida == 3:
        registro_numeros(lista_numeros)
    elif opcion_elegida == 5:
        matriz_aleatoria()
    elif opcion_elegida ==6:
        cadena_caracteres()
    elif opcion_elegida == 7:
        print ("Adiós")
        
menu()

    




#Crear una variable que contenga un  diccionario vacío y
# llenar el diccionario pidiendo al usuario ingresar clave y valor por pantalla, luego presentar el diccionario

def ejercicio1():
    diccionario = {}

    total_cv = int(input("Ingrese el total de claves y valor que desea agregar: "))
    for x in range(1,total_cv,+1):
        clave1 = input("ingrese la clave: ")
        valor1 = input("Ingrese el valor: ")
    diccionario[clave1] = valor1

    print(f"diccionario actualizado: {diccionario}")

#ejercicio1()

def ejercicio2():
    datos_usuario = {}

    # Solicitar al usuario ingresar los datos y almacenarlos en el diccionario
    for campo in ['cedula', 'nombre', 'edad', 'direccion', 'telefono']:
        datos_usuario[campo] = input(f"Ingrese su {campo}: ")

    # Mostrar los datos almacenados en el diccionario
    print("\nDatos del usuario:")
    #for clave, valor in datos_usuario.items():
        #print(clave.capitalize() + ":", valor) #para que se vea saltado todos los valores
    print(f"{datos_usuario}")
#ejercicio2()

def ejercicio3():
    diccionarioProducto = {"tomates":5,"zanahorias":20}

    while True:
        opcion = input("¿Desea agregar, eliminar o buscar elementos?: ")
        if opcion.lower() == "agregar":
            nuevoProducto = input("Ingrese un nuevo producto: ").lower()
            cantidad_producto = int(input(f"Ingrese la cantidad de {nuevoProducto} que desee: "))
            diccionarioProducto[nuevoProducto] = cantidad_producto
            print(f"Inventario actualizado!: {diccionarioProducto}")
        elif opcion.lower() == "eliminar":
            productoEliminar = input("Ingrese el producto a eliminar: ").lower()
            if productoEliminar in diccionarioProducto.keys():
                del diccionarioProducto[productoEliminar]
                print(f"El producto {productoEliminar} ha sido eliminado del inventario")
                print(f"Inventario actualizado!: {diccionarioProducto}")
            else:
                print(f"El producto {productoEliminar} no se pudo eliminar porque no está en el inventario")
        elif opcion.lower() == "buscar":
            productoBuscar = input("Ingrese el producto a buscar: ").lower()
            if productoBuscar in diccionarioProducto.keys():
                print(f"El producto {productoBuscar} se ha encontrado y su cantidad es {diccionarioProducto[productoBuscar]} unidades")
            else:
                print(f"El producto {productoBuscar} no se encontró en el inventario")
        else:
            print("opcion fuera de rango")

        alternativa = input("¿Desea volver a realizar algún proceso?: ")
        if alternativa.lower() == "no":
            print("Gracias por usar este servicio")
            break

# ejercicio3()


def ejercicio4():
    cantidadGastos = int(input("Ingrese la cantidad de gastos que tuvo durante la semana: "))
    listaGastos = []
    for x in range(1,cantidadGastos +1):
        gasto = float(input(f"{x}. Ingrese el gasto: "))
        listaGastos.append(gasto)

    print(f"La lista de los gastos es {listaGastos}")

    sumaGastos = 0
    for y in listaGastos:
        sumaGastos += y
    print(f"El gasto de la semana asciende a {sumaGastos} dolares")
#ejercicio4()


def ejercicio5():
    listaReservas = ["Canadá","Japón","Corea del Sur","El Salvador"]
    while True:
        consulta = input("Ingrese que vuelo desea: ")
        if consulta in listaReservas:
            print(f"El vuelo a {consulta} se encuentra disponible, en breve se lo reservaremos")
        else:
            print(f"El vuelo a {consulta} no se encuentra disponible")

        alternativa = input("¿Desea hacer otra consulta?: ").lower()
        if alternativa == "no":
            print("Muchas gracias por usar nuestro servicio")
# ejercicio5()

def ejercicio6():
    # Crear un diccionario para almacenar los datos del usuario
    usuario = {}
    for campo in ['cedula','nombre','edad','direccion','telefono']:
     usuario[campo] = input(f"Ingrese su {campo}:")
     # Mostrar los datos almacenados en el diccionario
     print("\nDatos del usuario:")
     for clave, valor in usuario.items():
         print(clave + ":", valor)
#ejercicio6()

# Solicitar los datos al usuario
# usuario['cedula'] = input("Ingrese su cédula: ")
# usuario['nombre'] = input("Ingrese su nombre: ")
# usuario['edad'] = input("Ingrese su edad: ")
# usuario['direccion'] = input("Ingrese su dirección: ")
# usuario['telefono'] = input("Ingrese su teléfono: ")

def ejercicio7():
    hola = str(input("escriba esto: "))
    print("hola")
#ejercicio7()

def ejercicio8():
    frase = input("ingrese una frase")
    vocales = ""  # cadena vacia para poder almacenar las vocales
    vocales_list = ['a', 'e', 'i', 'o', 'u']
    for caracter in frase:  # contar los caracteres de la frase
        if caracter in vocales_list:  # contar las voacles
            vocales += caracter  # agrega a la cadena de vocales
    print("Las vocales en la frase son:", vocales)
#ejercicio8()

def ejercicio9():
    frase2 = input("ingrese una frase")
    contador_vocales = 0  # para almacenar el numero de vocales
    vocales_list2 = ['a', 'e', 'i', 'o', 'u']
    for caracter in frase2:  # contar los caracteres de la frase
        if caracter in vocales_list2:  # contar las voacles
            contador_vocales += 1  # cuenta en la cadena las vocales
    print("El numer0 de vocales en la frase son en la frase son:", contador_vocales)
#ejercicio9()

def ejercicio10():
    precio_productos = {"tomate": 1, "pimiento": 1.5, "zanahoria": 2, "arroz": 2.5}
    producto2 = input("Ingrese el nombre del producto: ").lower()
    kilos = float(input("Ingrese la cantidad en kilos: "))
    if producto2 in precio_productos:
        precio_unitario = precio_productos[producto2]
        precio_total = precio_unitario * kilos
        print(f"El precio de {kilos} kilos de {producto2} es: {precio_total}")
    else:
        print("Lo siento el producto no es disponible en el mercado")
#ejercicio10()

def ejercicio11():
    numeros = []  # lista para almacenar los numeros
    while True:
        numero = int(input("Ingrese una serie de numeros: "))
        numeros.append(numero)  # agragamos los numeros a la lista
        if numero == 0:
            break  # si se ingresa 0 se rompe el blucle e imprime un mensaje
    print("Se ha roto la caneda al escribir 0")
#ejercicio11

def ejercicio12():
    while True:
        numero2 = float(input("Ingrese un numero: "))
        if numero2 >= 0:
            print("el numero ingresado es", numero2)
            break
        else:
            print("El numero ingresado es negativo, intente nuevamente:")
#ejercicio12()

def ejercicio13():
    numeros3 = []  # lista para almacenar los numeros
    while True:
        numeros_ingresados = input("Ingrese una serie de numeros: ")
        numeros3.append(numeros_ingresados)  # agragamos los numeros a la lista
        for numero in numeros3:
            numeros3 += numeros_ingresados
            if numeros3 == 0:
                break
    print("la suma es:", suma)
#ejercicio13()

#una lista que almacene numeros y cuando se escriba 0 se rompa el blucle y sume la lista de numeros
def ejercicio14():
    lista = []
    while True:
        numero = int(input("Ingrese una serie de numeros: "))
        lista.append(numero)
        if numero == 0:
            break
    print("Se ha roto la cadena al escribir 0")
    suma = 0
    for numero in lista:
        suma += numero
    print("La suma de los numeros es:", suma)
#ejercicio14()

#Solicitar al usuario que ingrese una lista de numeros positivos y por cada uno imprimir la suma de los digitos y el total de pares que los componen, la condicion de corte
# es que se ingrese el numero -1.
def ejercicio15():
    lista = []
    while True:
        numero = int(input("Ingrese una serie de numeros: "))
        lista.append(numero)
        if numero == -1:
            break
    print("Se ha roto la cadena al escribir -1")
    suma = 1
    for numero in lista:
        suma += numero
    print("La suma de los numeros es:", suma)
    #de la lista creada imprimir cuantos numeros pares hay
    pares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
    print("La cantidad de numeros pares es:", pares)
#ejercicio15()

#Mostrar un menu con tres opciones: 1 "comenzar programa", 2 "Imprimir listado", "finalizar programa"
#si se escribe un numero erroneo se informa el mensaje, El menu se debe mostrar luego de ejcutada cada opcion, permitiendo volver a elegir
#Si se le elige las opciones 1 y 2 se imprimira un texto, si se elige la opcion 3 se interrumpira la impresion del menu y finaliza el programa

def ejercicio16():
    while True:
        print("1. comenzar programa")
        print("2. Imprimir listado")
        print("3. finalizar programa")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            print("Haz elegido la opcion 1".upper())
        elif opcion == 2:
            print("Haz eleigido la opcion 2".upper())
        elif opcion == 3:
            print("Haz elegido la opcion 3".upper()) #el .upper() es para que se imprima en mayuscula
            break
        else:
            print("Opcion incorrecta")
#ejercicio16()

#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
def ejercicio17():
    diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisa = input("Ingrese una divisa: ")
    if divisa in diccionario:
        print(f"El simbolo de la divisa {divisa} es {diccionario[divisa]}")
    else:
        print("La divisa no se encuentra en el diccionario")
#ejercicio17()

#Leer un numero entero positivo desde teclado e imprimir la suma de los digitos que lo componen
def ejercicio18():
    numero = int(input("Ingrese un numero entero positivo: "))
    suma = 0
    while numero != 0:
        suma += numero % 10
        numero //= 10 #el // es para que el resultado de la division sea enteros
    print("La suma de los digitos es:", suma)
#ejercicio18()

#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
#Fruta	Precio
#Plátano	1.35
#Manzana	0.80
#Pera	0.85
#Naranja	0.70

def ejercicio19():
    diccionario = {"Platano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
    fruta = input("Ingrese una fruta: ").capitalize() # el .capitalize() es para que la primera letra de la palabra se imprima en mayuscula
    if fruta in diccionario:
        kilos = float(input("Ingrese la cantidad de kilos:"))
        precio = diccionario[fruta] * kilos
        print(f"El precio de {kilos} kilos de {fruta} fruta es: {precio}")
    else:
        print("La fruta no se encuentra en el diccionario")
#ejercicio19()

#Escribir un programa que permita al usuario ingresar 6 numeros enteros que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los numeros negativos y el promedio de los positivos.
#No te olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se ingresaron numeros positivos.
def ejercicio20():
    lista = []
    for x in range(1,7):
        numero = int(input("Ingrese un numero: "))
        lista.append(numero)
    print(f"La lista de numeros es: {lista}")

    suma_negativos = 0
    for numero in lista:
        if numero < 0:
            suma_negativos += numero
    print(f"La suma de los numeros negativos es: {suma_negativos}")

    suma_positivos = 0
    for numero in lista:
        if numero > 0:
            suma_positivos += numero
    print(f"La suma de los numeros positivos es: {suma_positivos}")

    promedio_positivos = suma_positivos / 6
    print(f"El promedio de los numeros positivos es: {promedio_positivos}")
#el mensaje de error al dividir por 0
    if suma_positivos == 0:
        print("No se puede dividir por 0")

#ejercicio20()

#Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada. En cada iteracion, solicitar al usuario que ingrese un numero. Al finalizar, mostrar la sumatoria de todos los numeros ingresados.
def ejercicio21():
    cantidad = int(input("Ingrese una cantidad: "))
    suma = 0
    for x in range(1,cantidad + 1): #que hace el (1,cantidad, +1)?
        numero = int(input("Ingrese un numero: "))
        suma += numero
    print(f"La suma de los numeros es: {suma}")
#mensaje de error si ponen numeros negativos
    if cantidad < 0:
        print("No se puede ingresar numeros negativos")
#ejercicio21()

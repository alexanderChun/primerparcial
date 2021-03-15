def ejercicio1():
    estud=[]
    for x in range(10):
        nombre=input("Ingrese el nombre del Alumno:")
        carnet=int(input("Ingrese su No. de Carné sin guiones:"))
        estud.append((nombre,carnet))
    print(estud)
#ejercicio1()

#alumnos()
#ejercicio1()

def ejercicio2():
    marcas=[]
    codigos=[]
    for x in range(10):
        nom=input("Ingrese la marca del producto:")
        marcas.append(nom)
        no1=input("Ingrese Nombre del producto:")
        no2=input("Ingrese codigo de un producto:")
        codigos.append([no1,no2])
    for x in range(10):
        print(marcas[x],codigos[x][0],codigos[x][1])
#ejercicio2()

def ejercicio3():
    paises={}
    for x in range(10):
        pais=input("Ingrese el nombre de un pais:")
        capital=input("Ingrese la capital:")
        paises[pais] = capital
    return paises

def ejercicio4(paises):
    print("Listado del diccionario completo")
    for pais in paises:
        print(pais, paises[pais])
#paises=ejercicio3()
#ejercicio4(paises)

def ejercicio5():
    ganados=[]
    for x in range(8):
        curso = input("Ingrese el nombre del curso: ")
        c1 = int(input("Ingrese nota: "))
        if c1 >50:
            if c1 >61:
                ganados.append((curso,c1))
        else:
            print("error: La nota ingresada debe ser mayor a 50")
            c1 = int(input("Ingrese nota: "))
    print("Los curso ganados son: ")
    print(ganados)
#ejercicio5()

def ejercicio6():
    novato=[]
    experto=[]
    super_experto=[]
    for x in range(8):
        jugador = input('ingrese el nombre del jugador: ')
        edad = int(input('ingrese la edad del jugador: '))
        if edad < 14:
            print("EDAD NO VALIDA: La edad debe ser de 14 en adelante")
            edad = int(input('ingrese la edad del jugador: '))
        elif edad >= 14 and edad <= 16:
            novato.append((jugador,edad))
        elif edad > 16 and edad <= 20:
            experto.append((jugador,edad))
        elif edad > 20:
            super_experto.append((jugador,edad))
    print("1. novato")
    print("2.Experto")
    print("3.Super Experto")
    elige=int(input('Elige la categoría que quiere seleccionar: '))
    if elige==1:
        print(novato)
    elif elige==2:
        print(experto)
    elif elige==3:
        print(super_experto)
#ejercicio6()


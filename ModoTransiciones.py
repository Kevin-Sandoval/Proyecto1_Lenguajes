

def modo2():
    lista_Alfabeto = []
    lista_Estados_De = []
    lista_Temporal = []
    lista_Transiciones = []

    print("\n\n-- NOTA --: La forma de ingresar: \n          Alfabeto: [simbolo1, simbolo2...]\n          Estados: [estado1, estado2...]\n          Transiciones: [estadoDe,estadoHacia;...]")
    print()
    cadena1= input("Ingrese el alfabeto: ")
    cadena2= input("Ingrese los estados: ")
    cadena3= input("Ingrese las transiciones")
    
    #cadena1 = "[a,b]"
    #cadena2 = "[A,B,C,D]"
    #cadena3 = "[A,C;A,C;B,D;-,-]"
    

    #ELIMINANDO CORCHETES
    cadena1 = cadena1.strip("[]")
    cadena2 = cadena2.strip("[]")
    cadena3 = cadena3.strip("[]")

    #SEPARANDO CADENA1 Y ALMACENANDO EN LISTA_ALFABETO
    lista_Alfabeto = cadena1.split(",")
    #SEPARANDO CADENA2 Y ALMACENANDO EN LISTA_ESTADOS_DE
    lista_Estados_De = cadena2.split(",")
    #SEPARANDO CADENA3 Y ALMACENANDO EN LISTA_TEMPORAL
    lista_Temporal = cadena3.split(";")

    contador = 0
    for estado_De in lista_Estados_De:
        estadoTemporal = Estado()
        estadoTemporal.agregarNombre(estado_De)
        for indice in range(0,len(lista_Alfabeto)):
            aux = lista_Temporal[contador].split(",")
            estadoTemporal.definirTransicion(aux[indice],lista_Alfabeto[indice])

        contador+=1
        lista_Transiciones.append(estadoTemporal)
        

    for x in lista_Transiciones:
        print(x.nombre)
        for i in x.transiciones:
            print(i)

    print(lista_Alfabeto)
    print(lista_Estados_De)
    print(lista_Temporal)

modo2()
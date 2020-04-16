import os
from Objeto import Estado
from Objeto import Transicion
from Objeto import Automata
from Principal import buscarEstado
from Principal import mostrarLista
from Principal import listaAutomatas
from Principal import verificar_Lista_Vacia

posiblesEstados=["A","B","C","D","E","F","G","H","I","J","K","L","M",
"N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def leerArchivoAFDa():
    lista_Estados = []
    lista_Alfabeto = []
    estado_Inicial = ""
    lista_EstadosAceptacion = []
    lista_Transiciones=[]

    ruta = input("Ingrese la ruta del archivo AFD: ") 
    archivo1 = open(ruta,"r")
    archivo1_Lineas = archivo1.readlines()
    AFD_Lineas=[]
    

    #QUITANDO EL SALTO DE LINEA
    for linea in archivo1_Lineas:
        AFD_Lineas.append(linea.strip())

    print(AFD_Lineas)
    print()
    #RECORRIENDO EL ARCHIVO DE LINEAS
    for x in AFD_Lineas:
        existe = False
        cadena1=x.split(";")
        cadena2=cadena1[0].split(",") # [ 'A', 'A', '1']
        cadena3=cadena1[1].split(",") # [ 'true', 'true']

        #GUARDANDO ESTADOS 
        if (cadena2[0] or cadena2[1]) in lista_Estados: #SI YA ESTAN EN LOS ESTADOS
            pass        
        elif (cadena2[0] in posiblesEstados):
            lista_Estados.append(cadena2[0])
        elif (cadena2[1] in posiblesEstados):
            lista_Estados.append(cadena2[1])
        else:
            print("NO hay estados")

        #GUARDANDO ALFABETO
        if cadena2[2] in lista_Alfabeto:
            pass
        elif cadena2[2] in lista_Estados:
            print("El simbolo del alfabeto coincide con un estado")
        else:
            lista_Alfabeto.append(cadena2[2]) 

        #GUARDANDO ESTADO INICIAL
        inicial = AFD_Lineas[0].split(",")
        estado_Inicial = inicial[0]

        #GUARDANDO ESTADOS DE ACEPTACION
        lista_EstadosAceptacion = lista_Estados.copy()
  
        if (cadena2[0] in lista_EstadosAceptacion) and (cadena3[0].upper()== "FALSE"):
            lista_EstadosAceptacion.remove(cadena2[0])
        if (cadena2[1] in lista_EstadosAceptacion) and (cadena3[1].upper()=="FALSE"):
            lista_EstadosAceptacion.remove(cadena2[1])
        else:
            pass

        #GUARDANDO LAS TRANSICIONES
        existe=False
        #VERIFICANDO SI YA EXISTE EL ESTADO EN LA LISTA
        for x in range(0, len(lista_Transiciones)):
            if cadena2[0] == lista_Transiciones[x].nombre:
                existe = True
            else:
                continue

        if existe == True: # SI YA EXISTE, BUSCAR EL ESTADO Y SOLO AGREGAR LA TRANSICION
            #print("El estado "+cadena2[0]+" ya existe")
            buscarEstado(cadena2[0], lista_Transiciones).definirTransicion(cadena2[1],cadena2[2])
        else: # SINO EXISTE, CREAR NUEVO ESTADO Y AGREGAR LA TRANSICION
            #print("El estado "+cadena2[0]+" no existe")
            estado_Tem = Estado()
            estado_Tem.agregarNombre(cadena2[0])
            estado_Tem.definirTransicion(cadena2[1],cadena2[2])
            lista_Transiciones.append(estado_Tem)
    
    print("Estados")
    print(lista_Estados)
    print("Alfabeto")
    print(lista_Alfabeto)
    print("Estado inicial")
    print(estado_Inicial)
    print("Estados de aceptacion")
    print(lista_EstadosAceptacion)
    print("Transiciones")
    mostrarLista(lista_Transiciones)

    print("\n\nEscriba -Si- o -No_")
    respuesta = input("Desea guardar el AFD: ")

    if respuesta.upper() == "SI":
        os.system('clear')
        nombre_AFD = input("Ingrese el nombre del AFD: ")    
            
        while verificar_Lista_Vacia(nombre_AFD)==True:
            os.system('clear') 
            print("\n--------- DEBE INGRESAR UN NOMBRE VALIDO ---------")
            nombre_AFD = input("Ingrese el nombre del AFD: ")


        nombre_AFD=nombre_AFD+" AFD"

        print("Automata guardado con exito como -"+nombre_AFD+"-")




    elif respuesta.upper() == "NO":
        print("Proceso cancelado")
    else:
        print("Respuesta no valida")





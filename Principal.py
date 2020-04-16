
import os
from Objeto import Automata
from Objeto import Estado
from Objeto import Transicion
from Objeto import GramaticaRegular
from RutaAFD import Ruta_AFD
from Evaluar_Cadena import Verifica_Cadena
from ExpandirGramatica import Expande_Gramatica
from Objeto import modo2
from graphviz import Digraph
from reportlab.pdfgen import canvas
from reportlab.lib.colors import white,red,green,blue,gray,black
from Evaluar_Cadena import Verifica_Cadena_Retorna



listaAutomatas=[]
listaGramaticas=[]
opcion =0
opcion1=0
encontrado = False
posiblesEstados=["A","B","C","D","E","F","G","H","I","J","K","L","M",
"N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def buscar_Gramatica(nombreGramatica):
    gramatica_Temporal= GramaticaRegular("","","","","","")
    for x in range(0, len(listaGramaticas)):
        if nombreGramatica == listaGramaticas[x].nombre:
            gramatica_Temporal=listaGramaticas[x]
        else:
            continue
    return gramatica_Temporal

def buscar_AFD(nombreAFD):
    AFD = Automata("","","","","","")
    for x in range(0, len(listaAutomatas)):
        if nombreAFD == listaAutomatas[x].nombre:
            AFD = listaAutomatas[x]
        else:
            continue
    return AFD

def validar_Cadena(nombreGramatica):
    #BUSCANDO LA GRAMATICA
    gramatica = buscar_Gramatica(nombreGramatica)
    contador=0

    cadena = input("Ingrese la cadena a evaluar: ")

    inicio = gramatica.NT_Inicial
    finalizar = gramatica.estadosAceptacion
    actual=gramatica.NT_Inicial

    while contador < len(cadena):
        for No_Terminal in gramatica.No_Terminales:
            for terminal in gramatica.terminales:
                if actual == No_Terminal:
                    if cadena[contador]==terminal:
                        actual=No_Terminal
                    contador+=1
                    continue

    if actual==finalizar:
        print("CADENA CORRECTA")
    else:
        print("CADENA INCORRECTA")

def buscarEstado(nombre,lista):
    estado=Estado()
    for x in range(0, len(lista)):
        if nombre == lista[x].nombre:
            estado=lista[x]
        else:
            continue
    return estado

def buscarSimbolo(estadoDe, lista, simbolo):
    encontrado=False
    
    estadoTemp = buscarEstado(estadoDe, lista)
    for x in estadoTemp.transiciones:
        if simbolo == x.get_Simbolo():
            encontrado = True
        else:
            continue
    return encontrado

def buscarEstadoo(nombre,lista):
    listaAux=[]
    for x in range(0, len(lista)):
        if nombre == lista[x].nombre:
            listaAux=lista[x].transiciones
        else:
            continue
    return listaAux

def buscar_Estado_Boolean(nombre,lista):
    encontrado = False
    for x in lista:
        if nombre==x:
            encontrado=True
        else:
            continue
    return encontrado

def mostrar_Transiciones():
    for x in listaAutomatas:
        for i in x.transiciones:
            print(i)

def verificar_Lista_Vacia(estructura):
    if estructura:
        #No esta vacia
        return False
    else:
        #Esta vacia
        return True    

def mostrarLista(lista):
    for x in lista:
        print("DE "+x.nombre)
        for i in x.transiciones:
            print(i)

def imprimirLista(lista):
    for x in lista:
        print(x)

def mostrar_Lista_Automatas():
    for x in listaAutomatas:
        print("\n")
        print("NOMBRE")
        print(x.nombre)
        print("ESTADOS")
        print(x.estados)
        print("ALFABETO")
        print(x.alfabeto)
        print("ESTADO INICIAL")
        print(x.estado_Inicial)
        print("ESTADOS DE ACEPTACION")
        print(x.estados_Aceptacion)
        print("TRANSICIONES")
        mostrarLista(x.transiciones)

def mostrar_Lista_Gramaticas():
    for x in listaGramaticas:
        print("\n")
        print("NOMBRE")
        print(x.nombre)
        print("NT")
        print(x.No_Terminales)
        print("TERMINALES")
        print(x.terminales)
        print("NT INICIAL")
        print(x.NT_Inicial)
        print("PRODUCCIONES")
        mostrarLista(x.producciones)
        print("ESTADOS DE ACEPTACION")
        print(x.estadosAceptacion)

def caratula():
    print("\n\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+-          LENGUAJES FORMALES Y DE PROGRAMACION           -+")
    print("+-                     SECCION B-                          -+")
    print("+-                     201807265                           -+")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    input("Presione Enter para continuar... ")
  
def ayuda():
    print("\n<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<")
    print("<:           LENGUAJES FORMALES Y DE PROGRAMACION          :>")
    print("<:                     SECCION B-                          :>")
    print("<:              Luis Javier Yela Quijada                   :>")
    print("<:                         5                               :>")
    print("<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<\n")


def leerArchivoAFD():
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
        #cadena2 = [ 'A', 'A', '1']
        #cadena3 = [ 'true', 'true']

        #
        if cadena3[0].upper()=="TRUE":
            lista_EstadosAceptacion.append(cadena2[0])
        if cadena3[0].upper()=="FALSE":
            if cadena2[0] in lista_EstadosAceptacion:
                lista_EstadosAceptacion.remove(cadena2[0])
            else:
                pass


        if cadena3[1].upper()=="TRUE":
            lista_EstadosAceptacion.append(cadena2[1])
        if cadena3[1].upper()=="FALSE":
            if cadena2[1] in lista_EstadosAceptacion:
                lista_EstadosAceptacion.remove(cadena2[1])
            else:
                pass

        

        #GUARDANDO LAS TRANSICIONES
        #cadena2 = [ 'A', 'A', '1']
        #cadena3 = [ 'true', 'true']
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

    direccion = os.path.split(ruta)
    print(direccion)
    nombre_AFD_Archivo = direccion[1]+" AFD"
    print(nombre_AFD_Archivo)
    nombre_Gramatica_Correspondiente = direccion[1]+" Gramatica"

    print("\n\nEscriba -Si- o -No_")
    respuesta = input("Desea guardar el AFD: ")

    if respuesta.upper() == "SI":
        os.system('cls')
        
        #CREANDO OBJETO AUTOMATA
        automata_Aux = Automata(nombre_AFD_Archivo,lista_Estados,lista_Alfabeto,
        estado_Inicial,lista_EstadosAceptacion,lista_Transiciones)

        listaAutomatas.append(automata_Aux)

        #CREANDO SU GRAMATICA CORRESPONDIENTE
        gramatica_Aux = GramaticaRegular(nombre_Gramatica_Correspondiente,lista_Estados,
        lista_Alfabeto,estado_Inicial,lista_Transiciones,lista_EstadosAceptacion)

        listaGramaticas.append(gramatica_Aux)
       



        print("Automata guardado con exito como -"+nombre_AFD_Archivo+"-")
        print("AUTOMATAS")
        #for x in listaAutomatas:
        #    mostrar_Lista_Automatas(x.transiciones)

        #print("GRAMATICAS")
        #for i in listaGramaticas:
        #    mostrar_Lista_Gramaticas(i.producciones)


    elif respuesta.upper() == "NO":
        print("Proceso cancelado")
    else:
        print("Respuesta no valida")

def leerArchivoGramatica():
    lista_NoTerminales = []
    lista_Terminales = []
    Nt_Inicial = ""
    lista_Producciones = []
    lista_Estados_Aceptacion = []

    rutaG = input("Ingrese la ruta del archivo Gramatica: ")
    archivoG = open(rutaG,"r")
    archivoG_Lineas = archivoG.readlines()
    Gramatica_Lineas = []

    for linea in archivoG_Lineas:
        Gramatica_Lineas.append(linea.strip())

    #print(Gramatica_Lineas)
    #print()
  
    for x in Gramatica_Lineas:
        entrada1 = x.split(">") # [ 'A', 'c B' ]
        entrada2 = entrada1[1].split(" ") # [ ' ', 'c', 'B' ]
              

        print(entrada1)
        print(entrada2)
        print()
        
        #GUARDANDO NO TERMINALES
        if entrada1[0].strip() in lista_NoTerminales:
            pass
        elif entrada1[0].strip() in posiblesEstados:
            lista_NoTerminales.append(entrada1[0].strip())
        else:
            print("No hay estados")

        #GUARDANDO TERMINALES
        if entrada2[1].strip() in lista_Terminales:
            lista_Terminales.remove(entrada2[1].strip())
        if entrada2[1].strip() == "epsilon":
            lista_Estados_Aceptacion.append(entrada1[0].strip())
        else:
            lista_Terminales.append(entrada2[1].strip())

        #GUARDANDO NT INICIAL
        nt_Inicial = Gramatica_Lineas[0].split(">") 
        Nt_Inicial = nt_Inicial[0].strip()

        #GUARDANDO PRODUCCIONES
        # entrada1 = [ 'A', 'c B' ]
        # entrada2 = [ ' ', 'c', 'B' ]
        encontrado = False
        for i in range (0, len(lista_Producciones)):
            if entrada1[0] == lista_Producciones[i].nombre:
                encontrado = True
            else:
                continue
        if len(entrada2)==2:
            pass
        else:
            if encontrado == True:
                buscarEstado(entrada1[0], lista_Producciones).definirTransicion(entrada2[2],entrada2[1])
            else:
                estado_Aux = Estado()
                estado_Aux.agregarNombre(entrada1[0])
                estado_Aux.definirTransicion(entrada2[2],entrada2[1])
                lista_Producciones.append(estado_Aux)

    print(lista_NoTerminales)
    print(lista_Terminales)
    print(Nt_Inicial)
    print(lista_Estados_Aceptacion)
    print("Producciones")
    mostrarLista(lista_Producciones)

    direccionG = os.path.split(rutaG)
    nombre_Gramatica_Archivo = direccionG[1]+" Gramatica"
    nombreAfd_Correspondiente = direccionG[1]+" AFD"

    print("\n\nEscriba -Si- o -No_")
    confirmar = input("Desea guardar la gramatica: ")

    if confirmar.upper() == "SI":
        os.system('cls')

        #CREANDO OBJETO GRAMATICA
        gramaticaA = GramaticaRegular(nombre_Gramatica_Archivo,lista_NoTerminales,
        lista_Terminales,Nt_Inicial,lista_Producciones,lista_Estados_Aceptacion)

        listaGramaticas.append(gramaticaA)

        #CREANDO AFD CORRRESPONDIENTE
        Afd = Automata(nombreAfd_Correspondiente,lista_NoTerminales,lista_Terminales,
        Nt_Inicial,lista_Estados_Aceptacion,lista_Producciones)

        listaAutomatas.append(Afd)

def menu():

    while True:
        print("\n---------->>> Se encuentra en el MENU PRINCIPAL <<<----------")
        print("1. Crear AFD")
        print("2. Crear gramatica")
        print("3. Evaluar cadenas")
        print("4. Reportes")
        print("5. Cargar archivo para AFD")
        print("6. Cargar archivo para gramatica")
        print("7. Salir")
        print("8. Gramaticas tipo2 y AP")
        print("9. Mostrar AUTOMATAS y GRAMATICAS existentes")    
        opcion = input("Ingrese una opcion: ")

        if verificar_Lista_Vacia(str(opcion))==True: #ESTA VACIA
            os.system('cls')
            print("********* Debe ingresar una opcion valida, intente nuevamente *********")
        else:
            opcion=int(opcion)

            if opcion == 1:
                listaTemporal_Estados=[]
                listaTemporal_Alfabeto=[]
                estadoTemporal_Inicial=""
                listaTemporal_EstadosAceptacion=[]
                listaTemporal_Transiciones=[]

                os.system('cls')
                nombre_AFD = input("Ingrese el nombre del AFD: ")

                Automata_Existente = False
                for objeto_Automata in listaAutomatas:
                    if objeto_Automata.nombre == (nombre_AFD+" AFD"):
                        Automata_Existente = True 
                        print("Ya existe el nombre")
                    else:
                        continue   
                
                while verificar_Lista_Vacia(nombre_AFD)==True:
                    os.system('cls') 
                    print("\n--------- DEBE INGRESAR UN NOMBRE VALIDO ---------")
                    nombre_AFD = input("Ingrese el nombre del AFD: ")


                nombreaux=nombre_AFD
                nombre_AFD=nombre_AFD+" AFD"
                contador1=1
                contador2=1
                contador4=1
                contador5=1
            
                while True:
                    print("---------->>> Se encuentra en el MENU CREAR AFD <<<----------")
                    print("1. Ingresar estados")
                    print("2. Ingresar alfabeto")
                    print("3. Estado inicial")
                    print("4. Estados de aceptacion")
                    print("5. Transiciones")
                    print("6. Ayuda")
                    print("7. Salir")
                    print("8. Guardar automata")
                    opcion1=input("Ingrese una opcion ")

                    if verificar_Lista_Vacia(str(opcion1))==True: #ESTA VACIA
                        os.system('cls')
                        print("\n********* Debe ingresar una opcion valida, intente nuevamente *********")

                    if Automata_Existente == True: #El automata ya existe
                        AFD_Existente = buscar_AFD(nombre_AFD)
                        Gram_Correspondiente = buscar_Gramatica(nombreaux+" Gramatica")
                        opcion1=int(opcion1)

                        if opcion1==1:
                            os.system('cls')
                            contE= len(AFD_Existente.estados)+1
                            print("Ingresando estados a: "+nombre_AFD+"\n")
                            estado= input("Estado No."+str(contE)+": ")
                            estado= estado.upper()

                            if verificar_Lista_Vacia(estado)==True:
                                print("\n******** DEBE INGRESAR UN ESTADO VALIDO, INTENTE NUEVAMENTE ********")
                            elif estado in AFD_Existente.estados:
                                print("\nEL ESTADO INGRESADO YA EXISTE, INGRESE UNO DISTINTO")
                            elif estado in AFD_Existente.alfabeto:
                                print("\nEL ESTADO INGRESADO COINCIDE CON UN SIMBOLO DEL ALFABETO, INTENTE NUEVAMENTE")
                            else:
                                AFD_Existente.estados.append(estado)
                                contE+=1

                        elif opcion1==2:
                            os.system('cls')
                            contA= len(AFD_Existente.alfabeto)+1
                            print("Ingresando alfabeto a: "+nombre_AFD)
                            terminal=input("Simbolo No. "+str(contA)+":") # TERMINAL ES UN SIMBOLO DEL ALFABETO

                            if verificar_Lista_Vacia(terminal)==True:
                                print("\n******** DEBE INGRESAR UN SIMBOLO VALIDO, INTENTE NUEVAMENTE ********")
                            else:
                                if terminal in AFD_Existente.estados:
                                    os.system('cls')
                                    print("\nEL SIMBOLO INGRESADO COINCIDE EN LA LISTA DE ESTADOS")
                                elif terminal in AFD_Existente.alfabeto:
                                    print("\nEL SIMBOLO INGRESADO YA EXISTE")
                                else:
                                    os.system('cls')
                                    AFD_Existente.alfabeto.append(terminal)
                                    contA=contA+1

                        elif opcion1==3:
                            os.system('cls')
                            AFD_Existente.estado_Inicial = ""
                            print("Ingresando estado inicial a: "+nombre_AFD)
                            inicial=input("Estado inicial: ")
                            inicial=inicial.upper()


                            if inicial in AFD_Existente.estados:
                                AFD_Existente.estado_Inicial = inicial
                                Gram_Correspondiente.NT_Inicial=""
                                Gram_Correspondiente.NT_Inicial=inicial
                            else:
                                inicial=""
                                print("\nEL ESTADO INICIAL INGRESADO NO EXISTE EN LA LISTA DE ESTADOS")
                            

                        elif opcion1==4:
                            os.system('cls')
                            contEA= len(AFD_Existente.estados_Aceptacion)+1
                            print("Ingresando estados de aceptacion a: "+nombre_AFD)
                            E_aceptacion= input("Estado de aceptacion No. "+str(contEA)+":")
                            E_aceptacion=E_aceptacion.upper()

                            if E_aceptacion in AFD_Existente.estados:
                                if E_aceptacion in AFD_Existente.estados_Aceptacion:
                                    print("El estado de aceptación ya existe")
                                else:
                                    AFD_Existente.estados_Aceptacion.append(E_aceptacion)
                                    contEA=contEA+1

                            else:
                                print("\nEL ESTADO DE ACEPTACION INGRESADO NO EXISTE EN LA LISTA DE ESTADOS")

                        elif opcion1==5:
                            os.system('cls')
                            print("Ingresando transiciones a: "+nombre_AFD)
                            while True:
                                print("---------->>> Se encuentra en el menu CREAR AFD - TRANSICIONES <<<----------")
                                print("1. Modo 1")
                                print("2. Salir")
                                opcion1=int(input("Ingrese una opcion: "))

                                if opcion1==1:
                                    existe=False
                                    os.system('cls')
                                    print("----- Se encuentra en el modo 1 -----")
                                    print("NOTA: La notacion correcta para ingresar una transicione es: A,B;0\n")
                                    transicion=input("Ingresando transicion: ") #A,B;0
                                    separacion1=transicion.split(";") #["A,B","0"]              
                                    separacion2=separacion1[0].split(",") #["A","B"]                        
                                    terminal = separacion1[1] #0
                                    
                                    #VERIFICANDO SI EXISTE EL ESTADO EN LA LISTA
                                    for x in range(0, len(AFD_Existente.transiciones)):
                                        if separacion2[0] == AFD_Existente.transiciones[x].nombre:
                                            existe=True
                                        else:
                                            continue
                                        
                                    #SI EXISTE, BUSCAR EL ESTADO Y SOLO AGREGAR LA TRANSICION            
                                    if existe==True:
                                        if buscarSimbolo(separacion2[0],AFD_Existente.transiciones,terminal) == True:
                                            print("La transición ingresada es ambigua (Repite simbolo desde un mismo estado)")
                                        else:
                                            print("EL ESTADO -"+separacion2[0]+"- YA EXISTE")
                                            buscarEstado(separacion2[0],AFD_Existente.transiciones).definirTransicion(separacion2[1],terminal)
                                    #SINO EXISTE, CREAR UN NUEVO ESTADO Y AGREGAR LA TRANSICION
                                    else:
                                        print("EL ESTADO -"+separacion2[0]+"- NO EXISTE")
                                        estado_Temporal=Estado()
                                        estado_Temporal.agregarNombre(separacion2[0])
                                        estado_Temporal.definirTransicion(separacion2[1],terminal)
                                        AFD_Existente.transiciones.append(estado_Temporal)                                
                                                

                                elif opcion1==2:
                                    os.system('cls')
                                    break
                               
                                else:
                                    os.system('cls')
                                    print("La opcion seleccionada no existe")

                        elif opcion1==6:
                            os.system('cls')
                            ayuda()
                            
                        elif opcion1==7:
                            os.system('cls')
                            break
                        
                    else: # EL AUTOMATA NO EXISTE
                        opcion1=int(opcion1)

                        if opcion1==1:
                            os.system('cls')
                            print("Ingresando estados a: "+nombre_AFD+"\n")
                            estado= input("Estado No."+str(contador1)+": ")
                            estado= estado.upper()

                            if verificar_Lista_Vacia(estado)==True:
                                print("\n******** DEBE INGRESAR UN ESTADO VALIDO, INTENTE NUEVAMENTE ********")
                            elif estado in listaTemporal_Estados:
                                print("\nEL ESTADO INGRESADO YA EXISTE, INGRESE UNO DISTINTO")
                            elif estado in listaTemporal_Alfabeto:
                                print("\nEL ESTADO INGRESADO COINCIDE CON UN SIMBOLO DEL ALFABETO, INTENTE NUEVAMENTE")
                            else:
                                listaTemporal_Estados.append(estado)                    
                                contador1=contador1+1
                        
                        #TERMINA INGRESAR ESTADOS

                        elif opcion1==2:
                            os.system('cls')
                            print("Ingresando alfabeto a: "+nombre_AFD)
                            terminal=input("Simbolo No. "+str(contador2)+":") # TERMINAL ES UN SIMBOLO DEL ALFABETO

                            if verificar_Lista_Vacia(terminal)==True:
                                print("\n******** DEBE INGRESAR UN SIMBOLO VALIDO, INTENTE NUEVAMENTE ********")
                            else:
                                if terminal in listaTemporal_Estados:
                                    os.system('cls')
                                    print("\nEL SIMBOLO INGRESADO COINCIDE EN LA LISTA DE ESTADOS")
                                elif terminal in listaTemporal_Alfabeto:
                                    print("\nEL SIMBOLO INGRESADO YA EXISTE")
                                else:
                                    os.system('cls')
                                    listaTemporal_Alfabeto.append(terminal)
                                    contador2=contador2+1
                        #TERMINA INGRESAR ALFABETO

                        elif opcion1==3:
                            os.system('cls')
                            print("Ingresando estado inicial a: "+nombre_AFD)
                            inicial=input("Estado inicial: ")
                            inicial=inicial.upper()

                            if inicial in listaTemporal_Estados:
                                estadoTemporal_Inicial=inicial
                            else:
                                inicial=""
                                print("\nEL ESTADO INICIAL INGRESADO NO EXISTE EN LA LISTA DE ESTADOS")
                            
                        #TERMINA INGRESAR ESTADO INICIAL

                        elif opcion1==4:
                            os.system('cls')
                            print("Ingresando estados de aceptacion a: "+nombre_AFD)
                            E_aceptacion= input("Estado de aceptacion No. "+str(contador4)+":")
                            E_aceptacion=E_aceptacion.upper()

                            if E_aceptacion in listaTemporal_Estados:
                                listaTemporal_EstadosAceptacion.append(E_aceptacion)
                                contador4=contador4+1
                            else:
                                print("\nEL ESTADO DE ACEPTACION INGRESADO NO EXISTE EN LA LISTA DE ESTADOS")
                        #TERMINA INGRESAR ESTADOS DE ACEPTACION
                        
                        elif opcion1==5:
                            os.system('cls')
                            print("Ingresando transiciones a: "+nombre_AFD)
                            while True:
                                print("---------->>> Se encuentra en el menu CREAR AFD - TRANSICIONES <<<----------")
                                print("1. Modo 1")
                                print("2. Modo 2")
                                print("3. Salir")
                                opcion1=int(input("Ingrese el modo: "))

                                if opcion1==1:
                                    existe=False
                                    os.system('cls')
                                    print("----- Se encuentra en el modo 1 -----")
                                    print("NOTA: La notacion correcta para ingresar una transicione es: A,B;0\n")
                                    transicion=input("Transicion No. "+str(contador5)+": ") #A,B;0
                                    separacion1=transicion.split(";") #["A,B","0"]              
                                    separacion2=separacion1[0].split(",") #["A","B"]                        
                                    terminal = separacion1[1] #0
                                    
                                    #VERIFICANDO SI EXISTE EL ESTADO EN LA LISTA
                                    for x in range(0, len(listaTemporal_Transiciones)):
                                        if separacion2[0] == listaTemporal_Transiciones[x].nombre:
                                            existe=True
                                        else:
                                            continue
                                        
                                    #SI EXISTE, BUSCAR EL ESTADO Y SOLO AGREGAR LA TRANSICION            
                                    if existe==True:
                                        if buscarSimbolo(separacion2[0],listaTemporal_Transiciones,terminal) == True:
                                            print("La transición ingresada es ambigua (Repite simbolo desde un mismo estado)")
                                            contador5=contador5-1
                                        else:
                                            print("EL ESTADO -"+separacion2[0]+"- YA EXISTE")
                                            buscarEstado(separacion2[0],listaTemporal_Transiciones).definirTransicion(separacion2[1],terminal)
                                    #SINO EXISTE, CREAR UN NUEVO ESTADO Y AGREGAR LA TRANSICION
                                    else:
                                        print("EL ESTADO -"+separacion2[0]+"- NO EXISTE")
                                        estado_Temporal=Estado()
                                        estado_Temporal.agregarNombre(separacion2[0])
                                        estado_Temporal.definirTransicion(separacion2[1],terminal)
                                        listaTemporal_Transiciones.append(estado_Temporal)                                
                                                
                                    contador5=contador5+1

                                #TERMINA EL MODO 1
                                elif opcion1==2:
                                    os.system('cls')
                                    print("----- Se encuentra en el modo 2 -----")

                                    lista_Alfabeto = []
                                    lista_Estados_De = []
                                    lista_Temporal = []
                                    lista_Transiciones = []

                                    print("\n\n-- NOTA --: La forma de ingresar: \n          Alfabeto: [simbolo1, simbolo2...]\n          Estados: [estado1, estado2...]\n          Transiciones: [estadoDe,estadoHacia;...]")
                                    print()
                                    cadena1= input("Ingrese el alfabeto: ")
                                    cadena2= input("Ingrese los estados: ")
                                    cadena3= input("Ingrese las transiciones: ")

                                    #ELIMINANDO CORCHETES
                                    cadena1 = cadena1.strip("[]")
                                    cadena2 = cadena2.strip("[]")
                                    cadena3 = cadena3.strip("[]")

                                    #SEPARANDO CADENA1 Y ALMACENANDO EN LISTA_ALFABETO
                                    lista_Alfabeto = cadena1.split(",") #[ a, b ]
                                    #SEPARANDO CADENA2 Y ALMACENANDO EN LISTA_ESTADOS_DE
                                    lista_Estados_De = cadena2.split(",") # [ A, B, C, D]
                                    #SEPARANDO CADENA3 Y ALMACENANDO EN LISTA_TEMPORAL
                                    lista_Temporal = cadena3.split(";") # [ A,C; A,C; B,D; -,-]

                                    contador = 0
                                    for estado_De in lista_Estados_De:
                                        estadoTemporal = Estado()
                                        estadoTemporal.agregarNombre(estado_De)
                                        for indice in range(0,len(lista_Alfabeto)):
                                            aux = lista_Temporal[contador].split(",") # [ A,C]
                                            if aux[indice] =="-": # SI EL SIMBOLO ES - NO HACER NADA
                                                print("Entro")
                                                pass
                                            else: # SI NO ES -, GUARDAR UNA TRANSICION NORMAL
                                                estadoTemporal.definirTransicion(aux[indice],lista_Alfabeto[indice])

                                        contador+=1

                                        if len(estadoTemporal.transiciones)==0:# SI LA LONGITUD DE LA LISTA DE TRANSICIONES DE UN ESTADO DE ES 0, NO HACER NADA
                                            pass
                                        else: # EN CAMBIO, AGREGAR A LA LISTA DE TRANSICIONES OBJETOS DE TIPO ESTADO-DE
                                            lista_Transiciones.append(estadoTemporal)

                                    listaTemporal_Transiciones = lista_Transiciones.copy()

                                elif opcion1==3:
                                    os.system('cls')
                                    break
                               
                                else:
                                    os.system('cls')
                                    print("La opcion seleccionada no existe")                             
                        #TERMINA INGRESAR TRANSICIONES  
                         
                        elif opcion1==6:
                            os.system('cls')
                            ayuda()
                       
                        elif opcion1==7:
                            os.system('cls')
                            break
                       
                        elif opcion1==8:
                            confirmar=input("\n¿Esta seguro que quiere guardar el AFD? ")
                            if confirmar.upper()=="SI":
                                os.system('cls')
                                #CREANDO OBJETO AUTOMATA
                                automata_Temporal=Automata(nombre_AFD,listaTemporal_Estados,listaTemporal_Alfabeto,
                                estadoTemporal_Inicial,listaTemporal_EstadosAceptacion,listaTemporal_Transiciones)
                                #AGREGANDO A LA LISTA AUTOMATAS
                                listaAutomatas.append(automata_Temporal)

                                #GUARDANDO SU GRAMATICA CORRESPONDIENTE
                                nombre_Gramatica=nombreaux+" Gramatica"
                                gramatica_Temporal=GramaticaRegular(nombre_Gramatica,listaTemporal_Estados,listaTemporal_Alfabeto,
                                estadoTemporal_Inicial,listaTemporal_Transiciones,listaTemporal_EstadosAceptacion)
                                #AGREGANDO A LA LISTA
                                listaGramaticas.append(gramatica_Temporal)

                                print("AFD guardado con exito")
                                
                                break

                            elif confirmar.upper()=="NO":
                                os.system('cls')
                                print("Proceso cancelado")
                            else:
                                os.system('cls')
                                print("Opcion NO VALIDA")
                                print("Escriba -SI- o -NO-")
                       
                        else:
                            os.system('cls')
                            print ("La opcion seleccionada no existe")      

                    # TERMINA LA OPCION DE CREAR AFD    
            #TERMINA CREAR AFD
                    
            elif opcion == 2:
                listaTemporal_NT=[]
                listaTemporal_Terminales=[]
                NT_Inicial=""
                listaTemporal_Producciones=[]
                listaTemporal_EstadosAceptacionG=[]

                os.system('cls')
                nombre_Gramatica= input("Ingrese el nombre de la gramatica: ")

                Gramatica_Existente = False
                for objeto_Gramatica in listaGramaticas:
                    if objeto_Gramatica.nombre == (nombre_Gramatica+" Gramatica"):
                        Gramatica_Existente = True 
                        print("Ya existe la Gramatica, entonces solo puede modificarse")
                    else:
                        continue  

                while verificar_Lista_Vacia(nombre_Gramatica)==True:
                    os.system('cls') 
                    print("\n--------- DEBE INGRESAR UN NOMBRE VALIDO ---------")
                    nombre_Gramatica= input("Ingrese el nombre de la gramatica: ")

                temp = nombre_Gramatica+" AFD"
                nombreOriginalG=nombre_Gramatica
                nombre_Gramatica=nombre_Gramatica+" Gramatica"


                contador1G=1
                contador2G=1
                contador4G=1

                while True:
                    print("---------->>> Se encuentra en el MENU CREAR GRAMATICA <<<----------")
                    print("1. Ingresar NT")
                    print("2. Ingresar terminales")
                    print("3. NT inicial")
                    print("4. Producciones")
                    print("5. Mostrar gramatica transformada")
                    print("6. Ayuda")
                    print("7. Salir")
                    print("8. Guardar gramatica")
                    opcion2=input("Ingrese una opcion ")

                    if verificar_Lista_Vacia(str(opcion2))==True: #ESTA VACIA
                        os.system('cls')
                        print("********* Debe ingresar una opcion valida, intente nuevamente *********")
                    
                    if Gramatica_Existente == True:
                        Gram_Existente = buscar_Gramatica(nombre_Gramatica)
                        AFD_Correspondiente = buscar_AFD(temp)
                        opcion2=int(opcion2)

                        if opcion2==1:
                            os.system('cls')
                            contG=len (Gram_Existente.No_Terminales)+1
                            print("Ingresando NT a: "+nombre_Gramatica+"\n")
                            NT=input("NT No."+str(contG)+": ")
                            NT = NT.upper()

                            if verificar_Lista_Vacia(NT)==True: #CADENA VACIA
                                print("********* DEBE INGRESAR UN NT VALIDO, INTENTE NUEVAMENTE *********")
                            elif NT in Gram_Existente.No_Terminales:
                                print("EL NT INGRESADO YA EXISTE, INGRESE UNO DISTINTO")
                            elif NT in Gram_Existente.terminales:
                                print("EL NT INGRESADO COINCIDE CON UN TERMINAL, INTENTE NUEVAMENTE")
                            else:
                                Gram_Existente.No_Terminales.append(NT)
                                contG+=1 

                            imprimirLista(listaTemporal_NT)

                        elif opcion2==2:
                            os.system('cls')
                            contT=len(Gram_Existente.terminales)+1
                            print("Ingresando terminal a: "+nombre_Gramatica+"\n")
                            terminal = input("Terminal No."+str(contT)+": ")


                            if verificar_Lista_Vacia(terminal)==True: #CADENA VACIA
                                print("********* DEBE INGRESAR UN TERMINAL VALIDO, INTENTE NUEVAMENTE *********")
                            else:
                                #SI EL TERMINAL EXISTE EN LA LISTA DE NT
                                if terminal in Gram_Existente.No_Terminales:
                                    os.system('cls')
                                    print("\nERROR! EL TERMINAL INGRESADO COINCIDE EN LA LISTA DE NT\n")
                                elif terminal in Gram_Existente.terminales:
                                    os.system('cls')
                                    print("\nERROR! EL TERMINAL INGRESADO YA EXISTE\n")
                                else:
                                    os.system('cls')
                                    Gram_Existente.terminales.append(terminal)
                        

                            for x in Gram_Existente.terminales:
                                print(x)
                         
                        elif opcion2==3:
                            os.system('cls')
                            print("Ingresando NT inicial a: "+nombre_Gramatica+"\n")
                            Inicial = input("Estado inicial: ")
                               
                            if Inicial in Gram_Existente.No_Terminales: #SI EL NT EXISTE EN LA LISTA DE NT
                                Gram_Existente.NT_Inicial = Inicial 
                                AFD_Correspondiente.estado_Inicial =""
                                AFD_Correspondiente.estado_Inicial = Inicial
                            else: #SI NO EXISTE VACIAR LA VARIABLE Y MOSTRAR EL ERROR
                                NT_Inicial=""
                                print("\nEL NT INGRESADO NO EXISTE NE LA LISTA DE NT")

                            
                            

                            print(NT_Inicial)   
                    
                        elif opcion2==4:
                            existe=False
                            os.system('cls')
                            print("Ingresando producciones a: "+nombre_Gramatica+"\n")
                            print("NOTA: La notacion correcta para ingresar una produccion es \"A>a B\"")
                            print("      Tome en cuenta el espacio del lado derecho de la produccion\n")
                            produccion = input("Produccion: ") # A>a B
                            separacion1=produccion.split(">") #[ "A","a B" ]
                            separacion2=separacion1[1].split(" ") # [ "a" , "B" ]

                            #AGREGANDO ESTADOS DE ACEPTACION
                            if separacion1[1].upper()=="EPSILON":
                                Gram_Existente.estadosAceptacion.append(separacion1[0])
                                print("Se agrego a "+separacion1[0]+" como estado de aceptacion")
                            else:
                                estado_De = separacion1[0]
                                estado_Hacia = separacion2[1]
                                simbolo=separacion2[0]

                                #VERIFICANDO SI EXISTE EL ESTADO_DE EN LA LISTA 
                                for x in range(0, len(Gram_Existente.producciones)):
                                    if estado_De==Gram_Existente.producciones[x].nombre:
                                        existe=True
                                    else:
                                        continue

                                #SI EXISTE BUSCA EL ESTADO Y SOLO AGREGAR LA PRODUCCION
                                if existe==True:
                                    if buscarSimbolo(separacion1[0],Gram_Existente.producciones,separacion2[0]):
                                        print("La produccion ingresada es ambigua (Repite simbolo desde un mismo estado)")
                                    else:
                                        print("El estado "+estado_De+" Ya existe")
                                        buscarEstado(estado_De,Gram_Existente.producciones).definirTransicion(estado_Hacia,simbolo)
                                #SINO EXISTE, CREAR UN NUEVO ESTADO Y AGREGAR LA PRODUCCION
                                else: 
                                    print("El estado "+estado_De+" No existe")
                                    estadoTemporal=Estado()
                                    estadoTemporal.agregarNombre(estado_De)
                                    estadoTemporal.definirTransicion(estado_Hacia,simbolo)

                                    Gram_Existente.producciones.append(estadoTemporal)

                        elif opcion2==6:
                            os.system('cls')
                            ayuda()
                       
                        elif opcion2==7:
                            os.system('cls')
                            break

                        else:
                            os.system('cls')
                            print ("La opcion seleccionada no existe")

                    else:
                        opcion2=int(opcion2)

                        if opcion2==1:
                            os.system('cls')
                            print("Ingresando NT a: "+nombre_Gramatica+"\n")
                            NT=input("NT No."+str(contador1G)+": ")
                            NT = NT.upper()

                            if verificar_Lista_Vacia(NT)==True: #CADENA VACIA
                                print("********* DEBE INGRESAR UN NT VALIDO, INTENTE NUEVAMENTE *********")
                            elif NT in listaTemporal_NT:
                                print("EL NT INGRESADO YA EXISTE, INGRESE UNO DISTINTO")
                            elif NT in listaTemporal_Terminales:
                                print("EL NT INGRESADO COINCIDE CON UN TERMINAL, INTENTE NUEVAMENTE")
                            else:
                                listaTemporal_NT.append(NT)
                                contador1G+=1 

                            imprimirLista(listaTemporal_NT)

                            #TERMINA INGRESAR NT
                        
                        elif opcion2==2:
                            os.system('cls')
                            print("Ingresando terminal a: "+nombre_Gramatica+"\n")
                            terminal = input("Terminal No."+str(contador2G)+": ")


                            if verificar_Lista_Vacia(terminal)==True: #CADENA VACIA
                                print("********* DEBE INGRESAR UN TERMINAL VALIDO, INTENTE NUEVAMENTE *********")
                            else:
                                #SI EL TERMINAL EXISTE EN LA LISTA DE NT
                                if terminal in listaTemporal_NT:
                                    os.system('cls')
                                    print("\nERROR! EL TERMINAL INGRESADO COINCIDE EN LA LISTA DE NT\n")
                                elif terminal in listaTemporal_Terminales:
                                    os.system('cls')
                                    print("\nERROR! EL TERMINAL INGRESADO YA EXISTE\n")
                                else:
                                    os.system('cls')
                                    listaTemporal_Terminales.append(terminal)

                            for x in listaTemporal_Terminales:
                                print(x)
                            
                        elif opcion2==3:
                            os.system('cls')
                            print("Ingresando NT inicial a: "+nombre_Gramatica+"\n")
                            Inicial = input("Estado inicial: ")
                               
                            if Inicial in listaTemporal_NT: #SI EL NT EXISTE EN LA LISTA DE NT OMITIR
                                NT_Inicial = Inicial
                            else: #SI NO EXISTE VACIAR LA VARIABLE Y MOSTRAR EL ERROR
                                NT_Inicial=""
                                print("\nEL NT INGRESADO NO EXISTE NE LA LISTA DE NT")

                            print(NT_Inicial)
                                
                        elif opcion2==4:
                            existe=False
                            os.system('cls')
                            print("Ingresando producciones a: "+nombre_Gramatica+"\n")
                            print("NOTA: La notacion correcta para ingresar una produccion es \"A>a B\"")
                            print("      Tome en cuenta el espacio del lado derecho de la produccion\n")
                            produccion = input("Produccion No."+str(contador4G)+": ") # A>a B
                            separacion1=produccion.split(">") #[ "A","a B" ]
                            separacion2=separacion1[1].split(" ") # [ "a" , "B" ]

                            #AGREGANDO ESTADOS DE ACEPTACION
                            if separacion1[1].upper()=="EPSILON":
                                listaTemporal_EstadosAceptacionG.append(separacion1[0])
                                print("Se agrego a "+separacion1[0]+" como estado de aceptacion")
                            else:
                                estado_De = separacion1[0]
                                estado_Hacia = separacion2[1]
                                simbolo=separacion2[0]

                                #VERIFICANDO SI EXISTE EL ESTADO_DE EN LA LISTA 
                                for x in range(0, len(listaTemporal_Producciones)):
                                    if estado_De==listaTemporal_Producciones[x].nombre:
                                        existe=True
                                    else:
                                        continue

                                #SI EXISTE BUSCA EL ESTADO Y SOLO AGREGAR LA PRODUCCION
                                if existe==True:
                                    if buscarSimbolo(separacion1[0],listaTemporal_Producciones,separacion2[0]):
                                        print("La produccion ingresada es ambigua (Repite simbolo desde un mismo estado)")
                                        contador4G=contador4G-1
                                    else:
                                        print("El estado "+estado_De+" Ya existe")
                                        buscarEstado(estado_De,listaTemporal_Producciones).definirTransicion(estado_Hacia,simbolo)
                                #SINO EXISTE, CREAR UN NUEVO ESTADO Y AGREGAR LA PRODUCCION
                                else: 
                                    print("El estado "+estado_De+" No existe")
                                    estadoTemporal=Estado()
                                    estadoTemporal.agregarNombre(estado_De)
                                    estadoTemporal.definirTransicion(estado_Hacia,simbolo)

                                    listaTemporal_Producciones.append(estadoTemporal)

                            contador4G+=1

                            #mostrarLista(listaTemporal_Producciones)
                            #print("ESTADOS DE ACEPTACION")
                            #print(listaTemporal_EstadosAceptacionG)



                            #TERMINA INGRESAR PRODUCCIONES
                        
                        elif opcion2==5:
                            os.system('cls')
                            print("Mostrando gramatica transformada...")
                        
                        elif opcion2==6:
                            os.system('cls')
                            ayuda()
                       
                        elif opcion2==7:
                            os.system('cls')
                            break
                       
                        elif opcion2==8:
                            confirmar= input("\n Esta seguro que quiere guardar la gramatica ")
                            if confirmar.upper()=="SI":
                                os.system('cls')
                                #CREANDO OBJETO GRAMATICA
                                gramatica_Temporal=GramaticaRegular(nombre_Gramatica,listaTemporal_NT,
                                listaTemporal_Terminales,NT_Inicial,listaTemporal_Producciones,listaTemporal_EstadosAceptacionG)
                                #AGREGANDO A LA LISTA GRAMATICAS
                                listaGramaticas.append(gramatica_Temporal)

                                #GUARDANDO SU AFD CORRESPONDIENTE

                                AFD_Temporal=Automata(temp,listaTemporal_NT,listaTemporal_Terminales,NT_Inicial,
                                listaTemporal_EstadosAceptacionG,listaTemporal_Producciones)
                                #AGREGANDO A LA LISTA DE AFD
                                listaAutomatas.append(AFD_Temporal)

                                print("Gramatica guardada con exito")
                                os.system('cls')
                                break
                            
                            elif confirmar.upper()=="NO":
                                os.system('cls')
                                print("Proceso cancelado")
                            else:
                                os.system('cls')
                                print("Opcion NO VALIDA")
                                print("Escriba -SI- o -NO-")

                        else:
                            os.system('cls')
                            print ("La opcion seleccionada no existe")
                        # TERMINA LA OPCION DE CREAR GRAMATICA
            #TERMINA CREAR GRAMATICA          

            elif opcion == 3:
                os.system('cls')
                Nombre_gramatica_Oringinal=input("Ingrese el nombre de la gramatica: ")
                Nombre_gramatica=Nombre_gramatica_Oringinal+" Gramatica"
                nombreAFD = Nombre_gramatica_Oringinal+" AFD"
                

                while True:
                    print("\n\n---------->>> Se encuentra en el MENU EVALUAR CADENAS <<<----------")
                    print("1. Solo validar")
                    print("2. Ruta en AFD")
                    print("3. Expandir con gramatica")
                    print("4. Ayuda")
                    print("5. Salir")
                    opcion3=int(input("Ingrese una opcion "))

                    if opcion3==1:
                        os.system('cls')
                        ObjetoGramatica = buscar_Gramatica(Nombre_gramatica)

                        cadena = input("Ingrese la cadena a evaluar: ")

                        Verifica_Cadena(ObjetoGramatica.NT_Inicial,cadena,ObjetoGramatica.No_Terminales,
                        ObjetoGramatica.producciones,ObjetoGramatica.estadosAceptacion)

                        #GUARDANDO CADENAS EVALUADAS
                        
                        ObjetoGramatica.Cadenas_Evaluadas.append(Verifica_Cadena_Retorna(ObjetoGramatica.NT_Inicial,cadena,ObjetoGramatica.No_Terminales,
                        ObjetoGramatica.producciones,ObjetoGramatica.estadosAceptacion))

                        #for x in ObjetoGramatica.Cadenas_Evaluadas:
                        #    print(x)
                        
                    elif opcion3==2:
                        os.system('cls')
                        print("Evaluando en ruta AFD...")
                        ObjetoAFD = buscar_AFD(nombreAFD)

                        cadena = input("Ingrese la cadena a evaluar: ")

                        print()
                        print("Ruta en AFD:  ", end="")
                        Ruta_AFD(ObjetoAFD.estado_Inicial,cadena,ObjetoAFD.estados,ObjetoAFD.transiciones,
                        ObjetoAFD.estados_Aceptacion)


                    elif opcion3==3:
                        os.system('cls')
                        print("Expandiendo gramatica...")
                        objetoG= buscar_Gramatica(Nombre_gramatica)

                        cadena= input("Ingrese la cadena a evaluar: ")

                        print(objetoG.NT_Inicial, end="")
                        Expande_Gramatica(objetoG.NT_Inicial,cadena,objetoG.No_Terminales,
                        objetoG.producciones,objetoG.estadosAceptacion)

                        
                    elif opcion3==4:
                        os.system('cls')
                        ayuda()
                    elif opcion3==5:
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                        print ("La opcion seleccionada no existe")
                    # TERMINA LA OPCION DE EVALUAR CADENAS
            #TERMINA EVALUAR CADENA
            
            elif opcion == 4:
                os.system('cls') 
                print("Reportess")
                nombre = input("Ingrese el nombre de la gramatica o AFD: ")
                nombreAFD = nombre+" AFD"
                nombreGramatica= nombre+" Gramatica"

                ObjetoAFD = buscar_AFD(nombreAFD)
                ObjetoGramatica = buscar_Gramatica(nombreGramatica)

                while True:
                    print("\n---------->>> Se encuentra en el MENU REPORTES <<<----------")
                    print("1. Ver detalle")
                    print("2. Generar reporte")
                    print("3. Ayuda")
                    print("4. Salir")
                    opcionReportes = input("Ingrese una opcion: ")

                    if verificar_Lista_Vacia(str(opcionReportes))==True: #ESTA VACIA
                        os.system('cls')
                        print("********* Debe ingresar una opcion valida, intente nuevamente *********")
                    else:
                        opcionReportes=int(opcionReportes)

                        if opcionReportes == 1:
                            os.system('cls')
                            print("\n\nMostrando detalles....")

                            #MOSTRANDO AFD
                            print()
                            print("--- "+nombreAFD+" ---")
                            print("ESTADOS")
                            print(ObjetoAFD.estados)
                            print("ALFABETO")
                            print(ObjetoAFD.alfabeto)
                            print("ESTADO INICIAL")
                            print(ObjetoAFD.estado_Inicial)
                            print("ESTADOS DE ACEPTACION")
                            print(ObjetoAFD.estados_Aceptacion)
                            print("TRANSICIONES")
                            mostrarLista(ObjetoAFD.transiciones)

                            #MOSTRANDO GRAMATICA
                            print()
                            print("--- "+nombreGramatica+" ---")
                            print("NO TERMINALES")
                            print(ObjetoGramatica.No_Terminales)
                            print("TERMINALES")
                            print(ObjetoGramatica.terminales)
                            print("NT INICIAL")
                            print(ObjetoGramatica.NT_Inicial)
                            print("PRODUCCIONES")
                            mostrarLista(ObjetoGramatica.producciones)
                            
                            #BUSCAR LA GRAMATICA Y AFD CORRESPONDIENTE AL NOMBRE INGRESADO


                        if opcionReportes == 2:
                            #GENERANDO GRAPHVIZ
                            f = Digraph('finite_state_machine', filename='fsm.gv', format="png")
                            f.attr(rankdir='LR', size='8,5')

                            f.attr('node', shape='doublecircle')
                            for estadoAceptacion in ObjetoGramatica.estadosAceptacion: 
                                f.node(estadoAceptacion)

                            f.attr('node', shape='circle')                                

                            for z in ObjetoGramatica.producciones:
                                estadoDe=z.get_Nombre()
                                for p in z.transiciones:
                                    f.edge(estadoDe.strip(), (p.get_Estado_Hacia()).strip(), label=(p.get_Simbolo()).strip())
                                
                            f.node("invisible", style="invis")
                            f.edge("invisible", ObjetoAFD.estado_Inicial)

                            f.view()


                            #REPORTE PDF
                            pdf = canvas.Canvas("Reporte.pdf") #CREA EL DOCUMENTO PDF
                            pdf.setFillColor(red)
                            pdf.setFont("Courier-BoldOblique",18)
                            pdf.drawString(50,800,"REPORTE DE -- "+nombre.upper()+" --")
                            pdf.setFillColor(blue)
                            pdf.setFont('Times-Bold',14)
                            pdf.drawString(50,770,"Gramática")
                            pdf.setFont("Times-Bold",12)
                            pdf.setFillColor(black)

                            #NO TERMINALES
                            pdf.drawString(80,750,"No Terminales:")
                            contadorNT=180
                            for t in ObjetoGramatica.No_Terminales:
                                pdf.drawString(contadorNT,750,t+", ")
                                contadorNT=contadorNT+15
                            
                            #TERMINALES
                            pdf.drawString(80,730,"Terminales:")
                            contadorT=180
                            for t in ObjetoGramatica.terminales:
                                pdf.drawString(contadorT,730,t+", ")
                                contadorT=contadorT+15

                            #INICIO
                            pdf.drawString(80,710, "Inicio:")
                            pdf.drawString(180,710,ObjetoGramatica.NT_Inicial)

                            #PRODUCCIONES
                            pdf.drawString(80,690, "Producciones:")
                            contadorYP=690
                            for estado in ObjetoGramatica.producciones:
                                contadorXP=180

                                for transicion in estado.transiciones:
                                    pdf.drawString(contadorXP,contadorYP,estado.get_Nombre())
                                    pdf.drawString(contadorXP+10,contadorYP,"→")
                                    pdf.drawString(contadorXP+28,contadorYP,transicion.get_Simbolo())
                                    pdf.drawString(contadorXP+38,contadorYP,transicion.get_Estado_Hacia())
                                    contadorXP+=70
                                    
                                contadorYP-=15   




                            pdf.setFillColor(blue)
                            pdf.setFont('Times-Bold',14)
                            pdf.drawString(50,450,"AFD")
                            pdf.setFont("Times-Bold",12)
                            pdf.setFillColor(black)

                            #ALFABETO
                            pdf.drawString(80,430,"Alfabeto:")
                            contadorA=180
                            for t in ObjetoAFD.alfabeto:
                                pdf.drawString(contadorA,430,t+", ")
                                contadorA=contadorA+15    

                            #ESTADOS
                            pdf.drawString(80,410,"Estados:")
                            contadorE=180
                            for t in ObjetoAFD.estados:
                                pdf.drawString(contadorE,410,t+", ")
                                contadorE=contadorE+15
                            
                            #INICIO
                            pdf.drawString(80,390, "Inicio:")
                            pdf.drawString(180,390,ObjetoAFD.estado_Inicial)

                            #ESTADOS DE ACEPTACION
                            pdf.drawString(80,370,"Estados de aceptacion:")
                            contadorEA=210
                            for t in ObjetoAFD.estados_Aceptacion:
                                pdf.drawString(contadorEA,370,t+", ")
                                contadorEA+=15

                            pdf.drawImage('fsm.gv.png',50,150,400,200)


                            #CADENAS EVALUADAS
                            #pdf.drawString(80,50,"Cadenas evaluadas")
                            contadorYCadena=30
                            pdf.drawString(50,100,"Cadenas evaluadas")
                            for cadena in ObjetoGramatica.Cadenas_Evaluadas:
                                pdf.drawString(80,contadorYCadena,cadena+" ")
                                contadorYCadena+=10
                            pdf.save()

                        if opcionReportes == 3:
                            os.system('cls')
                            ayuda()

                        if opcionReportes == 4:
                            os.system('cls')
                            break                    
            #TERMINA REPORTES
            
            elif opcion ==5:
                os.system('cls') 
                print("Cargando archivo AFD")

                leerArchivoAFD()
            #TERMINA CARGAR ARCHIVO AFD
            
            elif opcion==6:
                os.system('cls') 
                print("Cargando archivo gramatica")
                leerArchivoGramatica()
            #TERMINA CARGAR ARCHIVO GRAMATICA
            
            elif opcion ==7:
                os.system('cls') 
                print("FIN del programa")
                break
            #FIN DEL PROGRAMA

            elif opcion == 8:
                os.system('cls')


                while True:
                    print("---------->>> Se encuentra en el menu GRAMATICA TIPO2 Y AP <<<----------")
                    print("1. Ingresar / Modificar gramatica ")
                    print("2. Generar automata de pila")
                    print("3. Visualizar automata")
                    print("4. Validar cadena")
                    print("5. Salir")
                    opcion8 = input("Ingrese una opcion: ")

                    #SI LA OPCION ESTA VACIA
                    if verificar_Lista_Vacia(str(opcion8)) == True:
                        os.system('cls')
                        print("********* Debe ingresar una opcion valida, intente nuevamente *********")
                    else:
                        opcion8 = int(opcion8)

                        if opcion8 == 1:
                            os.system('cls')

                            contador1G2 = 1
                            contador2G2 = 1
                            lista_TerminalesG2 = []
                            lista_NoTerminalesG2 = []


                            nombre_Original = input("Ingrese el nombre de la gramatica tipo2: ")
                            while verificar_Lista_Vacia(nombre_Original)==True:
                                os.system('cls') 
                                print("\n--------- DEBE INGRESAR UN NOMBRE VALIDO ---------")
                                nombre_Original = input("Ingrese el nombre del AFD: ")

                            nombre_GramaticaTipo2 = nombre_Original+" Gramatica"


                            while True:                               
                                print("---------->>> Se encuentra en el menu INGRESAR / MODIFICAR GRAMATICA <<<----------")
                                print("1. Ingresar terminales")
                                print("2. Ingresar no terminales")
                                print("3. Ingresar producciones")
                                print("4. Borrar producciones")
                                print("5. No terminal inicial")
                                print("6. Salir")
                                print("7. Guardar gramatica tipo2")
                                respusta = input("Ingrese una opcion: ")

                                if verificar_Lista_Vacia(str(respusta))==True:
                                    os.system('cls')
                                    print("\n********* Debe ingresar una opcion valida, intente nuevamente *********")

                                else:
                                    respusta = int(respusta)
                                    if respusta == 1:
                                        os.system('cls')
                                        print("Ingresando terminales a: "+nombre_Original+"\n")
                                        terminal = input("Terminal No."+str(contador1G2)+": ")

                                        if verificar_Lista_Vacia(terminal) == True:
                                            print("\n******** DEBE INGRESAR UN TERMINAL VALIDO, INTENTE NUEVAMENTE ********")
                                        elif (terminal.isdigit()) == False: # SI ES LETRA
                                            if terminal == terminal.upper(): # SI ES MAYUSCULA
                                                print("\n******** EL TERMINAL NO PUEDE CONTENER LETRAS MAYUSCULAS ********")
                                            else:
                                                lista_TerminalesG2.append(terminal)
                                                contador1G2+=1
                                        else:
                                            lista_TerminalesG2.append(terminal)
                                            contador1G2+=1
                                            
                                        print(lista_TerminalesG2)

                                        # TERMINA INGRESAR TERMINALES

                                    elif respusta == 2:
                                        os.system('cls')
                                        print("Ingresando no terminales a:"+nombre_Original+"\n")
                                        No_Terminal = input("No Terminal No."+str(contador2G2)+": ")

                                        if verificar_Lista_Vacia(No_Terminal) == True:
                                            print("\n******** DEBE INGRESAR UN NO TERMINAL VALIDO, INTENTE NUEVAMENTE ********")
                                        elif No_Terminal[0] == No_Terminal[0].upper(): # SI EMPIEZA CON LETRA MAYUSCULA
                                            lista_NoTerminalesG2.append(No_Terminal)
                                            contador2G2+=1
                                            
                                        else:
                                            print("EL NO TERMINAL NO ES VALIDO, DEBE INICIAR CON LETRA MAYUSCULA")
                                        
                                        print(lista_NoTerminalesG2)
                                        # TERMINA INGRESAR NO TERMINALES

                                    elif respusta == 3:
                                        os.system('cls')
                                        print("Ingresando producciones")
                                        # TERMINA INGRESAR PRODUCCIONES

                                    elif respusta == 4:
                                        os.system('cls')
                                        print("Borrando producciones")
                                        # TERMINA BORRAR PRODUCCIONES

                                    elif respusta == 5:
                                        os.system('cls')
                                        print("Ingresando no terminal")
                                        # TERMINA INGRESAR NO TERMINAL                                        

                                    elif respusta == 6:
                                        os.system('cls')
                                        break
                                        # SALIR

                                    else:
                                        os.system('cls')
                                        print("La opcion seleccioanda no existe")


                        elif opcion8 == 5:
                            os.system('cls')
                            break

                        else:
                            os.system('cls') 
                            print ("La opcion seleccionada no existe")

            elif opcion == 9:
                os.system('cls')
                print("\n\n-------- AUTOMATAS --------")
                mostrar_Lista_Automatas()
                print("\n\n-------- GRAMATICAS --------")
                mostrar_Lista_Gramaticas()
            

            else:
                os.system('cls') 
                print ("La opcion seleccionada no existe")
            #OPCION INCORRECTA

caratula()
menu()

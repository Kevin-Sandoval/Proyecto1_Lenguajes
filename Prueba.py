from reportlab.pdfgen import canvas
from graphviz import Digraph

q = canvas.Canvas("hola.pdf")
q.drawString(100,750,"Hola mundo pdf!")
q.save()



def prueba():
    cadena="10101"

    inicio="A"
    finalizar="A"
    actual=inicio

    fin = False
    contador= 0

    while contador<(len(cadena)):
        print(contador)
        if actual=="A":
            print("Esta aqui1")

            if cadena[contador]=="1":
                actual="A"
                print("A-1=A")
            if cadena[contador]=="0":
                actual="B"
                print("A-0=B")
            contador= contador+1
            continue
        #TERMINA PRIMERA TRANSICION
        if actual=="B":
            print("Esta aqui2")
            if cadena[contador]=="1":
                actual="B"
                print("B-1=B")
            if cadena[contador]=="0":
                actual="A"
                print("B-0=A")
            contador= contador+1
            continue
        
    if actual==finalizar:
        print("CADENA CORRECTA")
    else:
        print("CADENA INCORRECTA")

class Estado():
    nombre=""
    transiciones=[]

    def __init__(self):
        self.nombre=""
        self.transiciones=[]
  
    def __str__(self):
        return self.nombre

    def agregarNombre(self,n):
        self.nombre=n

    def definirTransicion(self,hacia,simbolo):
        transicion_Temporal=Transicion()
        transicion_Temporal.Estado=hacia
        transicion_Temporal.simbolo=simbolo
        self.transiciones.append(transicion_Temporal)

    def getNombre(self):
        return self.nombre
    
    def getTransiciones(self):
        for x in self.transiciones:
            print(x)
    
class Transicion():
    #Estado=""
    #simbolo=""

    def __init__(self):
        self.Estado=""
        self.simbolo=""

    def __str__(self):
        return "Estado hacia: "+self.Estado+" Simbolo: "+self.simbolo

    def retornarSimbolo(self,objeto):
        objeto=Transicion()
        return objeto.simbolo

    def getEstado(self):
        return self.Estado

    def getSimbolo(self):
        return self.simbolo

def pruebaEvaluarCadenas():
    transiciones=[]
    estados=["A","B"]


    #ESTADOS
    estado1=Estado()
    estado2=Estado()

    estado1.agregarNombre("A")
    estado2.agregarNombre("B")

    #AGREGANDO TRANSICIONES
    estado1.definirTransicion("A","1")
    estado1.definirTransicion("B","0")

    estado2.definirTransicion("B","1")
    estado2.definirTransicion("A","0")

    transiciones.append(estado1)
    transiciones.append(estado2)


    #FUNCION QUE BUSCA EL ESTADO-DE EN LA LISTA DE PRODUCCIONES, RETORNA TRUE SI EXISTE DE LO CONTRARIO FALSE
    def verficar_Existencia_Estado_De_Retornar_Boolean(nombreEstadoDe,listaGeneral):
        existe=False
        for estado in listaGeneral:
            if nombreEstadoDe == estado.getNombre():
                #EL ESTADO SI EXISTE
                existe=True
            else:
                continue
        return existe

    def verficar_Existencia_Estado_De_Retornar_Objeto(nombreEstadoDe,listaGeneral):
        estadoTem=Estado()
        for estado in listaGeneral:
            if nombreEstadoDe == estado.getNombre():
                #EL ESTADO SI EXISTE
                estadoTem=estado
            else:
                continue
        return estadoTem

    #FUNCION QUE BUSCA EL ESTADO-DE EN LA LISTA DE PRODUCIONES, SI EXISTE RETORNA LA LISTA 
    # CON ESTADO-HACIA Y SIMBOLO
    def verificar_Existencia_Estado_De_Retornar_listaTrans(nombreEstadoDe, listaGeneral):
        listaAux=[]
        for estado in listaGeneral:
            if nombreEstadoDe== estado.getNombre():
                listaAux=estado.transiciones
            else:
                continue
        return listaAux

    #FUNCION QUE VERIFICA SI EXISTE EL SIMBOLO "X" EN LA LISTA DE TRANSICIONES DEL OBJETO ESTADO
    def verificar_Existencia_Simbolo_En_EstadoH_Hacia(nombreEstadoDe,simbolo,listaGeneral):
        existe=False
        listaAuxTransicionesEstado=verificar_Existencia_Estado_De_Retornar_listaTrans(nombreEstadoDe,listaGeneral)
    
        for x in listaAuxTransicionesEstado:# [Transicion1, Transicion2]
            a=x.getEstado()
            b =x.getSimbolo()
            if (b==simbolo) and (a in estados):
                existe=True
            else:
                continue  
        return existe

    def nueva(nombreEstadoDe,simbolo,listaGeneral):
        nuevo=""
        listaAuxTransicionesEstado=verificar_Existencia_Estado_De_Retornar_listaTrans(nombreEstadoDe,listaGeneral)
        for x in listaAuxTransicionesEstado:# [Transicion1, Transicion2]
            a=x.getEstado()
            b =x.getSimbolo()
            if (b==simbolo) and (a in estados):
                existe=True
                nuevo=a
            else:
                continue  
        return nuevo

    print(verificar_Existencia_Simbolo_En_EstadoH_Hacia("A","0",transiciones))

    nombre="Prueba"
    alfabeto= ["1","0"]
    estado_Inicial="A"
    estadosAceptacion="A"

    #DEFINIENDO LA GRAMATICA
    AF = Automata(nombre,estados,alfabeto,estado_Inicial,estadosAceptacion,transiciones)

    inicio="A"
    finalizar="A"
    actual=inicio
    cadena=input("Ingrese la cadena a evaluar: ")

    fin = False
    contador=0
    while fin ==False:

        if contador > (len(cadena)-1):
            fin =True
            break
        else:
            print("-----Contador----- = "+str(contador))
            if actual in estados:
                if verficar_Existencia_Estado_De_Retornar_Boolean(actual,transiciones)==True: # EXISTE
                    #for estado in estados:
                    if verificar_Existencia_Simbolo_En_EstadoH_Hacia(actual,cadena[contador],transiciones)==True: #existe el simbolo
                        actual=nueva(actual,cadena[contador],transiciones)
                
        
            contador=contador+1
            print("ACTUAL: "+actual)
            print()
        #continue




    if actual==finalizar:
        print("CADENA CORRECTA")
    else:
        print("CADENA INCORRECTA")


def modo2():
    lista_Alfabeto = []
    lista_Estados_De = []
    lista_Temporal = []
    lista_Transiciones = []

    cadena1 = "[a,b]"
    cadena2 = "[A,B,C,D]"
    cadena3 = "[A,C;A,C;B,D;-,-]"

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

 



    #Estados = ['A','B','C']
    #alfabeto = ['1','0']






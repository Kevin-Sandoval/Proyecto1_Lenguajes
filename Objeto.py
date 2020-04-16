
# CLASE GRAMATICA
class GramaticaRegular():
    def __init__(self,nombre,No_Terminales,terminales,NT_Inicial,producciones,estadosAceptacion):
        self.nombre=nombre
        self.No_Terminales=No_Terminales
        self.terminales=terminales
        self.NT_Inicial=NT_Inicial
        self.producciones=producciones
        self.estadosAceptacion=estadosAceptacion
        self.Cadenas_Evaluadas = []
        


#CLASE AUTOMATA
class Automata():
    def __init__(self,nombre,estados,alfabeto,estado_Inicial,estados_Aceptacion,transiciones):
        self.nombre = nombre
        self.estados = estados
        self.alfabeto = alfabeto
        self.estado_Inicial=estado_Inicial
        self.estados_Aceptacion =estados_Aceptacion
        self.transiciones=transiciones
        self.Cadenas_Evaluadas = []

    def editar_ListaEstados(self,nuevaLista):
        self.estados = nuevaLista
        


#CLASE ESTADO-DE: SE UTILIZA PARA GUARDAR LAS PRODUCCIONES O TRANSICIONES DE UNA GRAMATICA
# O UN AUTOMATA
class Estado():
    def __init__(self):
        self.nombre=""
        self.transiciones=[]
   
    def __str__(self):
        return self.nombre

    def agregarNombre(self,nombre):
        self.nombre=nombre

    def definirTransicion(self,hacia,simbolo):
        transicion_Temporal=Transicion()
        transicion_Temporal.Estado=hacia
        transicion_Temporal.simbolo=simbolo  
        self.transiciones.append(transicion_Temporal)

    def get_Nombre(self):
        return self.nombre

    def get_Transiciones(self):
        for x in self.transiciones:
            print(x)

#CLASE TRANSICION: GUARDA EL NOMBRE DEL ESTADO HACIA DONDE SE DIRIGE LA TRANSICION 
# CON SU SIMBOLO, ESTE OBJETO LE PERTENECE A UN ESTADO-DE 
class Transicion():
    def __init__(self):
        self.Estado=""
        self.simbolo=""

    def __str__(self):
        return "Hacia : "+self.Estado+" Con : "+self.simbolo

    def get_Estado_Hacia(self):
        return self.Estado
    
    def get_Simbolo(self):
        return self.simbolo





def modo2(listaTransiciones):
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


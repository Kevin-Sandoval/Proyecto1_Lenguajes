from Objeto import Estado
from Objeto import Transicion

#FUNCION QUE BUSCA EN LA LISTA DE TRANSICIONES EL ESTADO-DE, RETORNA TRUE SI EXISTE
def Existe_EstadoDe_Boolean(nombre_EstadoDe,lista_General):
    existe = False
    for estadoDe in lista_General:
        if nombre_EstadoDe == estadoDe.get_Nombre(): #SI EXISTE EL ESTADO-DE
            existe = True
        else:
            continue
    return existe

#FUNCION QUE BUSCA EN LA LISTA DE TANSICIONES EL ESTADO-DE, RETORNA LA LISTA 
# INTERNA DE TRANSICIONES SI EXISTE
def Existe_EstadoDe_ListaTransiciones(nombre_EstadoDe, lista_General):
    lista_Aux=[]
    for estadoDe in lista_General:
        if nombre_EstadoDe == estadoDe.get_Nombre():
            lista_Aux = estadoDe.transiciones
        else: 
            continue
    return lista_Aux

#FUNCION QUE BUSCA EL SIMBOLO EN LA LISTA DE TRANSICIONES DEL ESTADO-DE, RETORNA TRUE SI EXISTE
def Existe_Simbolo_En_EstadoHacia(nombre_EstadoDe,simbolo,lista_General,lista_Estados):
    existe = False
    lista_Aux_Transiciones = Existe_EstadoDe_ListaTransiciones(nombre_EstadoDe,lista_General)

    for x in lista_Aux_Transiciones:
        estado_Hacia = x.get_Estado_Hacia()
        simbolo_EstadoHacia = x.get_Simbolo()

        if (simbolo_EstadoHacia == simbolo) and (estado_Hacia in lista_Estados):
            existe = True
        else:
            continue
    return existe 

#FUNCION QUE BUSCA EL SIMBOLO EN LA LISTA DE TRANSICIONES DEL ESTADO-DE, RETORNA EL ESTADO-HACIA
def Existe_Simbolo_En_EstadoHacia_Estado_Hacia(nombre_EstadoDe,simbolo,lista_General,lista_Estados):
    nombre_Estado_Hacia=""

    lista_Aux_Transiciones = Existe_EstadoDe_ListaTransiciones(nombre_EstadoDe,lista_General)

    for x in lista_Aux_Transiciones:
        estado_Hacia = x.get_Estado_Hacia()
        simbolo_EstadoHacia = x.get_Simbolo()

        if (simbolo_EstadoHacia == simbolo) and (estado_Hacia in lista_Estados):
            nombre_Estado_Hacia = estado_Hacia
        else:
            continue
    return nombre_Estado_Hacia

#METODO QUE EVALUA UNA CADENA
def Expande_Gramatica(estado_Inicio,cadena_A_Evaluar, lista_Estados,lista_General_Transiciones, lista_Estados_Aceptacion):
    inicio = estado_Inicio
    actual = inicio

    cadena = cadena_A_Evaluar

    fin = False
    contador = 0

    gramaticaExpandida=""

    while fin == False:

        if contador > (len(cadena)-1):
            fin = True
            break

        else:
            #gramaticaExpandida.replace(actual,"")

            if actual in lista_Estados:
                if Existe_EstadoDe_Boolean(actual, lista_General_Transiciones) == True:
                    if Existe_Simbolo_En_EstadoHacia(actual, cadena[contador], lista_General_Transiciones, lista_Estados):
                        actual = Existe_Simbolo_En_EstadoHacia_Estado_Hacia(actual, cadena[contador], lista_General_Transiciones,lista_Estados)                        
                        gramaticaExpandida=gramaticaExpandida+""+cadena[contador]



            contador = contador+1
            print("-->"+gramaticaExpandida+""+actual,end="")
            

    if actual in lista_Estados_Aceptacion:
        print("--- CADENA CORRECTA ---")
    else:
        print("--- CADENA INCORRECTA ---")

 

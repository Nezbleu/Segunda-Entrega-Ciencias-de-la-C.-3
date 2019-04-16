from pila import *
from arbol import *
import os

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)

def leerArchivo():
    return[x.split() for x in open("expresiones.in.txt").readlines()]
    
lista = leerArchivo()

file = open("expresiones.out.txt", "w")

for i in range(0, len(lista)):
    pila = Pila()
    convertir(lista[i], pila)
    file.write(str(evaluar(pila.desapilar())) + os.linesep)
    
file.close()



#*
# Implementar un algoritmo que dado un árbol Trie T, un patrón p (prefijo) y un entero n, 
# escriba todas las palabras del árbol que empiezan por p y sean de longitud n. 
# #

from tp_trie import *

def recorrer(trie):
    palabras = []
    recorrer_recursivo(trie.root, "", palabras)
    return palabras

def recorrer_recursivo(nodo_trie, prefijo, lista_palabras):
    if nodo_trie.isEndOfWord == True:
        lista_palabras.append(prefijo)
    
    for nodo_hijo in nodo_trie.children:
        recorrer_recursivo(nodo_hijo, prefijo + nodo_hijo.key, lista_palabras)

def escribir_palabras_bajo_condicion(palabras, prefijo, entero):
    palabras_con_prefijo = []
    # Añado todas las palabras que comienzan con prefijo en otra lista
    for palabra in palabras:
        if prefijo in palabra:
            palabras_con_prefijo.append(palabra)
    
    for palabra in palabras_con_prefijo:
        if len(palabra) == entero:
            print("Palabra que comienza con prefijo: ", prefijo, " y de longitud: ", entero, "\nPalabra: ", palabra, "\n")
        else:
            print("La palabra: ", palabra, " no cumple con el requisito de longitud.", "\n")
    return

# Ejemplo de uso
trie = Trie()
insert(trie ,"hola")
insert(trie ,"holanda")
insert(trie ,"holandés")
insert(trie ,"perro")
lista_palabras1 = recorrer(trie)
escribir_palabras_bajo_condicion(lista_palabras1, "ho", 4)
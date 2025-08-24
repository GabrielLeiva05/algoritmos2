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

def buscar_inversa(palabras):
    for palabra in palabras:
        palabra_inversa = palabra[::-1]
        if palabra_inversa in palabras:
            print("Se encontró palabra inversa.\nPalabra original: ", palabra, "\nPalabra inversa: ", palabra_inversa, "\n")
            # Saco las palabras de la lista para que no se impriman dos veces.
            palabras.remove(palabra)
            palabras.remove(palabra_inversa)
    return

# Ejemplo de uso
trie = Trie()
insert(trie ,"hola")
insert(trie ,"holanda")
insert(trie ,"aloh")
insert(trie ,"perro")

lista_palabras = recorrer(trie)
buscar_inversa(lista_palabras)
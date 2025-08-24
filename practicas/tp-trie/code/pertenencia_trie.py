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

def buscar_pertenencia(trie1, trie2):
    pertenencia = False
    for palabra1 in trie1:
        for palabra2 in trie2:
            if palabra1 == palabra2:
                # Con que una palabra ya pertenezca al otro trie, decimos que pertenece
                pertenencia = True
    return pertenencia

# Ejemplo de uso
trie = Trie()
trie2 = Trie()
insert(trie ,"hola")
insert(trie ,"holanda")
insert(trie ,"aloh")
insert(trie ,"perro")
insert(trie2 ,"hol")
insert(trie2 ,"holand")
insert(trie2 ,"alo")
insert(trie2 ,"perro")

lista_palabras1 = recorrer(trie)
lista_palabras2 = recorrer(trie2)

if buscar_pertenencia(lista_palabras1, lista_palabras2):
    print("El trie 1 pertenece al trie 2")
else:
    print("El trie 1 no pertenece al trie 2")
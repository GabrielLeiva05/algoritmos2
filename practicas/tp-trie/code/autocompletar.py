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

def autocompletar(palabras, prefijo):
    palabras_con_prefijo_inicial = []
    # Agrego las palabras que comienzan con ese prefijo a otra lista.
    for palabra in palabras:
        if prefijo in palabra:
            palabras_con_prefijo_inicial.append(palabra)
    # Si hay palabras con ese prefijo en la lista seguimos, sino cortamos.
    if palabras_con_prefijo_inicial != []:
        sufijo_candidato = palabras_con_prefijo_inicial[0][len(prefijo):]
    else:
        return 
    
    for palabra in palabras_con_prefijo_inicial:
        sufijo_a_comparar = palabra[len(prefijo):]
        sufijo_comun = ""
        # Uso zip para que si un sufijo es más largo en longitud que el otro, no siga buscando comparaciones. 
        # Se corta cuando el sufijo menor se queda sin caracteres.
        for letra1, letra2  in zip(sufijo_candidato, sufijo_a_comparar):
            if letra1 == letra2:
                sufijo_comun += letra1
        sufijo_candidato = sufijo_comun
    return sufijo_candidato

# Ejemplo de uso
trie = Trie()
trie2 = Trie()
insert(trie ,"hola")
insert(trie ,"holanda")
insert(trie ,"holandés")
insert(trie ,"perro")
insert(trie2 ,"chau")
insert(trie2 ,"que")
insert(trie2 ,"paso")
insert(trie2 ,"gano")
lista_palabras1 = recorrer(trie)
lista_palabras2 = recorrer(trie2)
print(autocompletar(lista_palabras1, "h"))
print(autocompletar(lista_palabras2, "hol"))
class TrieNode():
    def __init__(self, parent = None ,key = None):
        self.parent = parent
        self.key = key
        self.children = []
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

def insert(trie, elemento):
    nodo_actual = trie.root
    for key_actual in elemento:
        hijo_encontrado = None
        for hijo_actual in nodo_actual.children:
            if key_actual == hijo_actual.key:
                hijo_encontrado = hijo_actual
        if hijo_encontrado is not None:
            nodo_actual = hijo_encontrado
        else:
            nodo_nuevo = TrieNode(parent = nodo_actual, key = key_actual)
            nodo_actual.children.append(nodo_nuevo)
            nodo_actual = nodo_nuevo
    nodo_actual.isEndOfWord = True
    return

def search(trie, elemento):
    nodo_actual = trie.root
    for key_actual in elemento:
        hijo_encontrado = None
        for hijo_actual in nodo_actual.children:
            if key_actual == hijo_actual.key:
                hijo_encontrado = hijo_actual
        if hijo_encontrado is not None:
            nodo_actual = hijo_encontrado
        else:
            return False
    return nodo_actual.isEndOfWord

def delete(trie, elemento):
    nodo_actual = trie.root
    for key_actual in elemento:
        hijo_encontrado = None
        for hijo_actual in nodo_actual.children:
            if hijo_actual.key == key_actual:
                hijo_encontrado = hijo_actual
        if hijo_encontrado is not None:
            nodo_actual = hijo_encontrado
        else:
            #*  
            #  caso en el que no se encuentra un elemento en el trie
            #  Va a haber uno o mas nodos que no tengan algun caracter
            #  del elemento. 
            # #
            return False
    if nodo_actual.isEndOfWord == False:
        return False
    
    #*
    # caso en el que la palabra es un prefijo y se desmarca 
    # la bandera de fin de palabra. Se devuelve True al final
    # #
    
    nodo_actual.isEndOfWord = False
    
    #*
    # caso en el que se borran todos los nodos porque ninguna parte
    # del elemento contiene a otro y
    # caso en el que se borran los nodos hasta la primera hoja
    # del elemento más largo
    # #
    while nodo_actual.parent is not None and nodo_actual.isEndOfWord == False and len(nodo_actual.children) == 0:
        nodo_padre = nodo_actual.parent
        nodo_padre.children.remove(nodo_actual)
        nodo_actual = nodo_padre
    
    return True

def print_trie(node, palabra=""):
    """Función auxiliar para imprimir todas las palabras del Trie."""
    if node.isEndOfWord:
        print("Palabra encontrada:", palabra)
    for child in node.children:
        print_trie(child, palabra + child.key)
class AVLTree:
    root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None

def rotacion_izquierda(arbol_avl, nodo_avl):
    nueva_raiz = nodo_avl.rightnode  # la nueva raíz será el hijo derecho de la raíz actual.
    nodo_avl.rightnode = nueva_raiz.leftnode    # el hijo derecho del nodo que era raíz será el hijo izquierdo del nodo que pasa a ser la nueva raíz.
    
    if nueva_raiz.leftnode is not None:     # siempre y cuando ese nodo tenga hijo; se valida en esta función.
        nueva_raiz.leftnode.parent = nodo_avl
    
    if nodo_avl.parent is None:     # si el nodo es la actual raíz, es decir, no tiene padre; actualizamos la raíz.
        arbol_avl.root = nueva_raiz
    elif nodo_avl == nodo_avl.parent.leftnode:  # si el nodo es el hijo izquierdo de la raíz, actualizamos su padre.
        nodo_avl.parent.leftnode = nueva_raiz
    else:
        nodo_avl.parent.rightnode = nueva_raiz  # si el nodo es el hijo derecho de la raíz, entonces actualizamos su padre.
    
    nueva_raiz.leftnode = nodo_avl  # el hizo izquierdo de la nueva raíz pasa a ser el nodo que era raíz.
    nodo_avl.parent = nueva_raiz    # el nodo que era raíz inicialmente tiene una nueva raíz.
    
    return nueva_raiz

def rotacion_derecha(arbol_avl, nodo_avl):
    nueva_raiz = nodo_avl.leftnode  # la nueva raíz será el hijo izquierdo de la raíz actual.
    nodo_avl.leftnode = nueva_raiz.rightnode    # el hijo izquierdo del nodo que era raíz será el hijo derecho del nodo que pasa a ser la nueva raíz.
    
    if nueva_raiz.rightnode is not None:        # siempre y cuando ese nodo tenga un hijo; se valida en esta función.
        nueva_raiz.rightnode.parent = nodo_avl
    
    if nodo_avl.parent is None:     # si el nodo es la actual raíz, actualizamos la nueva raíz.
        arbol_avl.root = nueva_raiz
    elif nodo_avl == nodo_avl.parent.leftnode:      # si el nodo no es la raíz, sino que es el hijo izquierdo de la raíz, entonces actualizamos su padre.
        nodo_avl.parent.leftnode = nueva_raiz
    else:
        nodo_avl.parent.rightnode = nueva_raiz      # si el nodo no es la raíz, sino que es el hijo derecho de la raíz, entonces actualizamos su padre.
    
    nueva_raiz.rightnode = nodo_avl     # el hijo derecho de la nueva raíz pasa a ser el nodo que era raíz inicialmente.
    nodo_avl.parent = nueva_raiz        # el nodo que era raíz pasa a tener un padre que es la nueva raíz.
    
    return nueva_raiz   # retornamos la raíz actualizada.

def altura_arbol(nodo_avl):
    if nodo_avl is None:    
        return 0
    return 1 + max(altura_arbol(nodo_avl.leftnode), altura_arbol(nodo_avl.rightnode))   # retorna la altura de los subárboles para calcular el bf.

def calcular_factor_balanceo(nodo_avl):
    if nodo_avl is None:    # caso base, si no hay mas nodos hijos, se retorna 0.
        return 0
    
    calcular_factor_balanceo(nodo_avl.leftnode) # baja de forma recursiva para calcular el bf de todos los hijos izquierdos.
    calcular_factor_balanceo(nodo_avl.rightnode)    # baja de forma recursiva para calcular el bf de todos los hijos derechos.
    
    altura_subarbol_izquierdo = altura_arbol(nodo_avl.leftnode) 
    altura_subarbol_derecho = altura_arbol(nodo_avl.rightnode)
    nodo_avl.bf = altura_subarbol_izquierdo - altura_subarbol_derecho   # se calcula la altura de cada subarbol para sacar el bf de cada nodo.
    
    return nodo_avl.bf  # se retorna el bf de cada nodo.

def calcular_balance(arbol_avl):    # funcion para calcular el factor de balanceo para todos los nodos del árbol.
    calcular_factor_balanceo(arbol_avl.root)    # pasa la raíz a otra función que se encargará de ir nodo por nodo calculando el bf.
    return arbol_avl

def rebalancear_arbol(arbol_avl):
    calcular_balance(arbol_avl)
    arbol_avl.root = rebalancear_subarbol(arbol_avl, arbol_avl.root)
    return arbol_avl

def rebalancear_subarbol(arbol_avl, nodo_avl):
    if nodo_avl is None:
        return None
    
    nodo_avl.leftnode = rebalancear_subarbol(arbol_avl, nodo_avl.leftnode)
    nodo_avl.rightnode = rebalancear_subarbol(arbol_avl, nodo_avl.rightnode)
    
    altura_subarbol_izquierdo = altura_arbol(nodo_avl.leftnode) 
    altura_subarbol_derecho = altura_arbol(nodo_avl.rightnode)
    nodo_avl.bf = altura_subarbol_izquierdo - altura_subarbol_derecho
    
    if nodo_avl.bf > 1:
        if nodo_avl.leftnode is not None and nodo_avl.leftnode.bf < 0:
            nodo_avl.leftnode = rotacion_izquierda(arbol_avl, nodo_avl.leftnode)
            return rotacion_derecha(arbol_avl, nodo_avl)
        else:
            return rotacion_derecha(arbol_avl, nodo_avl)
    elif nodo_avl.bf < -1:
        if nodo_avl.rightnode is not None and nodo_avl.rightnode.bf > 0:
            nodo_avl.rightnode = rotacion_derecha(arbol_avl, nodo_avl.rightnode)
            return rotacion_izquierda(arbol_avl, nodo_avl)
        else:
            return rotacion_izquierda(arbol_avl, nodo_avl)
    
    return nodo_avl

# función tomada de binarytree.py de algo1 adaptada
def insertR(node, element, key):
    if key < node.key:
        if node.leftnode is None:
            nuevo = AVLNode()
            nuevo.key = key
            nuevo.value = element
            nuevo.parent = node
            nuevo.leftnode = None
            nuevo.rightnode = None
            nuevo.bf = 0
            node.leftnode = nuevo
            return nuevo
        else:
            return insertR(node.leftnode, key, element)
    elif key > node.key:
        if node.rightnode is None:
            nuevo = AVLNode()
            nuevo.key = key
            nuevo.value = element
            nuevo.parent = node
            nuevo.leftnode = None
            nuevo.rightnode = None
            nuevo.bf = 0
            node.rightnode = nuevo
            return nuevo
        else:
            return insertR(node.rightnode, key, element)
    else:
        return None

# función tomada de binarytree.py de algo1 adaptada
def insert(B, element, key):
    if B.root is None:  # si el árbol está vacío, se agrega un nodo y terminamos.
        raiz = AVLNode()
        raiz.key = key
        raiz.value = element
        raiz.parent = None
        raiz.leftnode = None
        raiz.rightnode = None
        raiz.bf = 0
        B.root = raiz
        return raiz
    nodo_insertado = insertR(B.root, key, element)  # si el árbol no está vacío se busca la posición donde debe ser insertado.
    if nodo_insertado is None:  # si la key del nodo a insertar ya existía, no se inserta.
        return None
    nodo_rebalanceado = nodo_insertado.parent
    while nodo_rebalanceado is not None:    # se hace el rebalanceo hasta que no hayan más nodos padres.
        altura_izq = altura_arbol(nodo_rebalanceado.leftnode)
        altura_der = altura_arbol(nodo_rebalanceado.rightnode)
        nodo_rebalanceado.bf = altura_izq - altura_der
        if nodo_rebalanceado.bf > 1:
            if nodo_rebalanceado.leftnode.bf >= 0:
                nueva_raiz = rotacion_derecha(B, nodo_rebalanceado)
            else:
                rotacion_izquierda(B, nodo_rebalanceado.leftnode)
                nueva_raiz = rotacion_derecha(B, nodo_rebalanceado)
            if nueva_raiz.parent is None:
                B.root = nueva_raiz
            nodo_rebalanceado = nueva_raiz.parent
        elif nodo_rebalanceado.bf < -1:
            if nodo_rebalanceado.rightnode.bf <= 0:
                nueva_raiz = rotacion_izquierda(B, nodo_rebalanceado)
            else:
                rotacion_derecha(B, nodo_rebalanceado.rightnode)
                nueva_raiz = rotacion_izquierda(B, nodo_rebalanceado)
            if nueva_raiz.parent is None:
                B.root = nueva_raiz
            nodo_rebalanceado = nueva_raiz.parent
        else:
            nodo_rebalanceado = nodo_rebalanceado.parent
    return nodo_insertado

# función tomada de binarytree.py de algo1 adaptada
def eliminar_segun_caso(B, nodo):
    key_nodo = nodo.key
    
    # caso en el que el nodo a eliminar sea el root
    if nodo.parent == None and nodo.leftnode == None and nodo.rightnode == None:
        B.root = None
        return key_nodo
    
    # caso en el que el nodo sea una hoja
    if nodo.leftnode == None and nodo.rightnode == None:
        if nodo.parent.leftnode == nodo:
            nodo.parent.leftnode = None
            return key_nodo
        else:
            nodo.parent.rightnode = None
        return key_nodo
    
    # caso en el que tenga un hijo menor
    # caso en que el nodo tiene un solo hijo (izquierdo)
    if nodo.leftnode != None and nodo.rightnode == None:
        if nodo.parent.leftnode == nodo:
            nodo.parent.leftnode = nodo.leftnode
        else:
            nodo.parent.rightnode = nodo.leftnode
        nodo.leftnode.parent = nodo.parent
        return key_nodo

    # caso en que el nodo tiene un solo hijo (derecho)
    if nodo.leftnode == None and nodo.rightnode != None:
        if nodo.parent.leftnode == nodo:
            nodo.parent.leftnode = nodo.rightnode
        else:
            nodo.parent.rightnode = nodo.rightnode
        nodo.rightnode.parent = nodo.parent
        return key_nodo
    
    # caso en el que tenga dos hijos
    if nodo.leftnode != None and nodo.rightnode != None:
        nodo_sucesor = nodo.rightnode
        # vamos a buscar el nodo con key más chica dentro de los que tienen la mayor key.
        while nodo_sucesor.leftnode != None:
            nodo_sucesor = nodo_sucesor.leftnode
        
        nodo.value = nodo_sucesor.value
        nodo.key = nodo_sucesor.key
        
        # desvinculo el nodo sucesor del árbol
        if nodo_sucesor.parent.leftnode == nodo_sucesor:
            nodo_sucesor.parent.leftnode = nodo_sucesor.rightnode
        else:
            nodo_sucesor.parent.rightnode = nodo_sucesor.rightnode
        
        if nodo_sucesor.rightnode != None:
            nodo_sucesor.rightnode.parent = nodo_sucesor.parent
        
        return key_nodo

# función tomada de binarytree.py de algo1 adaptada
def search_node_by_key(node, key):
    if node == None:
        return None
    
    if node.key == key:
        return node
    
    nodo_izquierda = search_node_by_key(node.leftnode, key)
    if nodo_izquierda != None:
        return nodo_izquierda
    
    nodo_derecha = search_node_by_key(node.rightnode, key)
    if nodo_derecha != None:
        return nodo_derecha

# función tomada de binarytree.py de algo1 adaptada
def delete(B, key):
    nodo = search_node_by_key(B.root, key)
    if nodo is None:    # si no encontramos el nodo retornamos sin eliminar nada.
        return None
    key_eliminado = eliminar_segun_caso(B, nodo)
    nodo_actual = nodo.parent
    while nodo_actual is not None:  # se rebalancea el árbol desde el padre del nodo eliminado hacia arriba.
        altura_izq = altura_arbol(nodo_actual.leftnode)
        altura_der = altura_arbol(nodo_actual.rightnode)
        nodo_actual.bf = altura_izq - altura_der
        if nodo_actual.bf > 1 or nodo_actual.bf < -1:
            if nodo_actual.parent is None:
                B.root = rebalancear_subarbol(B, nodo_actual)
                nodo_actual = None
            else:
                nuevo_subraiz = rebalancear_subarbol(B, nodo_actual)
                if nodo_actual == nodo_actual.parent.leftnode:
                    nodo_actual.parent.leftnode = nuevo_subraiz
                else:
                    nodo_actual.parent.rightnode = nuevo_subraiz
                nodo_actual = nuevo_subraiz.parent
        else:
            nodo_actual = nodo_actual.parent
    return key_eliminado
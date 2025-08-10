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


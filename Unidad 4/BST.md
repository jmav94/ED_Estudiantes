# Unidad 4 – Árboles y Estructuras Avanzadas

## Tema: Árboles Binarios de Búsqueda (BST)


## **Objetivos de aprendizaje**

1. Comprender el concepto y las propiedades de un **árbol binario de búsqueda**.
2. Implementar las operaciones fundamentales: **inserción, búsqueda y eliminación**.
3. Analizar la **complejidad temporal** de las operaciones básicas.
4. Aplicar recorridos (inorden, preorden, postorden) para procesar los datos en orden lógico.
5. Identificar los casos en que un BST se desequilibra y comprender la motivación de los árboles balanceados (como AVL o Red-Black Trees).

## **1. Concepto y propiedades de un BST**

Un **árbol binario de búsqueda (Binary Search Tree)** es un tipo especial de árbol binario que mantiene los elementos **ordenados jerárquicamente**.

### Propiedad fundamental:

Para cada nodo del árbol:

* Los valores del **subárbol izquierdo** son **menores** que el valor del nodo.
* Los valores del **subárbol derecho** son **mayores** que el valor del nodo.

> Esta propiedad debe cumplirse **recursivamente** en todos los subárboles.


### Ejemplo:

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4  7  13
```

* Subárbol izquierdo de `8` contiene valores menores: [3, 1, 6, 4, 7]
* Subárbol derecho contiene valores mayores: [10, 14, 13]


## **2. Implementación básica en Python**

### Clase `Nodo` y `BST`:

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class BST:
    def __init__(self):
        self.raiz = None

    # Insertar un valor
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(valor, nodo.izq)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(valor, nodo.der)
        # Si es igual, se ignora o maneja según el caso
```


## **3. Búsqueda en un BST**

```python
def buscar(self, valor):
    return self._buscar(valor, self.raiz)

def _buscar(self, valor, nodo):
    if nodo is None:
        return False
    if valor == nodo.valor:
        return True
    elif valor < nodo.valor:
        return self._buscar(valor, nodo.izq)
    else:
        return self._buscar(valor, nodo.der)
```

**Ejemplo de uso:**

```python
arbol = BST()
for n in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    arbol.insertar(n)

print(arbol.buscar(6))  # True
print(arbol.buscar(11)) # False
```


## **4. Recorridos del BST**

```python
def inorden(self, nodo):
    if nodo:
        self.inorden(nodo.izq)
        print(nodo.valor, end=" ")
        self.inorden(nodo.der)
```

**Salida esperada (valores en orden ascendente):**

```
1 3 4 6 7 8 10 13 14
```


## **5. Eliminación de un nodo**

La operación de eliminación requiere manejar **tres casos**:

1. **Nodo hoja:** simplemente se elimina.
2. **Nodo con un hijo:** se reemplaza por su hijo.
3. **Nodo con dos hijos:** se reemplaza por el **sucesor inorden** (el menor del subárbol derecho).

```python
def eliminar(self, valor):
    self.raiz = self._eliminar(valor, self.raiz)

def _eliminar(self, valor, nodo):
    if nodo is None:
        return nodo
    if valor < nodo.valor:
        nodo.izq = self._eliminar(valor, nodo.izq)
    elif valor > nodo.valor:
        nodo.der = self._eliminar(valor, nodo.der)
    else:
        # Caso 1 y 2
        if nodo.izq is None:
            return nodo.der
        elif nodo.der is None:
            return nodo.izq
        # Caso 3: buscar sucesor inorden
        temp = self._minimo(nodo.der)
        nodo.valor = temp.valor
        nodo.der = self._eliminar(temp.valor, nodo.der)
    return nodo

def _minimo(self, nodo):
    actual = nodo
    while actual.izq:
        actual = actual.izq
    return actual
```


## **6. Complejidad temporal**

| Operación   | Mejor caso (balanceado) | Peor caso (desbalanceado) |
| ----------- | ----------------------- | ------------------------- |
| Búsqueda    | O(log n)                | O(n)                      |
| Inserción   | O(log n)                | O(n)                      |
| Eliminación | O(log n)                | O(n)                      |

**Nota:** Cuando el árbol está muy desbalanceado (por ejemplo, al insertar datos ya ordenados), su comportamiento se degrada a una **lista enlazada**.
Esto motiva el uso de **árboles balanceados (AVL, Red-Black Trees)**.


### Tarea 

Implementa un programa que:

1. Inserte los valores `[50, 30, 70, 20, 40, 60, 80]` en un BST.
2. Imprima el recorrido inorden.
3. Busque los valores `60` y `25`.
4. Elimine el nodo `30` y vuelva a imprimir el árbol.


## **7. Visualización del BST**

Para depurar y visualizar el árbol en consola:

```python
def imprimir(self, nodo=None, nivel=0):
    if nodo is None:
        nodo = self.raiz
    if nodo.der:
        self.imprimir(nodo.der, nivel + 1)
    print('   ' * nivel + f'→ {nodo.valor}')
    if nodo.izq:
        self.imprimir(nodo.izq, nivel + 1)

# Ejemplo:
arbol.imprimir()
```

**Salida visual:**

```
         → 14
      → 10
   → 8
         → 7
      → 6
         → 4
   → 3
      → 1
```

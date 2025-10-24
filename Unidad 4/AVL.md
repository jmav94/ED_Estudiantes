# Unidad 4: Árboles y Estructuras Avanzadas

## Tema: Árboles Balanceados (AVL y Splay)

## 1. ¿Por qué se necesitan árboles balanceados?

Los **árboles binarios de búsqueda (BST)** permiten insertar, eliminar y buscar elementos en promedio en **O(log n)**.
Sin embargo, si los datos llegan en orden (ascendente o descendente), el árbol se **desbalancea** y se convierte en una lista lineal, empeorando a **O(n)**.

Ejemplo:

```
Insertar: 1, 2, 3, 4, 5
```

BST resultante:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
```

Este árbol está completamente desbalanceado: cada nodo tiene solo un hijo derecho.
Para resolver este problema surgen los **árboles balanceados**, que **mantienen su altura lo más baja posible**.

---

## 2. Árboles AVL

Los **árboles AVL** (por *Adelson-Velsky y Landis*, 1962) fueron los **primeros árboles de búsqueda balanceados**.

### Definición

Un árbol AVL cumple:

> Para cada nodo, la diferencia entre la altura del subárbol izquierdo y derecho es como máximo **1**.

Formalmente:
[
|altura(izq) - altura(der)| \leq 1
]

---

### Operaciones principales

#### Inserción

Cuando insertas un nodo en un AVL:

1. Se inserta igual que en un BST normal.
2. Se recalcula el **factor de balanceo (FB)** de cada nodo.
3. Si el árbol se desbalancea, se aplican **rotaciones**.

#### Factor de balanceo (FB)

[
FB = altura(izquierdo) - altura(derecho)
]

Valores posibles:

* `FB = -1, 0, 1` → balanceado
* `FB < -1 o FB > 1` → desbalanceado


### Tipos de rotaciones

1. **Rotación simple a la derecha (caso Izquierda-Izquierda)**
   Ocurre cuando se inserta en el subárbol izquierdo del hijo izquierdo.

   ```
       A
      /
     B
    /
   C
   ```

   Se rota a la derecha en A → B pasa a ser la nueva raíz del subárbol.

2. **Rotación simple a la izquierda (caso Derecha-Derecha)**
   Ocurre cuando se inserta en el subárbol derecho del hijo derecho.

   ```
   A
    \
     B
      \
       C
   ```

   Se rota a la izquierda en A → B pasa a ser la nueva raíz.

3. **Rotación doble Izquierda-Derecha (caso IZQ-DER)**

   ```
       A
      /
     B
      \
       C
   ```

   Se rota primero a la izquierda sobre B, luego a la derecha sobre A.

4. **Rotación doble Derecha-Izquierda (caso DER-IZQ)**

   ```
   A
    \
     B
    /
   C
   ```

   Se rota primero a la derecha sobre B, luego a la izquierda sobre A.

### Ejemplo de inserción en un árbol AVL

Insertar: 30, 20, 10

1. Insertar 30 → raíz
2. Insertar 20 → a la izquierda
3. Insertar 10 → subárbol izquierdo del 20
   → desbalance (FB de 30 = +2)

Aplicamos **rotación simple a la derecha**.
Resultado:

```
    20
   /  \
  10   30
```

Árbol balanceado.


### Complejidad

* Búsqueda, inserción, eliminación: **O(log n)**
* Rotaciones: **O(1)**
* Espacio adicional: **O(1)**

---

### Ejemplo en Python

```python
class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1

def altura(nodo):
    return nodo.altura if nodo else 0

def rotacion_derecha(y):
    x = y.izq
    T2 = x.der
    x.der = y
    y.izq = T2
    y.altura = 1 + max(altura(y.izq), altura(y.der))
    x.altura = 1 + max(altura(x.izq), altura(x.der))
    return x

def rotacion_izquierda(x):
    y = x.der
    T2 = y.izq
    y.izq = x
    x.der = T2
    x.altura = 1 + max(altura(x.izq), altura(x.der))
    y.altura = 1 + max(altura(y.izq), altura(y.der))
    return y

def factor_balanceo(nodo):
    return altura(nodo.izq) - altura(nodo.der) if nodo else 0

def insertar(raiz, valor):
    if not raiz:
        return NodoAVL(valor)
    if valor < raiz.valor:
        raiz.izq = insertar(raiz.izq, valor)
    else:
        raiz.der = insertar(raiz.der, valor)

    raiz.altura = 1 + max(altura(raiz.izq), altura(raiz.der))
    fb = factor_balanceo(raiz)

    # Casos de rotación
    if fb > 1 and valor < raiz.izq.valor:
        return rotacion_derecha(raiz)
    if fb < -1 and valor > raiz.der.valor:
        return rotacion_izquierda(raiz)
    if fb > 1 and valor > raiz.izq.valor:
        raiz.izq = rotacion_izquierda(raiz.izq)
        return rotacion_derecha(raiz)
    if fb < -1 and valor < raiz.der.valor:
        raiz.der = rotacion_derecha(raiz.der)
        return rotacion_izquierda(raiz)

    return raiz

## Uso
raiz = None
for valor in [30, 20, 10]:
    raiz = insertar(raiz, valor)
print("Recorrido inorden del AVL balanceado:")
inorden(raiz)

```


## 3. Árboles Splay (autoajustables)

Los **árboles Splay** son **árboles de búsqueda binaria autoajustables**, creados por *Sleator y Tarjan (1985)*.

### Idea principal

Cada vez que se accede (se busca, inserta o elimina) un nodo, el árbol realiza **rotaciones** para **llevar ese nodo a la raíz**.

De esta forma, los elementos más usados tienden a quedar más cerca de la raíz.


### Operación de *Splaying*

Hay tres tipos básicos de rotaciones (similares al AVL):

1. **Zig:**
   Cuando el nodo es hijo directo de la raíz.
   Se realiza una sola rotación.

2. **Zig-Zig:**
   Nodo y su padre están en la misma dirección (ambos izquierdos o ambos derechos).
   Se realizan dos rotaciones simples.

3. **Zig-Zag:**
   Nodo y su padre están en direcciones opuestas.
   Se realizan dos rotaciones, una en el padre y otra en el abuelo.

---

### Ejemplo simplificado en Python

```python
class NodoSplay:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def rotacion_derecha(x):
    y = x.izq
    x.izq = y.der
    y.der = x
    return y

def rotacion_izquierda(x):
    y = x.der
    x.der = y.izq
    y.izq = x
    return y

def splay(raiz, valor):
    if raiz is None or raiz.valor == valor:
        return raiz

    # Zig-Zig izquierda
    if valor < raiz.valor and raiz.izq:
        if valor < raiz.izq.valor:
            raiz.izq.izq = splay(raiz.izq.izq, valor)
            raiz = rotacion_derecha(raiz)
         elif valor > raiz.izq.valor:
            raiz.izq.der = splay(raiz.izq.der, valor)
            if raiz.izq.der:
                raiz.izq = rotacion_izquierda(raiz.izq)
        return rotacion_derecha(raiz) if raiz.izq else raiz

    # Zig-Zig derecha
    if valor > raiz.valor and raiz.der:
        if valor > raiz.der.valor:
            raiz.der.der = splay(raiz.der.der, valor)
            raiz = rotacion_izquierda(raiz)
        elif valor < raiz.der.valor:
            raiz.der.izq = splay(raiz.der.izq, valor)
            if raiz.der.izq:
                raiz.der = rotacion_derecha(raiz.der)
        return rotacion_izquierda(raiz) if raiz.der else raiz

    return raiz

## uso
raiz = NodoSplay(10)
raiz.der = NodoSplay(20)
raiz.der.der = NodoSplay(30)

# Acceder al valor 30
raiz = splay(raiz, 30)

# Imprimir raíz actual
print("Raíz actual tras acceder 30:", raiz.valor)
```


### Comparación AVL vs Splay

| Característica       | AVL                                       | Splay                                   |
| -------------------- | ----------------------------------------- | --------------------------------------- |
| Balance              | Estricto (altura logarítmica garantizada) | Ajuste dinámico por acceso              |
| Eficiencia promedio  | O(log n)                                  | O(log n) amortizado                     |
| Eficiencia peor caso | O(log n)                                  | O(n)                                    |
| Ideal para           | Accesos aleatorios                        | Accesos repetidos o patrones frecuentes |
| Rotaciones           | Al insertar o eliminar                    | En cada acceso                          |

---

## Tarea

1. **Implementación:**
   Implementar una clase `ArbolAVL` y una clase `ArbolSplay` con inserción y recorrido inorden.

2. **Visualización:**
   Usar la librería `graphviz` o `networkx` para visualizar el árbol antes y después de las rotaciones.

3. **Comparación práctica:**
   Medir los tiempos de búsqueda repetida en AVL y Splay con los mismos datos.


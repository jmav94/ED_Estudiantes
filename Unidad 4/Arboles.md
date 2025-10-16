
# **Unidad 4 — Representación e Implementación de Árboles**

---
**Representaciones comunes de árboles**

### Representación con listas anidadas  

Es la forma más simple y directa para árboles pequeños o demostrativos.

**Ejemplo:**

```python
# Estructura: [raíz, subárbol_izq, subárbol_der]
arbol = ['A', 
          ['B', 
             ['D', None, None], 
             ['E', None, None]], 
          ['C', 
             None, 
             ['F', None, None]]
        ]
```

 **Ventajas:**

* Fácil de visualizar y manipular.
* No requiere clases ni estructuras complejas.

 **Desventajas:**

* Poco eficiente en árboles grandes.
* Acceso y modificación complicados.
* No hay encapsulación ni métodos.


### Representación con diccionarios

Adecuada para árboles **no necesariamente binarios**, especialmente si las claves son **nombres o identificadores únicos**.

**Ejemplo:**

```python
arbol = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
```

**Interpretación:**

* Cada clave representa un nodo.
* Cada valor es la lista de hijos.

 **Ventajas:**

* Ideal para representar jerarquías tipo árbol general.
* Compatible con JSON y bases de datos NoSQL.

 **Desventajas:**

* No hay referencias directas a los padres.
* No es trivial realizar recorridos recursivos si no se conoce la raíz.

---

### **2.3. Representación con clases (orientado a objetos)**

La forma más estructurada y extensible.
Permite encapsular comportamiento y crear árboles dinámicos.

#### Clase para Árbol General

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print_tree(self, level=0):
        print("  " * level + self.data)
        for child in self.children:
            child.print_tree(level + 1)

# Ejemplo de uso
root = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

root.add_child(b)
root.add_child(c)
b.add_child(d)

root.print_tree()
```

📘 **Salida:**

```
A
  B
    D
  C
```

**Ventajas:**

* Permite expandir el diseño (agregar métodos: búsqueda, recorrido, altura).
* Ideal para modelar estructuras reales.

**Desventajas:**

* Requiere más memoria y código.
* Más complejo de serializar.

---

###  Representación de Árbol Binario

Un árbol **binario** restringe a **dos hijos** por nodo: izquierdo y derecho.
Se usa ampliamente en algoritmos de búsqueda, ordenación y compresión.

#### Clase para Árbol Binario

```python
class NodoBinario:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None
```

####  Creación de un árbol binario manual

```python
raiz = NodoBinario('A')
raiz.izquierdo = NodoBinario('B')
raiz.derecho = NodoBinario('C')
raiz.izquierdo.izquierdo = NodoBinario('D')
raiz.izquierdo.derecho = NodoBinario('E')
raiz.derecho.derecho = NodoBinario('F')
```

Estructura visual:

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

---

##  Recorridos básicos

Los **recorridos** son métodos para visitar todos los nodos del árbol de manera sistemática.

Para árboles binarios, los principales son:

| Tipo          | Orden de visita  | Ejemplo (para el árbol anterior) |
| ------------- | ---------------- | -------------------------------- |
| **Preorden**  | Raíz → Izq → Der | A, B, D, E, C, F                 |
| **Inorden**   | Izq → Raíz → Der | D, B, E, A, C, F                 |
| **Postorden** | Izq → Der → Raíz | D, E, B, F, C, A                 |

#### Implementación:

```python
def preorden(nodo):
    if nodo:
        print(nodo.dato, end=' ')
        preorden(nodo.izquierdo)
        preorden(nodo.derecho)
```

---

## **4. Propiedades prácticas de los árboles en Python**

* Los **árboles binarios** permiten búsquedas logarítmicas (O(log n)) cuando están balanceados.
* Se usan para implementar estructuras como:

  * Árboles de búsqueda binaria (BST).
  * Árboles AVL (balanceados).
  * Montículos (Heaps).
  * Árboles de decisión (Machine Learning).

---

## **5. Actividades prácticas**

### **Actividad 1: Construcción**
Crea una clase Node con atributos data y children.
Construye un árbol que represente el sistema de carpetas:
```
Root
 ├── Documentos
 │    ├── Escuela
 │    └── Trabajo
 └── Imágenes
      ├── Vacaciones
      └── Familia
```
Implementa un método print_tree() para mostrarlo jerárquicamente.

### **Actividad 2: Árbol binario**

Estructura visual:

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

1. Implementa la clase `NodoBinario`.
2. Crea el árbol del ejemplo anterior (A–F).
3. Implementa e imprime los recorridos:

   * Preorden
   * Inorden
   * Postorden

### **Actividad 3**

Agrega un método a `NodoBinario` que calcule la **altura** del árbol:

```python
def altura(nodo):
    if nodo is None:
        return 0
    return 1 + max(altura(nodo.izquierdo), altura(nodo.derecho))
```

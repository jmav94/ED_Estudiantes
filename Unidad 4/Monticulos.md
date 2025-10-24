# Unidad 4 – Estructuras Jerárquicas

## Tema 5: Montículos (Heaps) y Colas de Prioridad

## 1. ¿Qué es un Heap?

Un **heap (montículo)** es una **estructura de datos basada en un árbol binario completo** que mantiene un **orden parcial** entre los elementos.

Existen dos tipos principales:

* 🟢 **Min-Heap:** el valor del **padre es menor o igual** que el de sus hijos.
* 🔴 **Max-Heap:** el valor del **padre es mayor o igual** que el de sus hijos.

**Ejemplo de un Min-Heap:**

```
         2
       /   \
      4     5
     / \   / \
    9  6  7   8
```

✅ El valor más pequeño (2) está siempre en la **raíz**.
Esto es lo que hace tan eficiente la operación de obtener el mínimo.

## 2. Propiedad de los Heaps

Un **heap siempre es un árbol binario completo**, lo que significa:

* Todos los niveles, excepto el último, están **completos**.
* En el último nivel, los nodos se llenan de **izquierda a derecha**.

Gracias a esto, **no se necesita una estructura de nodos**; se puede guardar todo en una **lista**.

**Ejemplo:**

```
Árbol:                Lista (índices)
       2              [2, 4, 5, 9, 6, 7, 8]
      / \
     4   5
    / \ / \
   9 6 7  8
```

Relaciones entre índices:

| Operación      | Fórmula      |
| -------------- | ------------ |
| Padre de i     | (i - 1) // 2 |
| Hijo izquierdo | 2 * i + 1    |
| Hijo derecho   | 2 * i + 2    |



## La Idea Central

Un **árbol binario completo** se puede almacenar en un array **leyendo sus niveles de arriba a abajo y de izquierda a derecha**.

```
    Árbol:          Array:
      0            [0, 1, 2, 3, 4, 5]
     /   \
    1     2        Posiciones: 0, 1, 2, 3, 4, 5
   / \   /
  3   4 5
```

---

## Explicación Visual con Ejemplo

Usemos este array: `[A, B, C, D, E, F]`

```
    Árbol:          Array:
      A (0)         Índices: [0:A, 1:B, 2:C, 3:D, 4:E, 5:F]
     /   \
    B(1)  C(2)
   / \    /
  D(3) E(4) F(5)
```

### 1. **Padre de i = (i - 1) // 2** ⬆️

**¿Por qué?** Porque cada nivel tiene aproximadamente el doble de nodos que el anterior.

**Ejemplos:**
- **Padre de E (índice 4)**: `(4 - 1) // 2 = 3 // 2 = 1` → **B** ✅
- **Padre de F (índice 5)**: `(5 - 1) // 2 = 4 // 2 = 2` → **C** ✅
- **Padre de D (índice 3)**: `(3 - 1) // 2 = 2 // 2 = 1` → **B** ✅

### 2. **Hijo izquierdo = 2 × i + 1** ⬇️↙️

**¿Por qué?** Porque cada nodo padre tiene exactamente 2 hijos en el nivel siguiente.

**Ejemplos:**
- **Hijo izquierdo de A (0)**: `2×0 + 1 = 1` → **B** ✅
- **Hijo izquierdo de B (1)**: `2×1 + 1 = 3` → **D** ✅
- **Hijo izquierdo de C (2)**: `2×2 + 1 = 5` → **F** ✅

### 3. **Hijo derecho = 2 × i + 2** ⬇️↘️

**¿Por qué?** Está justo al lado del hijo izquierdo.

**Ejemplos:**
- **Hijo derecho de A (0)**: `2×0 + 2 = 2` → **C** ✅
- **Hijo derecho de B (1)**: `2×1 + 2 = 4` → **E** ✅
- **Hijo derecho de C (2)**: `2×2 + 2 = 6` → ❌ (no existe, índice fuera del array)

---

## Explicación Matemática Simple

Imagina que los nodos están numerados por niveles:

```
Nivel 0:               0
Nivel 1:         1           2
Nivel 2:     3     4     5     6
Nivel 3:   7   8 9  10 11 12 13 14
```

**Patrón:**
- El **nivel k** comienza en el índice: `2^k - 1`
- Cada nodo en la posición `i` tiene:
  - **Hijos en**: `2i+1` y `2i+2`
  - **Padre en**: `⌊(i-1)/2⌋` (división entera)

---

## Puntos Importantes a Recordar

1. **// significa división entera**: Descarta el decimal `(5-1)//2 = 4//2 = 2`
2. **Verifica los límites del array**: Un hijo puede no existir si el índice calculado es mayor que el tamaño del array
3. **La raíz está en índice 0**: El padre de la raíz no existe

---

## Ejemplo Práctico en Código

```python
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
```
---

## 3. Operaciones básicas en un Heap

Python incluye el módulo `heapq`, que implementa un **min-heap** de manera muy eficiente.

```python
import heapq
```

---

### a) Insertar un elemento: `heappush(heap, elemento)`

Cuando insertamos, el nuevo elemento se agrega al final y luego “sube” hasta mantener la propiedad del heap (heapify-up).

```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

print(heap)
```

 **Salida:**

```
[1, 2, 8, 5]
```

➡️ Aunque la lista no parece ordenada, sí cumple la **propiedad del heap**:

* El mínimo (1) está en la raíz.
* Cada padre es menor que sus hijos.


### b) Extraer el elemento mínimo: `heappop(heap)`

Se elimina la raíz (mínimo), y el último elemento toma su lugar para luego “bajar” (heapify-down).

```python
minimo = heapq.heappop(heap)
print("Elemento mínimo:", minimo)
print("Heap después:", heap)
```

**Salida:**

```
Elemento mínimo: 1
Heap después: [2, 5, 8]
```

### c) Ver el mínimo sin eliminarlo

```python
print("Mínimo actual:", heap[0])
```

**Salida:**

```
Mínimo actual: 2
```


### d) Convertir una lista en heap: `heapify(lista)`

Convierte cualquier lista en un heap válido, **sin necesidad de insertar uno a uno**.

```python
nums = [5, 3, 8, 1, 9]
heapq.heapify(nums)
print(nums)
```

**Salida:**

```
[1, 3, 8, 5, 9]
```

## 4. ¿Por qué usar un Heap?

Un heap **no está completamente ordenado**, pero **permite acceder rápidamente al mínimo** sin ordenar toda la lista.

Comparación:

| Operación       | Lista ordenada | Heap     |
| --------------- | -------------- | -------- |
| Insertar        | O(n)           | O(log n) |
| Eliminar mínimo | O(1)           | O(log n) |
| Ver mínimo      | O(1)           | O(1)     |

➡️ Ideal cuando hay **inserciones y eliminaciones frecuentes** y solo necesitas el mínimo o máximo en cada momento.


## 5. Colas de Prioridad

Una **cola de prioridad** es como una fila donde cada elemento tiene una prioridad:
* no se atiende al primero que llega, sino al **más urgente**.

El heap permite implementarla fácilmente.

### Ejemplo: gestión de tareas

```python
import heapq

# (prioridad, tarea)
tareas = []
heapq.heappush(tareas, (3, "Hacer tarea"))
heapq.heappush(tareas, (1, "Atender emergencia"))
heapq.heappush(tareas, (2, "Revisar correo"))

while tareas:
    prioridad, tarea = heapq.heappop(tareas)
    print(f"Ejecutando: {tarea} (Prioridad {prioridad})")
```

**Salida:**

```
Ejecutando: Atender emergencia (Prioridad 1)
Ejecutando: Revisar correo (Prioridad 2)
Ejecutando: Hacer tarea (Prioridad 3)
```

> Mientras menor es el número de prioridad, **mayor urgencia**.

---

## 6. Aplicaciones de los Heaps

### a) Planificación de tareas (Scheduling)

Los sistemas operativos usan heaps para decidir **qué proceso ejecutar primero** según prioridad o tiempo de CPU restante.

---

### b) Algoritmo de Dijkstra (camino más corto)

El heap se usa para elegir el **nodo más cercano** en cada paso, haciendo el algoritmo mucho más eficiente.

```python
import heapq

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

def dijkstra(grafo, inicio):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[inicio] = 0
    heap = [(0, inicio)]  # (distancia, nodo)

    while heap:
        costo, nodo = heapq.heappop(heap)
        for vecino, peso in grafo[nodo]:
            nuevo_costo = costo + peso
            if nuevo_costo < dist[vecino]:
                dist[vecino] = nuevo_costo
                heapq.heappush(heap, (nuevo_costo, vecino))
    return dist

print(dijkstra(grafo, 'A'))
```

**Salida:**

```
{'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

---

## 7. Tarea

### Ejercicio 1:

Crea un min-heap con `[10, 1, 8, 4, 7, 3]`.
Inserta el número `2`, elimina el mínimo y muestra el heap final.

---

### Ejercicio 2:

Simula una **cola de prioridad de pacientes**.
Cada paciente tiene un nombre y un nivel de prioridad (1 = urgente, 5 = leve).
Muestra el orden en que son atendidos.

---

### Ejercicio 3:

Convierte una lista `[9, 5, 7, 3, 8]` en un heap y muestra cómo cambia después de agregar `1` y eliminar el mínimo.

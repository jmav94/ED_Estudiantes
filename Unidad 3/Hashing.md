## Tema: Hashing, Tablas Hash y Comparación con Estructuras Lineales

---

## 1. Introducción al Hashing

El **hashing** es una técnica que permite **acceder rápidamente a los datos** mediante una **clave**.
La idea principal es transformar cada clave en una **posición (índice)** dentro de una tabla mediante una **función hash**.

Ejemplo conceptual:

```
Clave → Función hash → Índice → Valor almacenado
"Juan" → hash("Juan") = 3 → tabla[3] = "555-1212"
```

---

## 2. Concepto de Función Hash

Una **función hash** convierte una clave (texto, número, etc.) en un número entero que se utiliza como posición de almacenamiento.

### Requisitos de una buena función hash:

✅ Debe ser **rápida** de calcular.

✅ Debe **distribuir uniformemente** las claves.

✅ Debe **minimizar colisiones** (cuando dos claves tienen el mismo hash).

---

### Ejemplo en Python:

```python
# Ejemplo del uso de la función hash interna de Python
print(hash("Juan"))
print(hash("Pedro"))
print(hash("Ana"))
```

🔎 Nota: El valor de `hash()` puede variar en cada ejecución, ya que Python aleatoriza el resultado por seguridad.

---

## 3. Colisiones

Una **colisión** ocurre cuando dos claves diferentes producen el mismo índice.

Ejemplo conceptual:

```
hash("Juan") = 5
hash("María") = 5
```

Ambas claves intentan ocupar la misma posición en la tabla.

---

## 4. Estrategias para Manejo de Colisiones

### 4.1 Encadenamiento (Chaining)

Cada posición de la tabla contiene una **lista de pares (clave, valor)**.
Cuando hay colisión, el nuevo elemento se agrega a la lista.

```python
tabla = [[] for _ in range(5)]  # 5 espacios en la tabla

def funcion_hash(clave):
    return hash(clave) % len(tabla)

def insertar(tabla, clave, valor):
    indice = funcion_hash(clave)
    tabla[indice].append((clave, valor))

insertar(tabla, "Juan", "555-1212")
insertar(tabla, "María", "555-3434")  # podría ir al mismo índice

print(tabla)
```

---

### 4.2 Direccionamiento abierto (Open Addressing)

En lugar de listas, si una posición está ocupada, se busca la **siguiente libre** en la tabla.

Ejemplo de búsqueda lineal:

```python
tabla = [None] * 5

def funcion_hash(clave):
    return hash(clave) % len(tabla)

def insertar(clave, valor):
    indice = funcion_hash(clave)
    while tabla[indice] is not None:
        indice = (indice + 1) % len(tabla)
    tabla[indice] = (clave, valor)

insertar("Ana", 25)
insertar("Juan", 30)
print(tabla)
```

---

## 5. Comparación: Listas vs Diccionarios (y Tablas Hash)

| Característica              | Lista                            | Diccionario (Hash Table) |
| --------------------------- | -------------------------------- | ------------------------ |
| Tipo de acceso              | Por posición (índice)            | Por clave                |
| Tiempo de búsqueda promedio | O(n)                             | O(1)                     |
| Duplicados permitidos       | Sí                               | No (claves únicas)       |
| Orden                       | Orden de inserción (desde Py3.7) | Orden de inserción       |
| Implementación interna      | Arreglo dinámico                 | Tabla hash               |

### Ejemplo comparativo:

```python
# Búsqueda en lista
nombres = ["Ana", "Luis", "Carlos", "María"]
print("María" in nombres)  # Recorre la lista → O(n)

# Búsqueda en diccionario
edades = {"Ana": 20, "Luis": 22, "Carlos": 21, "María": 23}
print("María" in edades)  # Búsqueda directa → O(1)
```

---

## 6. Implementación Básica de una Tabla Hash en Python

Ejemplo didáctico de cómo funciona internamente un diccionario:

```python
class TablaHash:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]  # Encadenamiento

    def funcion_hash(self, clave):
        return hash(clave) % self.tamaño

    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)
        for par in self.tabla[indice]:
            if par[0] == clave:
                par = (clave, valor)
                return
        self.tabla[indice].append((clave, valor))

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        for par in self.tabla[indice]:
            if par[0] == clave:
                return par[1]
        return None

# Uso
tabla = TablaHash(5)
tabla.insertar("Ana", 20)
tabla.insertar("Luis", 22)
print(tabla.buscar("Ana"))   # 20
```

---

## 7. Aplicaciones del Hashing y los Diccionarios

### 🧮 a) Conteo de frecuencia de palabras

```python
texto = "hola mundo hola python hola"
palabras = texto.split()
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print(frecuencia)
# {'hola': 3, 'mundo': 1, 'python': 1}
```

---

### 💾 b) Implementación simple de caché (almacenamiento temporal)

```python
cache = {}

def obtener_datos(clave):
    if clave in cache:
        print("Recuperado del caché.")
        return cache[clave]
    else:
        print("Calculando valor...")
        resultado = clave ** 2
        cache[clave] = resultado
        return resultado

print(obtener_datos(5))
print(obtener_datos(5))  # Ya viene del caché
```

**Salida:**

```
Calculando valor...
25
Recuperado del caché.
25
```

---

## 8. Ejercicios 


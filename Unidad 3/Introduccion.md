# 📘 Unidad 3 – Mapas, Diccionarios y Hashing

## 1. Introducción General

Hasta ahora hemos trabajado con **estructuras lineales** (listas, pilas y colas).
Estas estructuras organizan los datos en secuencias, pero no siempre son eficientes cuando queremos **buscar rápidamente** un valor asociado a una clave.

Imagina que tienes una lista con 10,000 alumnos y quieres encontrar la calificación de “María López”. Con una lista, tendrías que recorrer elemento por elemento (**O(n)**).
Con un **mapa o diccionario**, puedes acceder directamente en **O(1)**.



## 2. Concepto de Mapa / Diccionario

Un **mapa** es una estructura de datos que almacena **pares clave-valor**, donde:

* Cada **clave** es única.
* Cada **clave** se asocia con un **valor**.
* Se accede a los valores usando las claves, no con posiciones numéricas.

Ejemplo abstracto:

```
Clave → Valor
"ID001" → "Ana Pérez"
"ID002" → "Luis García"
"ID003" → "Carlos Ruiz"
```

En Python:

```python
alumnos = {
    "ID001": "Ana Pérez",
    "ID002": "Luis García",
    "ID003": "Carlos Ruiz"
}
```



## 3. Ventajas de los Mapas

✅ **Búsqueda rápida**: promedio O(1).

✅ **Claves personalizadas** (pueden ser strings, números, tuplas).

✅ **Flexibilidad**: los valores pueden ser números, listas, diccionarios, etc.

✅ **Orden de inserción preservado** (desde Python 3.7).



## 4. Hashing: la base de los Diccionarios

El **hashing** es una técnica que transforma una clave en un **índice numérico**.

* Se aplica una **función hash** a la clave.
* El resultado indica dónde guardar el valor en memoria.

Ejemplo simple (no Python real, solo idea):

```
Clave = "Luis"
Hash("Luis") = 102
Se guarda en la posición 102
```

🔑 Si dos claves generan el mismo índice → ocurre una **colisión**.
Existen estrategias como **encadenamiento** (listas en cada posición) o **direccionamiento abierto** (buscar la siguiente casilla libre).



## 5. Aplicaciones del Hashing y Diccionarios

*  **Índices de bases de datos** (buscar un registro por ID).
*  **Sistemas de inventario** (producto → cantidad).
*  **Cachés en navegadores** (URL → página almacenada).
*  **Procesamiento de texto** (palabra → número de veces que aparece).
*  **Gestión de contraseñas** (hash de la contraseña en lugar de guardarla directamente).



## 6. Comparación Rápida: Listas vs Diccionarios

| Operación             | Lista (arreglo) | Diccionario |
| --------------------- | --------------- | ----------- |
| Acceso por índice     | O(1)            | No aplica   |
| Búsqueda de elemento  | O(n)            | O(1)        |
| Inserción (al final)  | O(1)            | O(1)        |
| Eliminación por clave | O(n)            | O(1)        |



## 7. Ejemplo 

**Problema**: Queremos contar cuántas veces aparece cada palabra en una frase.

### Con lista:

```python
frase = "hola mundo hola python"
palabras = frase.split()
frecuencia = []

for palabra in palabras:
    encontrado = False
    for item in frecuencia:
        if item[0] == palabra:
            item[1] += 1
            encontrado = True
            break
    if not encontrado:
        frecuencia.append([palabra, 1])

print(frecuencia)
# [['hola', 2], ['mundo', 1], ['python', 1]]
```

### Con diccionario:

```python
frase = "hola mundo hola python"
palabras = frase.split()
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print(frecuencia)
# {'hola': 2, 'mundo': 1, 'python': 1}
```

👉 Más limpio, más rápido, más eficiente.

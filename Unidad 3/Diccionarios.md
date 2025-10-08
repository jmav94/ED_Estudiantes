
# 📘 Unidad 3 – Diccionarios en Python

## 1. Introducción

En programación, un **mapa** o **diccionario** es una estructura que asocia una **clave (key)** con un **valor (value)**.
En Python, esta estructura se implementa con el tipo integrado `dict`.

Ejemplo sencillo:

```python
# Diccionario de estudiante
estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Sistemas"
}

print(estudiante["nombre"])  # Ana
```


## 2. Características de los Diccionarios en Python


## 3. Operaciones Básicas

```python
# Crear un diccionario
dic = {
    "a": 1,
    "b": 2
}

# Acceder a un valor

print(dic["a"]) # 1

# Agregar un nuevo par clave-valor

dic["c"] = 3 

# Modificar un valor

dic["a"] = 10

# Eliminar un par

del dic["b"]

# Comprobar existencia de clave

print("a" in dic) #True
print("e" in dic) # False

# Recorrer claves y valores

for clave, valor in dic.items():
    print(clave, valor)

## 4. Métodos Útiles

dic = {"x": 100, "y": 200}

dic.keys() # x,  y 
dic.values() # 100, 200
dic.items() # (x, 100) , (y, 200) 


# Obtener valor con get (más seguro que [])
print(dict.get("x")) # 100



# Eliminar y devolver un valor
valor = dic.pop("y")

print(valor) # 200


```

## 5. Comparación: Lista vs Diccionario

📌 Buscar un elemento en **lista** → O(n).
📌 Buscar un elemento en **diccionario** → O(1) en promedio (gracias a hashing).

Ejemplo:


## 6. Ejercicios Prácticos

### Ejercicio 1 – Diccionario básico

Crea un diccionario llamado `alumno` con las claves: `nombre`, `edad`, `carrera`.
Imprime cada clave y valor en formato:
`nombre: Ana`

```python

alumno = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Ingeniería en Sistemas"
}

for clave, valor in alumno.items():
    print(f"{clave}: {valor}")


```


### Ejercicio 2 – Conteo de palabras

Escribe un programa que reciba una cadena y cuente la frecuencia de cada palabra usando un diccionario.

```python
texto = "hola mundo hola python mundo"
# Resultado esperado:
# {"hola": 2, "mundo": 2, "python": 1}
```

```python

texto = "hola mundo hola python mundo"
palabras = texto.split()
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print(frecuencia)


```


### Ejercicio 3 – Agenda telefónica

Crea un programa que permita:

1. Agregar un contacto (`nombre` → `número`).
2. Buscar un contacto por nombre.
3. Eliminar un contacto.

```python

agenda = {}

# 1. Agregar
agenda["Ana"] = "123456789"
agenda["Luis"] = "987654321"

# 2. Buscar
nombre = "Ana"
if nombre in agenda:
    print(f"{nombre}: {agenda[nombre]}")
else:
    print("Contacto no encontrado")

# 3. Eliminar
del agenda["Luis"]

print("Agenda final:", agenda)

```


### Ejercicio 4 – Diccionario con listas

Crea un diccionario que guarde materias y las calificaciones del alumno:

```python
calificaciones = {
    "Matemáticas": [90, 85, 88],
    "Programación": [100, 95, 97],
}

```

Calcula el promedio por materia.

```python

calificaciones = {
    "Matemáticas": [90, 85, 88],
    "Programación": [100, 95, 97],
    "Bases de Datos": [85, 80, 90]
}

for materia, notas in calificaciones.items():
    promedio = sum(notas) / len(notas)
    print(f"{materia}: {promedio:.2f}")


```

---

### Ejercicio 5 – Uso de `collections.Counter`

Usa `Counter` para simplificar el conteo de palabras en un texto:

```python
from collections import Counter

texto = "python java python c c c java"
frecuencia = Counter(texto.split())
print(frecuencia)
```

```python

from collections import Counter

texto = "python java python c c c java"
palabras = texto.split()
frecuencia = Counter(palabras)

print(frecuencia)

```
---

## 7. Mini Proyecto del tema

**Sistema de Inventario con Diccionarios**
Crea un programa que permita:

* Registrar productos con su nombre como clave y cantidad como valor.
* Vender un producto (disminuir la cantidad).
* Mostrar inventario actualizado.
* Evitar vender productos inexistentes.

Ejemplo de uso:

```
Inventario inicial: {"manzanas": 10, "peras": 5}
Vender("manzanas", 3) → {"manzanas": 7, "peras": 5}
Vender("naranjas", 2) → "Producto no encontrado"
```

```python

inventario = { 
    "manzanas": 10,
    "peras" : 5
     }

def vender(prodcuto, cantidad){
    if producto in inventario: 
        if inventario[producto] >= cantidad:
            inventario[producto] -= cantidad
            print(f"Se vendieron {cantidad} {producto}.")
        else:
            print(f"No hay suficiente cantidad en inventario.")
    else:
        print(f"Producto no encontrado")
}

def mostrar_inventario():
    print("Inventario actual:", inventario)


# Ejemplo de uso
mostrar_inventario()
vender("manzanas", 3)
mostrar_inventario()
vender("peras", 2)


```



## 8. Preguntas de Evaluación



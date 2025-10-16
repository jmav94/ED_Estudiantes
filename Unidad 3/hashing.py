import time

inicio = time.time()
print(inicio)
# Lista 
libros = ["perro", "gato", "pájaro"]
print("gato" in libros)  # Revisa todo, lento si es larga
tiempo_lineal = time.time() - inicio
print(f"Tiempo lineal: {tiempo_lineal:.6f}")


inicio1 = time.time()
print(inicio)
# Diccionario 
dic_libros = {"gato": "maúlla", "perro": "ladrará"}
print(dic_libros["gato"])  
tiempo_lineal1 = time.time() - inicio1
print(f"Tiempo acceso diccionario: {tiempo_lineal1:.6f}")
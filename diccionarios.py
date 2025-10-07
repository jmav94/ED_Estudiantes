inventario = { 
    "manzanas": 10,
    "peras" : 5,
    "naranjas": 8,
    "platanos": 12
     }

def vender(producto, cantidad):
    if producto in inventario: 
        if inventario[producto] >= cantidad:
            inventario[producto] -= cantidad
            print(f"Se vendieron {cantidad} {producto}.")
        else:
            print(f"No hay suficiente cantidad en inventario.")
    else:
        print(f"Producto no encontrado")


def mostrar_inventario():
    print("Inventario actual:", inventario)


# Ejemplo de uso
mostrar_inventario()
vender("manzanas", 3)
mostrar_inventario()
vender("peras", 2)
mostrar_inventario()
vender("platanos", 2)
mostrar_inventario()
# Paso 1: Análisis del problema y listado de tareas
# Tareas:
# - Añadir productos
# - Buscar productos
# - Actualizar precios
# - Eliminar productos
# - Calcular valor total del inventario
# - Interfaz interactiva y validación de datos

# Paso 2: Diseño del programa
# Usaremos un diccionario para el inventario: clave = nombre del producto, valor = (precio, cantidad)

inventario = {}

# Paso 3: Implementación de funciones

def agregar_producto(nombre, precio, cantidad):
    """Agrega un nuevo producto al inventario"""
    if nombre in inventario:
        print("❌ El producto ya existe. Usa otra opción para modificarlo.")
    else:
        inventario[nombre] = (precio, cantidad)
        print(f"✅ Producto '{nombre}' agregado correctamente.")

def buscar_producto(nombre):
    """Busca un producto por nombre y retorna su información"""
    if nombre in inventario:
        precio, cantidad = inventario[nombre]
        print(f"🔎 Producto encontrado: {nombre} - Precio: ${precio:.2f} - Cantidad: {cantidad}")
    else:
        print("❌ Producto no encontrado en el inventario.")

def actualizar_precio(nombre, nuevo_precio):
    """Actualiza el precio de un producto existente"""
    if nombre in inventario:
        _, cantidad = inventario[nombre]
        inventario[nombre] = (nuevo_precio, cantidad)
        print(f"✅ Precio de '{nombre}' actualizado a ${nuevo_precio:.2f}")
    else:
        print("❌ No se puede actualizar. El producto no existe.")

def eliminar_producto(nombre):
    """Elimina un producto del inventario"""
    if nombre in inventario:
        del inventario[nombre]
        print(f"🗑️ Producto '{nombre}' eliminado del inventario.")
    else:
        print("❌ No se puede eliminar. El producto no existe.")

def calcular_valor_total():
    """Calcula el valor total del inventario usando una función lambda"""
    calcular_valor = lambda: sum(precio * cantidad for precio, cantidad in inventario.values())
    valor_total = calcular_valor()
    print(f"💰 Valor total del inventario: ${valor_total:.2f}")

# Paso 4: Interfaz de usuario interactiva

def menu():
    """Muestra el menú principal y gestiona las opciones del usuario"""
    while True:
        print("\n📦 GESTIÓN DE INVENTARIO 📦")
        print("1. Añadir producto")
        print("2. Buscar producto")
        print("3. Actualizar precio de producto")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Ver inventario completo")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            try:
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad disponible: "))
                agregar_producto(nombre, precio, cantidad)
            except ValueError:
                print("⚠️ Precio y cantidad deben ser números válidos.")
        elif opcion == "2":
            nombre = input("Nombre del producto a buscar: ").strip()
            buscar_producto(nombre)
        elif opcion == "3":
            nombre = input("Nombre del producto a actualizar: ").strip()
            try:
                nuevo_precio = float(input("Nuevo precio: "))
                actualizar_precio(nombre, nuevo_precio)
            except ValueError:
                print("⚠️ Ingresa un precio válido.")
        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ").strip()
            eliminar_producto(nombre)
        elif opcion == "5":
            calcular_valor_total()
        elif opcion == "6":
            if not inventario:
                print("📭 El inventario está vacío.")
            else:
                print("📋 Inventario actual:")
                for nombre, (precio, cantidad) in inventario.items():
                    print(f"- {nombre}: Precio ${precio:.2f}, Cantidad: {cantidad}")
        elif opcion == "0":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# Paso 5: Prueba del programa (ejecutamos el menú)
if __name__ == "__main__":
    menu()

# Paso 6: Documentación
# Cada función está comentada para explicar su propósito.
# El programa puede ejecutarse en terminal o IDLE de Python.
# Guarda este archivo como "gestion_inventario_tienda.py"
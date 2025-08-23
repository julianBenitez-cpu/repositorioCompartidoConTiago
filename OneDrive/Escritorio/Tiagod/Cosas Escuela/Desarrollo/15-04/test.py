"""Escribe un programa que administre el inventario de una
tienda. El programa debe permitir agregar nuevos
productos, actualizar las cantidades de los productos
existentes, y mostrar el inventario actual."""

inventario = {}

while True:
    print("Opciones:")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = input("elegi una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        if nombre in inventario:
            print(f"El producto '{nombre}' ya existe, usa otro modo")
        else:
            inventario[nombre] = cantidad
            print(f"Producto '{nombre}' agregado con cantidad {cantidad}.")

    elif opcion == "2":
        nombre = input("Nombre del producto: ")
        if nombre in inventario:
            cantidad = int(input("Nueva cantidad: "))
            inventario[nombre] = cantidad
            print(f"Producto '{nombre}' actualizado. Nueva cantidad: {inventario[nombre]}.")
        else:
            print(f"El producto '{nombre}' no existe, usa otro modo.")

    elif opcion == "3":
        if not inventario:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for nombre, cantidad in inventario.items():
                print(f"- {nombre}: {cantidad}")

    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
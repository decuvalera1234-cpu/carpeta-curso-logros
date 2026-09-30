# Definición de listas globales
compras = []
precios = []

def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")
    producto = input("Dime qué producto vas a llevar: ").strip().lower()
    
    if producto == "":
        print("El nombre del producto no puede estar vacío.")
        return

    try:
        precio = float(input(f"¿Qué precio tiene el producto '{producto}'?: "))
        if precio < 0:
            print("El precio no puede ser negativo.")
            return
        
        compras.append(producto)
        precios.append(precio)
        print(f"¡Producto '{producto}' agregado con éxito!")
    except ValueError:
        print("Error: Ingresa un número válido para el precio.")

def mostrar_cesta():
    print("\n" + "="*50)
    print("="*5 + " Esta es Tu Cesta de inventario pasa por la caja " + "="*5)
    print("="*50)
    
    if len(compras) == 0:
        print("Tu cesta está vacía por ahora.")
    else:
        for i, (prod, prec) in enumerate(zip(compras, precios), start=1):
            print(f"{i}. {prod.capitalize():<20} -> ${prec:.2f}")
    print("="*50)

def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")
    if len(compras) == 0:
        print("No tienes ningún producto en la cesta para eliminar.")
        return

    mostrar_cesta()
    borrar = input("Escribe el nombre del producto a quitar: ").strip().lower()

    if borrar in compras:
        posicion = compras.index(borrar)
        compras.pop(posicion)
        precios.pop(posicion)
        print(f"Entendido, hemos quitado '{borrar}' de tu lista.")
    else:
        print("Ups, ese producto no se encuentra en la cesta.")

def calcular_total():
    print("\n--- TOTAL DE LA COMPRA ---")
    if len(precios) == 0:
        print("El total es $0.00 porque la cesta está vacía.")
    else:
        total = sum(precios)
        print(" "*18 + f"Total: ${total:.2f}")
        print("="*52)

def iniciar_tienda():
    print("==========================================")
    print("     Tienda tu Corazon es mio             ")
    print("==========================================")

    while True:
        print("\n************ MENÚ PRINCIPAL ************")
        print("1. Agregar un nuevo producto")
        print("2. Mostrar el contenido de la cesta")
        print("3. Eliminar un producto")
        print("4. Calcular el total de la compra")
        print("5. Salir / Pasar a caja")
        print("****************************************")

        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_cesta()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            calcular_total()
        elif opcion == "5":
            calcular_total()
            print("\nGracias por tu compra en 'Tienda tu Corazon es mio'. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta eligiendo un número del 1 al 5.")

# Ejecución del programa
if __name__ == "__main__":
    iniciar_tienda()




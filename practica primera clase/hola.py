compras = []
precios = []
total = 0

print("Hola dime que vas a llevar")
while True:
    producto = str(input("Dime que producto vas a llevar al terminar coloca q: ")).lower()
    if producto== "q":
        break
    else:
        precio=float(input(f"Dime que precio tiene el producto {producto}: "))
        compras.append(producto)
        precios.append(precio)
for productos,precio in zip(compras,precios):
    print(f"{productos}: {precio:.2f}")
for precio in precios:
    total += precio
print(f"Total: {total:.2f}")
    
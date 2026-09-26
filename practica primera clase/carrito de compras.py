#Definir variables

compras = []
precios = []
total = 0

print("Tienda tu Corazon es mio")
while True:
    producto=str(input("Dime que producto vas a llevar si ya terminaste coloca q: ")).lower()
   
    if producto == "q":
        break
    
    else:

        precio = float(input(f"Que precio tiene el producto {producto}: "))
        compras.append(producto)
        precios.append(precio)
print("="*50)
print("="*5,"Esta es Tu Cesta de inventario pasa por la caja","="*5)

for productos,precio in zip(compras, precios):
    print(" "*18, f"{productos}: {precio:.2f}")
    print("="*50)
for precio in precios:
    total += precio
print(" "*18, f"Total: {total:.2f}")
print("="*52)






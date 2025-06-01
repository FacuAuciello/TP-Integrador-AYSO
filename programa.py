precio = float(input('Ingrese el precio del producto: '))
descuento = float(input('Ingrese el descuento en porcentaje: '))
impuestos = float(input('Ingrese los impuestos en porcentaje: '))

precio_con_descuento = precio - (precio * descuento / 100)
precio_final = precio_con_descuento + (precio_con_descuento * impuestos / 100)

print(f'El precio final es: {precio_final}')

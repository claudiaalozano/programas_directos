precio = float(input("Introduzca el precio del producto: "))
iva = (precio * 21 ) / 100 
precio_iva = precio + iva
vivienda = input("¿Que tipo de vivienda quiere calcular para el ibi? (casa/terreno):")
if vivienda == "casa":
    print("Usted debe pagar un total de (...) ")
if vivienda == "terreno":
    print("Usted debe de pagar un total de (...) ")
# programas_directos
He realizado 5 progamas directos en python.

Ejercicio 8: Porcentajes, IVA e inversiones

1. Escribir un algoritmo que calcula el precio con todos los impuestos incluidos (TII) para un precio sin impuestos y un porcentaje de IVA dado.

2. Escribir un algoritmo que calcula el importe de los intereses generados por un capital invertido a un interés dado durante un tiempo dado, expresado en meses.

```precio = float(input("Introduzca el precio del producto: "))
iva = (precio * 21 ) / 100 
precio_iva = precio + iva
vivienda = input("¿Que tipo de vivienda quiere calcular para el ibi? (casa/terreno):")
if vivienda == "casa":
    print("Usted debe pagar un total de 300€ ")
if vivienda == "terreno":
    print("Usted debe de pagar un total de 150€ ")´´´
    
    
Ejercicio 9: Media aritmética ponderada

1. Escribir un algoritmo que calcula la media aritmética de tres números dados.

2. La misma pregunta para una media ponderada cuando se dan los números y los coeficientes de ponderación.

```numero1= float(input("Introduzca el primer número: "))
numero2= float(input("Introduzca el segundo número: "))
numero3= float(input("Introduzca el tercer número: "))
media = (numero1+ numero2 + numero3) / 3

print ("La media aritmética es: " , media )
mediaponderada = round (media)
print ("La media ponderada es: " , mediaponderada)´´´



Ejercicio 10: Área del triángulo

1. Escribir un algoritmo que calcula el área de un triángulo del que se da la medida de un lado y la de la altura relativa a este lado.

2. ¿Se puede utilizar este algoritmo para un triángulo rectángulo si se dan las medidas de sus dos lados perpendiculares?
Si, debido a que un lado se toma como base y otro como la altura.

```altura = float(input("Introduzca cuanto mide la altura del triángulo: "))
base = float(input("Introduzca cuanto mide la base del triángulo: "))
area= (altura * base) / 2
print ("El área del triángulo es: " , area)
´´´


Ejercicio 11: Salario y horas extra

El cálculo de una nómina tiene en cuenta el salario bruto asociado a las horas «normales» que debe hacer el empleado y las horas «extra» trabajadas en el mes. Las horas extra se remuneran según las siguientes normas administrativas:

Tarifa por hora aumentada en un 125 % para las horas entre la 36.ª y la 43.ª.

Tarifa por hora aumentada en un 150 % para las horas a partir de la 44.ª.

El aumento se realiza sobre la tarifa por hora normal, calculado a partir del salario mensual bruto para un año de 52 semanas repartidas en 12 meses, sobre la base de 35 horas trabajadas por semana.

Escribir el algoritmo que calcula el importe de las horas extra que hay que pagar, a partir del salario mensual bruto y de la cantidad de horas extra.

Se podrá suponer que el cálculo siempre se usa para una cantidad de horas superior a 8. El problema general supone el estudio previo del capítulo siguiente, que trata de la alternativa.

Encontrará una solución propuesta para este ejercicio en los elementos complementarios de este libro que están disponibles para descargar desde la página Información.

```horas= int(input("Introduzca las horas extra que ha trabajado en este mes:"))
#se cobra la hora a 17 euros
horas_totales= horas + 35
if horas_totales > 36 and horas_totales < 43:
    horas_extra = float((horas * 17 )) * 1.25
    sueldo = (35 * 17) + horas_extra
    print("Usted ha trabajado un total de horas extra de " , horas , "por lo que su sueldo ha ascendido a un total de " , sueldo , ", y ha trabajado un total de " , horas_totales , "horas.")
if horas_totales >= 44:
    horas_extra2 = float((horas * 17)) * 1.50
    sueldo2 = (35 * 17) + horas_extra2
    print("Usted ha trabajado un total de horas extra de " , horas , "por lo que su sueldo ha ascendido a un total de " , sueldo2 , ", y ha trabajado un total de " , horas_totales , "horas.")
    ´´´



Ejercicio 12: Cuenta de depósito

Se considera las cuentas de depósitos alojadas en un banco por los clientes. Solo se permite hacer una retirada si el saldo que queda en la cuenta no es negativo.

1. Definir el tipo de datos CUENTA..

2. Definir las operaciones aplicables.

En determinadas circunstancias y para determinados clientes, la banca autoriza un descubierto limitado y temporal.

3. Volver a hacer las definiciones previas para permitir estos descubiertos.

El ejercicio está parcialmente resuelto en los elementos complementarios de este libro que están disponibles para descargar desde la página Información.

```cuenta = input("Desea abrir una cuenta en el banco (si/no): ")

if cuenta == "no":
    print("Usted no desea abrir una cuenta en nustro banco. Muchas gracias.")
if cuenta == "si":
    saldo = 0
    print("Primero debe abonar dinero en la cuenta.")
    abono= int(input("Introduzca el dinera desea abonar:"))
    saldo = abono

operacion = input("¿Desea hacer otra operación más como consultar dinero,retirar o abonar?")
if operacion == "no":
    print("Vale gracias por consultar este banco. Hasta pronto.")
if operacion == "abonar":
    introducir_dinero= float(input("Introduzca el dinero de desea ingresar en la cuenta: "))
    saldo = saldo + introducir_dinero
    print("Su saldo es de " , saldo , "€")
if operacion == "consultar":
    print("El saldo de su cuenta es " , saldo , "€")
if operacion == "retirar":
    retirar_dinero= float(input("Introduzca el dinero que desea retirar: "))
    saldo = saldo - retirar_dinero
    if saldo >= 0:
        print("Con la retirada de " , retirar_dinero , " su saldo disminuye a un total de " , saldo , "€")
    if saldo < 0:
        saldo = saldo * -1
        print("Con la retirada de " , retirar_dinero ,"Usted no tiene saldo en la cuenta, además debe un total de  " , saldo , "€")
        ´´´

numeros=[]
numero1= numeros.append(float(input("Introduzca el primer número: ")))
numero2= numeros.append(float(input("Introduzca el segundo número: ")))
numero3= numeros.append(float(input("Introduzca el tercer número: ")))
suma= 0
for i in numeros:
    suma = i + suma

suma = suma / 3 
print ("La media aritmética es: " , suma )
suma = round (suma)
print ("La media ponderada es: " , suma)
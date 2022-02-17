numeros=[]
numero1= numeros.append(float(input("Introduzca el primer número: ")))
numero2= numeros.append(float(input("Introduzca el segundo número: ")))
numero3= numeros.append(float(input("Introduzca el tercer número: ")))
suma= 0
for i in range(numeros):
    suma = i + numeros

suma = suma / 3 
print ("La media aritmética es: " , suma )

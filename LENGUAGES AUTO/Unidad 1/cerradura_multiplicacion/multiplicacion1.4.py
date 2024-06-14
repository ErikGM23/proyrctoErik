num1 = float(input("Ingresa tu primer numero: "))
num2 = float(input("Ingresa tu segundo numero: "))
multiplicacion = num1 * num2

#verifica si la suma es un numero entero o  no 
if multiplicacion.is_integer():
    resultado = "entero"
else:
    resultado = "racional"
print ()

print("el resultado de la suma es:", multiplicacion)
print("el resultado es un numero: ", resultado)

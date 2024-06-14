#Comprovacion de la propiedad con cerradura de suma 
print("cerradura: la suama de dos numeros reales siempre da como resultado otro numero real")
print ("a + b pertenece R")
print ()


#se imprimira el menaje que indica que se demostratra la propiedad de la cerradura 
print ("El programa a continuacion realiza la propiedad de la cerradura: ")
print ()#linea vacia 

num1 = float(input("Ingresa tu primer numero: "))
num2 = float(input("Ingresa tu segundo numero: "))
suma = num1 + num2

#verifica si la suma es un numero entero o  no 
if suma.is_integer():
    resultado = "entero"
else:
    resultado = "racional"
print ()

print("el resultado de la suma es:", suma)
print("el resultado es un numero: ", resultado)


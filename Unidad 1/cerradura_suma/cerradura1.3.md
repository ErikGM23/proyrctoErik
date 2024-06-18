num1 = float(input("ingresa el primer numero")) 
num2 = float(input("ingresa el segundo numero")) 
if num1 > num2: 
    print("el primer numero ({}) es mayor que el segundo numero ({})".format(num1, num2))
elif num1 < num2:
    print("el segundo numero ({}) es mayor que el primer numero ({})".format(num2, num1))
else:
    print("ambos numeros son iguales")
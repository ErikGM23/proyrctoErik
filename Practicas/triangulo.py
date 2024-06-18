import math

def calcular_lado_faltante():
    print("Introduce los valores de los dos lados de un triangulo rectangulo")
    print("Deja en blanco elvalor del lado que deseas")

    a = input("Lado a (cateto): ")
    b = input("Lado b (cateto): ")
    c = input("Lado c (hipotenusa): ")

    def calcular_lado_faltante():

        #convertir las entradas a numeros, si se 
        a = float (a) if a else None
        b = float (b) if b else None
        c = float (c) if c else None

    #calcula el lado flotante usando el teorema 
    if a is None and b is not None and c is not None
    a = math.sqrt(c**2 - b**2)
    elif b is None and a is not None and c is not None
b = math.sqrt(c**2 - a**2)
elif c is None and a is not None and b is not None
c = math.sqrt(a**2 + b**2)
\end{code}



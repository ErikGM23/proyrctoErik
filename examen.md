Erik Daniel Galicia Moreno 

4.- ¿Qué es un alfabeto en la teoría de lenguajes formales? 
R= Es una secuencia ordenada de elementos que pertenecen a un cierto lenguaje formal o alfabeto análogas 
9.- Defina qué es una cadena
R= Es una secuencia ordenada que contiene números, caracteres, letras, oraciones etc
10.- Genera un código en Python demuestre todos los conceptos anteriores (comenta donde se encuentra cada uno de los conceptos) 

# Define un alfabeto como un conjunto de simbolos 
Alfabeto = {'a', 'b', 'c', 'd', 'e'}

# Definir una cadena como una secuencia de símbolos del alfabeto
Cadena = 'abcde'

# Definir una cadena como una secuencia de símbolos del alfabeto cadena 
if set(Cadena).issubset(Alfabeto):
    print("La cadena es una palabra válida sobre el alfabeto.")
else:
    print("La cadena contiene símbolos que no están en el alfabeto.")

# Imprime el alfabeto y la cadena.
print("Alfabeto :", Alfabeto)
print("Cadena:", Cadena)


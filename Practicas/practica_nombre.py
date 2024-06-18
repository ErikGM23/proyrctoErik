nombre = input("Ingresa tu nombre")
import random 
input = nombre
saludos=[
    "Bienenido " +nombre+",te saluda las poderosas Aguilas del America",
    "Hola " +nombre+", en que te puedo servir?",
    "Es un placer tenerte de nuevo " +nombre+", patron",
]
indice=random.randint(0,len(saludos)-1)
print(saludos[indice])

"""numero mayor y menor"""
numero1 = int(input("ingrese un numero"))
numero2 = int(input("ingrese el segundo numero"))

if numero1 < numero2:
    print(numero1, " es menor a " , numero2)
elif numero1 > numero2:
    print(numero1, " es mayor a " , numero2)
else:
    print(numero1, " y " ,numero2 , " son iguales") 

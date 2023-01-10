
"""escriba programa que solicite contraseña"""

contraseña = int (input("ingrese la contraseña"))
repetir = int(input("ingrese de nuevo "))
while contraseña != repetir:
    contraseña= int(input("ingrese la contraseña"))
    repetir = int(input("ingrese de nuevo "))
print("la contraseña es correta")

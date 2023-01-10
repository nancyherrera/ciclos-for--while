"""precio video juegos """

nombre = input("ingrese su nombre")
edad = int(input("ingrese su edad"))

if edad <= 10 :
    print(nombre, " Tu entrada es gratis ")
elif edad >=11 and edad <=18:
    print(nombre,  " Debe pagar 24.660 ")
else:
    print(nombre, "Debe pagar 48000") 
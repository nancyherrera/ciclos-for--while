"dias semana"

diaSeman = input("ingresa un dia de la semana")

if diaSeman == "lunes":
    print("hoy es " ,diaSeman, " es un dia maravilloso para empezar semana")
elif diaSeman == "viernes":
    print("Hoy es " ,diaSeman, " termina tu semana regular con toda la energia")
elif diaSeman == "sabado" or "domingo":
    print("Hoy es " ,diaSeman, " disfruta tu fin de semana")
else:
    print("este dia no tiene mensaje")
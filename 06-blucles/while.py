contador = 1
while contador <= 100:
    print(contador)
    contador += 1


number = int(input("¿Que numero quieres multiplicar?: "))

if number < 1:
    number = 1



contador = 1
while contador <= 10:
    print(f"{number} x {contador} = {number * contador}")
    contador += 1
else:
    print("La tabla ha finalizado")
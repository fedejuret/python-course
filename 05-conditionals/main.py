# Condicionales IF
"""
Operadores de comparacion
Los mismos en php, js, etc

==
!=
>
<
<=
>=

"""

color = "yellow"

if color == "red":
    print("Yes! The color is red")
else:
    print("Noup :< The color not is red")


year = 2020
#year = int(input("¿Que año es?: "))

if year >= 2021:
    
    print("Si, es mayor o igual")
else:
    print("No, no es mayor ni igual. Es 2020")


name = input("¿Cual es tu nombre?: ")
city = input("¿Cual es tu ciudad?: ")
mayor = int(input("¿Que edad tienes?: "))

if city == "Guatrache":
    if mayor >= 18:
        print(f"Hey! {name} de {city}! Eres mayor de edad")
    else:
        print(f"Hey! {name} Eres menor de edad :C")
else:
    print(f"Hey! {name} Solo personas de Guatraché pueden usar este programa")


"""
ELIF -> Es como el else if de java

"""

# OPERADORES LOGICOS

# and = &&
# or = ||
# ! = denegacion
# not = no

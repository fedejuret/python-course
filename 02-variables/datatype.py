# indicate que esta variable no tiene nada
nothing = None

string = "Esto es un string"
integer = 99
floatNumber = 99.5

# La primer letra con MAYUSCULA
boolean = True # o False

# Arrays | Lista | Arreglo
lista = [10, 20, 30, 100, 200]
lista = [10, "veinte", 22.5]

# Tupla = Tipo de datos que NO CAMBIA
tupla = ("Master", "en", "python")

# Permite tener clave y valor. Tipo hashmap o JSON
diccionario = {
    "name": "Federico",
    "surname": "Juretich"
}

# Imprime un rango del 0 al 9
rango = range(9)

# Tipo de dato Bytes
byte = b"Test"

# mostrar el tipo de dato
print(type(nothing))
print(type(string))
print(type(floatNumber))
print(type(integer))
print(type(boolean))
print(type(lista))
print(type(tupla))
print(type(diccionario))
print(type(rango))
print(type(byte))

# probar concatenar distintos tipos de datos
# Utilizar str para convertir un numero a un string
# Tipo IntegerParse, StringParse
texto = "This is a text"
number = str(255)

print(texto + " " + number)

# Forzar nuevamente a entero
number = int(255)

# Para utilizar comillas dentro de un string hay que agregar la barra \" TEXTO AHI\"
comillasInside = "Hello \"how\" are you my friend?"
"""
for variable in elemento


"""

contador = 0
cantidad_de_iter = 0
for contador in range(0, 10):
    print("Voy por el " + str(contador))
    cantidad_de_iter += 1


# Ejemplo
print("\n ############### Example #############")

number = int(input("Coloca un numero: "))

if number < 1:
    number = 1

print(f"### Tabla de multiplicar del numbero {number} ###")

for numbero_tabla in range(0, 11):
    print(f"{number} x {numbero_tabla} = {number * numbero_tabla}")
else:
    print("Tabla finalizada")
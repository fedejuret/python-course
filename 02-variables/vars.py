name = "Federico"
surname = "Juretich"

# Concatenacion simple
print("Hey! My name is " + name + " " + surname)

# Para poder usar la interpolacion es necesario agregar la "f" antes del texto
print(f"Hey! My name is {name} {surname}")

# Utilizando .format 
print("Hey! my name is {} {}".format(name, surname))

# Utilizando comas {NO ES CONCATENACION}
print(name, surname)
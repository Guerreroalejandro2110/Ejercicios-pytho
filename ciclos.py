# Ejercicio Alejandro Guerrero

i = 1

while i <= 100:  # Rango del ciclo
    if i % 3 == 0 and i % 5 == 0:  # condicion para multiplos de 3 y 5
        print("FIZZ BUZZ", end="\n\n")
    elif i % 3 == 0:  # condicion para multiplos de 3
        print("FIZZ", end="\n\n")
    elif i % 5 == 0:  # condicion para multiplos de 5
        print("BUZZ", end="\n\n")
    else:
        print(i, end="\n\n")
    i += 1

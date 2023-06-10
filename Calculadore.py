N1 = input("Ingrese primer numero")
N2 = input("Ingrese segundo numero")

N1 = int(N1)
N2 = int(N2)
Mensaje = str

Suma = N1 + N2
Resta = N1 - N2
Multi = N1 * N2
Div = N1 / N2
Res = N1 & N2
Potencia = N1**N2
Comparar = N1 >= N2

Mensaje = f"""
Para {N1} y {N2}
El resultado de suma es {Suma} 
El resultado de resta es {Resta}
El resultado de multiplicacion es {Multi}
El resultado de division es {Div}
El resultado dEl residuo es {Res}
El resultado de la potencia es {Potencia} 
El numero mayor es {Comparar}
"""

print(Mensaje)

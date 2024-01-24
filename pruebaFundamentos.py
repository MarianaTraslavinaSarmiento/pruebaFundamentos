
voltaje = 0

for x in range(5):
    voltajeUsuario = float(input(f"Ingresar voltaje {x+1}: "))
    voltaje += voltajeUsuario

promedio = voltaje/5

if promedio > 220:
    print ("ALTO VOLTAJE")

else:
    print("VOLTAJE CORRECTO")

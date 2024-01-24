
voltaje = 0 

for x in range (3):
    voltajeUsuario = float(input(f"Ingrese voltaje {x+1}: "))
    voltaje += voltajeUsuario

promedio = round((voltaje/3),2)
print(f"El promedio de los voltajes es {promedio}")

if (promedio < 115):
    print("VOLTAJE CORRECTO")

if (promedio>115) and (promedio<220):
    print("ALTO VOLTAJE")

if (promedio>220):
    print("PELIGRO")
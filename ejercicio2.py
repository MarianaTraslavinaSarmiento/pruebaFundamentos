

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

areaTriangulo = (base*altura)/2

if areaTriangulo>1000:
    print("DATOS NO VÁLIDOS")
else:
    print(f"El área del triángulo es {areaTriangulo}")

   
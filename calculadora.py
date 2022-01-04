

numerox = float(input("Introduzca un numero"))

numeroy = float(input("Introduzca otro numero"))

calcular = str(input("Ahora introduzca la operacion a realizar: +,-,*,/"))


if calcular == "+":
    suma = numerox + numeroy
    print(suma)
    
elif calcular == "-":
    resta = numerox - numeroy
    print(resta)

elif calcular == "*":
    multiplicacion = numerox * numeroy
    print(multiplicacion)

elif calcular == "/":
    division = numerox / numeroy
    print(division)
    
else:
    print("Solo puedo hacer ciertas operaciones")

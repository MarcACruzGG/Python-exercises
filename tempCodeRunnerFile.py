
a = int(input("Dame un numero\n"))
positivos = 0   
negativos = 0
while a != 0:
    if a > 0:
        positivos += 1
    elif a < 0:
        negativos += 1
    a = int(input("Dame otro numero\n"))
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")


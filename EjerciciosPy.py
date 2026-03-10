# ==========================================================
# BLOQUE 1
# EJERCICIOS 1 - 10
# FUNDAMENTOS DE PYTHON
#
# Temas:
# - Operaciones aritméticas
# - Entrada de datos con input()
# - Salida con print()
# - Manipulación básica de cadenas
# - Indexación y slicing
# - Listas básicas
# ==========================================================

# ==============================
# Ejercicio 1
# Lee dos números enteros desde teclado.
# Imprime:
# 1. La suma
# 2. La resta
# 3. La multiplicación
# 4. La división real
# 5. La división entera
# 6. El residuo
# Cada resultado debe imprimirse en una línea distinta.
# ==============================

num1 = int(input("Ingresa un numero \n"))
num2 = int(input("Ingresa otro numero \n"))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)

# ==============================
# Ejercicio 2
# Lee tres números enteros desde teclado.
# Imprime los tres números en la misma línea
# sin espacios entre ellos.
# ==============================

num1 = int(input("Dame el primer numero (1 / 3)\n"))
num2 = int(input("Dame el segundo numero (2 / 3)\n"))
num3 = int(input("Dame el tercer numero (3 / 3)\n"))
print(num1,num2,num3,sep="")

# ==============================
# Ejercicio 3
# Lee dos valores desde teclado.
# Intercambia sus valores.
# Después imprime los valores intercambiados.
# ==============================


num1 = int(input("Dame el primer numero (1 / 2)\n"))
num2 = int(input("Dame el segundo numero (2 / 2)\n"))

print("Los valores del numero han sido modificados tu numero uno es:", num2, "\nY tu numero numero dos es:", num1)


# ==============================
# Ejercicio 4
# Lee una cadena de texto.
# Imprime:
# 1. La cadena en mayúsculas
# 2. La cadena en minúsculas
# 3. La longitud de la cadena
# ==============================

cadena=input("Ingresa una cadena de texto para modificarla: \n")

print("El texto en mayuscula es:", cadena.upper())
print("El texto en minuscula es: ", cadena.lower())
print("El texto tiene", len(cadena))


# ==============================
# Ejercicio 5
# Lee una cadena de texto.
# Imprime:
# 1. El primer carácter
# 2. El último carácter
# 3. El tercer carácter
# 4. El antepenúltimo carácter
# ==============================

cadena=input("Ingresa una cadena de texto: \n")

print(cadena[0])
print(cadena[-1])
print(cadena[2])
print(cadena[-3])


# ==============================
# Ejercicio 6
# Lee una cadena de texto.
# Imprime:
# 1. Los primeros 3 caracteres
# 2. Los últimos 3 caracteres
# 3. Los caracteres del índice 2 al 5
# 4. La cadena invertidas
# ==============================

cadena=input("Ingresa una cadena de texto: \n")

print(cadena[:3])
print(cadena[-3:])
print(cadena[1:5])
print(cadena[::-1])


# ==============================
# Ejercicio 7
# Lee 5 números enteros desde teclado
# y guárdalos en una lista.
# Imprime:
# 1. La lista completa
# 2. El primer elemento
# 3. El último elemento
# 4. La suma de todos los elementos
# ==============================

a=int(input("Ingresa el primer numero \n"))
b=int(input("Ingresa el segundo numero \n"))
c=int(input("Ingresa el tercero numero \n"))
d=int(input("Ingresa el cuarto numero \n"))
e=int(input("Ingresa el quinto numero \n"))

mi_lista = [a,b,c,d,e]

print(mi_lista)
print(mi_lista[0])
print(mi_lista[-1])
print(sum(mi_lista))

# ==============================
# Ejercicio 8
# Lee 4 palabras desde teclado
# y guárdalas en una lista.
# Cambia la segunda palabra por "Python".
# Imprime la lista resultante.
# ==============================

a=input("Ingresa una palabra \n")
b=input("Ahora otra \n")
c=input("Ahora otra \n")
d=input("Ya la ultima te lo prometo \n")

mi_lista = [a,b,c,d]
mi_lista[1] = 'Python'
print(mi_lista)



# ==============================
# Ejercicio 9
# Lee 6 números enteros
# y guárdalos en una lista.
# Imprime:
# 1. El segundo número
# 2. El cuarto número
# 3. El último número
# ==============================

a=int(input("Ingresa el primer numero \n"))
b=int(input("Ingresa el segundo numero \n"))
c=int(input("Ingresa el tercero numero \n"))
d=int(input("Ingresa el cuarto numero \n"))
e=int(input("Ingresa el quinto numero \n"))
f=int(input("Ingresa el sexto numero \n"))

mi_lista = [a,b,c,d,e,f]

print(mi_lista[1])
print(mi_lista[3])
print(mi_lista[-1])

# ==============================
# Ejercicio 10
# Lee una cadena de texto desde teclado.
# Imprime:
# 1. La cantidad de caracteres
# 2. El primer carácter
# 3. El último carácter
# 4. La cadena repetida 3 veces
# ==============================

cadena=input("Ingresa una cadena de texto: \n")

print(len(cadena))
print(cadena[0])
print(cadena[-1])
print(cadena*3)

# ==========================================================
# BLOQUE 2
# EJERCICIOS 11 - 20
# OPERADORES Y EXPRESIONES LÓGICAS
#
# Temas:
# - Operadores relacionales
# - Operadores lógicos (and, or)
# - Tipo de dato booleano (True / False)
# - Evaluación de condiciones
# - Expresiones lógicas
# ==========================================================


# ==============================
# Ejercicio 1
# Lee dos números enteros.
# Imprime:
# 1. Si el primero es mayor que el segundo
# 2. Si el primero es menor que el segundo
# 3. Si ambos números son iguales
# ==============================

a=int(input("Ingresa el primer numero \n"))
b=int(input("Ingresa el segundo numero \n"))

print(a>b)
print(a<b)
print(a==b)



# ==============================
# Ejercicio 2
# Lee un número entero.
# Imprime:
# 1. Si el número es mayor que 10
# 2. Si el número es menor o igual a 10
# ==============================


a=int(input("Ingresa el primer numero \n"))

print(a>10)
print(a<=10)

# ==============================
# Ejercicio 3
# Lee tres números enteros.
# Imprime:
# 1. Si el primer número es mayor que el segundo
# 2. Si el segundo número es menor que el tercero
# ==============================


a=int(input("Ingresa el primer numero \n"))
b=int(input("Ingresa el segundo numero \n"))
c=int(input("Ingresa el tercero numero \n"))

print(a>b)
print(b<c)



# ==============================
# Ejercicio 4
# Lee dos números enteros.
# Imprime:
# 1. Si ambos números son positivos
# ==============================

a=int(input("Ingresa el primer numero \n"))
b=int(input("Ingresa el segundo numero \n"))

print(a>=0 and b>=0)


# ==============================
# Ejercicio 5
# Lee dos números enteros.
# Imprime:
# 1. Si al menos uno de los números es mayor que 100
# ==============================


a=int(input("Ingresa el primer numero \n"))
b=int(input("Ingresa el segundo numero \n"))

print(a>100 or b>100)

# ==============================
# Ejercicio 6
# Lee tres números enteros.
# Imprime:
# 1. Si los tres números son iguales
# ==============================

a=int(input("Ingresa el primer numero \n"))
b=int(input("Ingresa el segundo numero \n"))
c=int(input("Ingresa el tercero numero \n"))

print(a==b and b==c and c==a)

# ==============================
# Ejercicio 7
# Lee un número entero.
# Usa operadores de asignación para:
# 1. Sumarle 5
# 2. Multiplicarlo por 2
# 3. Restarle 3
# Imprime el resultado final
# ==============================


a=int(input("Ingresa el primer numero \n"))

a += 5
a *= 2
a -= 3

print (a)


# ==============================
# Ejercicio 8
# Lee dos números enteros.
# Guarda en una variable lógica el resultado de:
# el primer número es mayor que el segundo.
# Imprime esa variable.
# ==============================

a=int(input("Ingresa el primer numero \n"))
b=int(input("Ingresa el segundo numero \n"))

c = (a > b)

print(c)

# ==============================
# Ejercicio 9
# Lee tres números enteros.
# Crea una expresión lógica que verifique:
# el primero es mayor que el segundo
# Y el segundo es mayor que el tercero.
# Imprime el resultado.
# ==============================

a=int(input("Ingresa el primer numero \n"))
b=int(input("Ingresa el segundo numero \n"))
c=int(input("Ingresa el tercero numero \n"))

d=(a>b)and(b>c)
print(d)

# ==============================
# Ejercicio 10
# Lee dos números enteros.
# Imprime el resultado lógico de:
# el primero es mayor que 10
# Y el segundo es menor que 20
# ==============================

a=int(input("Ingresa el primer numero \n"))
b=int(input("Ingresa el segundo numero \n"))

c=(a>10)and(b<20)

print(c)

# ==========================================================
# BLOQUE 3
# EJERCICIOS 21 - 30
# SENTENCIAS CONDICIONALES
#
# Temas:
# - Sentencia if
# - Sentencia else
# - Sentencia elif
# - Evaluación de condiciones
# - Control de flujo del programa
# ==========================================================

# ==============================
# Ejercicio 1
# Lee un número entero.
# Si el número es mayor que 0
# imprime "Numero positivo".
# ==============================

a=int(input("Ingresa un número entero: \n"))

if a > 0 :
    print("El numero es positivo")


# ==============================
# Ejercicio 2
# Lee un número entero.
# Si el número es menor que 0
# imprime "Numero negativo".
# Si no
# imprime "No es negativo".
# ==============================


a = int(input("Ingresa un numero entero: \n"))

if a < 0:
    print("El numero es negativo")
else:
    print("El numero no es negativo")


# ==============================
# Ejercicio 3
# Lee un número entero.
# Si el número es par
# imprime "Numero par".
# Si no
# imprime "Numero impar".
# ==============================

a = int(input("Ingresa un numero entero: \n"))

if a % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

# ==============================
# Ejercicio 4
# Lee un número entero.
# Si el número es mayor que 10
# imprime "Mayor que 10".
# Si es igual a 10
# imprime "Es 10".
# Si no
# imprime "Menor que 10".
# ==============================

a = int(input("Ingresa un numero entero: \n"))

if a > 10:
    print("El numero es mayor a 10")
elif a == 10:
    print("El numero es 10")
else:
    print("El numero es menor a 10")

# ==============================
# Ejercicio 5
# Lee dos números enteros.
# Si el primero es mayor que el segundo
# imprime "El primero es mayor".
# Si no
# imprime "El segundo es mayor o igual".
# ==============================

a = int(input("Ingresa un numero entero: \n"))
b = int(input("Ingresa un numero entero: \n"))

if a>b:
    print("EL perimero es mayor")
else:
    print("El segundo numero es mayor o igual")

# ==============================
# Ejercicio 6
# Lee una edad.
# Si la edad es mayor o igual a 18
# imprime "Mayor de edad".
# Si no
# imprime "Menor de edad".
# ==============================

a = int(input("Ingresa tu edad: \n"))

if a >= 18 :
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# ==============================
# Ejercicio 7
# Lee una edad.
# Si la edad es mayor o igual a 18
# imprime "Adulto".
# Si la edad es mayor que 12
# imprime "Adolescente".
# Si no
# imprime "Niño".
# ==============================

a = int(input("Ingresa tu edad: \n"))

if a >= 18 :
    print("Adulto")
elif a > 12:
    print("Adolescente")
else:
    print("Niño")

# ==============================
# Ejercicio 8
# Lee un número entero.
# Si el número es mayor que 100
# imprime "Numero grande".
# Si el número es mayor que 50
# imprime "Numero mediano".
# Si no
# imprime "Numero pequeño".
# ==============================


a = int(input("Ingresa un numero: \n"))

if a > 100 :
    print("Numero grande")
elif a > 50:
    print("Numero mediano")
else:
    print("Numero pequeño")



# ==============================
# Ejercicio 9
# Lee dos números.
# Si ambos son positivos
# imprime "Ambos positivos".
# Si no
# imprime "Alguno no es positivo".
# ==============================

a = int(input("Ingresa un numero entero: \n"))
b = int(input("Ingresa un numero entero: \n"))

if a > 0 and b > 0:
    print("Ambos son numeros positivos")
else:
    print("Algun numero no es positivo")


# ==============================
# Ejercicio 10
# Lee un número entero.
# Si el número es mayor que 0
# y menor que 100
# imprime "Numero dentro del rango".
# Si no
# imprime "Numero fuera del rango".
# ==============================

a = int(input("Ingresa un numero: \n"))

if a > 0 and a < 100:
    print("Numero dentro del rango")
else:
    print("Numero fuera del rango")


# ==========================================================
# BLOQUE 4
# EJERCICIOS 31 - 40
# BUCLES WHILE
#
# Temas:
# - Repetición de instrucciones
# - Condiciones de parada
# - Contadores
# - Iteraciones controladas
# ==========================================================


# ==============================
# Ejercicio 1
# Imprime los números del 1 al 10
# usando while.
# ==============================

a = 1
while a <= 10:
    print("Iteracion",a)
    a += 1

# ==============================
# Ejercicio 2
# Imprime los números del 10 al 1
# usando while.
# ==============================

a = 10
while a >= 1:
    print("Iteracion",a)
    a -= 1

# ==============================
# Ejercicio 3
# Imprime todos los números pares
# del 1 al 20 usando while.
# ==============================

a = 0
while a <= 20:
    if a % 2 == 0:
        print('Par', a)
    a += 1

# ==============================
# Ejercicio 4
# Pide números al usuario
# mientras el número sea positivo.
# Cuando ingrese un número negativo
# el programa termina.
# ==============================

a = int(input("Ingresa un numero\n"))

while a >= 0:
    a = int(input("Ingresa un numero\n"))
print("Se rompio")

# ==============================
# Ejercicio 5
# Pide un número entero.
# Imprime ese número
# repetido 5 veces usando while.
# ==============================


a = int(input("Ingresa un numero\n"))

contador = 0

while contador < 5:
    print(a)
    contador += 1


# ==============================
# Ejercicio 6
# Imprime los números del 1 al 50
# pero salta el número 25 usando continue.
# ==============================


a = 0
while a < 50:
    a += 1
    if a == 25:
        continue
    print(a)   


# ==============================
# Ejercicio 7
# Imprime los números del 1 al 10
# pero detén el bucle cuando el número sea 7
# usando break.
# ==============================

a = 0
while a <= 10:
    a += 1
    if a == 7:
        break
    print(a)   

# ==============================
# Ejercicio 8
# Usa un while con else.
# Imprime los números del 1 al 5.
# Cuando el bucle termine naturalmente
# imprime "Bucle terminado".
# ==============================

a = 0
while a < 5:
    a += 1
    print(a)
else:
    print("Bucle terminado")

# ==============================
# Ejercicio 9
# Usa un while que reciba números
# hasta que el usuario escriba 0.
# Cuando ocurra, termina el bucle.
# ==============================


a = int(input("Ingresa un numero\n"))

while a != 0:
    a = int(input("Ingresa un numero\n"))
print("Se rompio")


# ==============================
# Ejercicio 10
# Crea un while con pass
# dentro de un if que verifique
# si el número es igual a 3.
# ==============================

a = 0
while a < 50:
    a += 1
    if a == 3:
        pass
    print(a)   


# ==========================================================
# BLOQUE 5
# EJERCICIOS 41 - 50
# CONTROL DE FLUJO EN BUCLES
#
# Temas:
# - Uso de break
# - Uso de continue
# - Uso de pass
# - Uso de else en bucles
# - Control avanzado de iteraciones
# ==========================================================



# ==============================
# Ejercicio 1
# Imprime los números del 1 al 20
# e imprime solo los pares usando if.
# ==============================

a = 0
while a <=  20:
    if a % 2 == 0:
        print("El numero es par",a)
    a += 1
    
# ==============================
# Ejercicio 2
# Imprime los números del 1 al 10.
# Si el número es múltiplo de 3
# imprime "Multiplo de 3".
# ==============================

a = 0
while a <  10:
    a += 1
    if a % 3 == 0:
        print(f"El numero {a}, es multiplo de 3")
    else:
        print(a)

# ==============================
# Ejercicio 3
# Pide números al usuario.
# Si el número es positivo
# imprímelo.
# Si es negativo
# termina el programa.
# ==============================

a = int(input("Ingresa un numero\n"))

while a >= 0:
    print(a)
    a = int(input("Ingresa un numero\n"))
print("Se rompio")


# ==============================
# Ejercicio 4
# Imprime números del 1 al 20.
# Si el número es 10
# usa break para terminar el bucle.
# ==============================

a = 0
while a < 20:
    a += 1
    if a == 10:
        break
    print(a)   


# ==============================
# Ejercicio 5
# Imprime números del 1 al 20.
# Si el número es par
# imprímelo.
# Si no
# usa continue.
# ==============================

a = 0
while a <  20:
    a += 1
    if a % 2 == 0:
        print("El numero es par",a)
    else: continue
    

# ==============================
# Ejercicio 6
# Pide números al usuario.
# Si el número es 0
# termina el bucle.
# Si el número es positivo
# imprime "Positivo".
# Si no
# imprime "Negativo".
# ==============================

a = int(input ("Dame un numero \n"))

while a != 0:
    if a > 0:
        print("Positivo")
    else:
        print('Negativo')
    a = int(input ("De new viejo \n"))   
print("Morimo \n")


# ==============================
# Ejercicio 7
# Imprime los números del 1 al 15.
# Si el número es divisible entre 5
# imprime "Multiplo de 5".
# ==============================

a = 0

while a < 15:
    a += 1
    if a % 5 == 0:
        print(f"{a} es multiplo de 5")
    else:
        print(a)


# ==============================
# Ejercicio 8
# Usa un while para contar del 1 al 10.
# Si el número es 4
# usa pass.
# ==============================

a = 0

while a<10:
    a += 1
    if a == 4:
        pass
    else:
        print(a)
    

# ==============================
# Ejercicio 9
# Imprime números del 1 al 20.
# Si el número es 8
# usa continue.
# Si el número es 15
# usa break.
# ==============================

a = 0

while a<20:
    a += 1
    if a == 4:
        continue
    elif a == 15:
        break
    else:
        print(a)
    

# ==============================
# Ejercicio 10
# Pide números al usuario
# hasta que escriba 0.
# Si el número es mayor que 100
# imprime "Numero grande".
# ==============================

a = int(input ("Dame un numero \n"))

while a != 0:
    if a > 100:
        print("Numero Grande\n")
    a = int(input ("De new viejo \n"))   
print("Morimo \n")


# ==========================================================
# BLOQUE
# EJERCICIOS 1 - 10
# BUCLE FOR (ITERACIÓN)
#
# Temas:
# - Bucle for
# - Recorrido de listas
# - Recorrido de strings
# - Función range()
# - Función enumerate()
# ==========================================================


# ==============================
# Ejercicio 1
# Imprime los números del 1 al 10
# usando la función range().
# ==============================

for i in range(1,11):
    print(i)

# ==============================
# Ejercicio 2
# Recorre la lista:
# ["Rojo", "Azul", "Verde"]
# e imprime cada color.
# ==============================

cadena = ["Rojo", "Azul", "Verde"]
for color in cadena:
    print(color)

# ==============================
# Ejercicio 3
# Recorre la palabra "Python"
# e imprime cada letra
# en una línea.
# ==============================

cadena = "Python"
for caracter in cadena:
    print(caracter)

# ==============================
# Ejercicio 4
# Crea una lista de números
# [5, 10, 15, 20]
# e imprime cada número
# multiplicado por 2.
# ==============================

numeros = [5, 10, 15, 20]
for indice,numero in enumerate(numeros):
    numeros[indice] *= 2
print(numeros)

# ==============================
# Ejercicio 5
# Usa range() para imprimir
# los números del 1 al 20.
# ==============================

for i in range(1,21):
    print(i)


# ==============================
# Ejercicio 6
# Recorre la lista:
# ["Ana", "Luis", "Pedro"]
# usando enumerate()
# e imprime:
# Posición X: Nombre
# ==============================

nombres = ["Ana", "Luis", "Pedro"]
for i,nombres in enumerate(nombres):
    print(f"Posicion {i}", nombres)

# ==============================
# Ejercicio 7
# Recorre la palabra "PROGRAMAR"
# e imprime solo las vocales.
# ==============================

palabra = "Pogramar"

for letra in palabra:
    if letra in "aeiou":
        print(letra)


# ==============================
# Ejercicio 8
# Imprime los números
# del 10 al 1 usando range().
# ==============================

for i in range(10,0, -1):
    print(i)

# ==============================
# Ejercicio 9
# Recorre la lista
# [3, 6, 9, 12, 15]
# e imprime cuáles son
# múltiplos de 3.
# ==============================
numeros = [3, 6, 9, 12, 15]

for i in numeros:
    if i % 3 == 0:
        print (i)
# ==============================
# Ejercicio 10
# Pide al usuario una palabra
# e imprime cada letra
# usando un bucle for.
# ==============================

palabra = input("Dame una palabra: \n")

for i in palabra:
    print(i)

# ==========================================================
# BLOQUE
# EJERCICIOS 11 - 20
# BUCLE FOR (ITERACIÓN AVANZADA)
#
# Temas:
# - Bucle for
# - Condicionales (if / elif / else)
# - break / continue / pass
# - range()
# - enumerate()
# - Listas y Strings
# ==========================================================


# ==============================
# Ejercicio 11
# Imprime los números del 1 al 30.
# Si el número es múltiplo de 5
# imprime "Multiplo de 5".
# ==============================

for i in range (1,31):
    if i % 5 == 0:
        print(f"{i} es multiplo de 5")
    else:
        print(i)

# ==============================
# Ejercicio 12
# Recorre la palabra "Programacion".
# Si la letra es vocal
# imprímela.
# ==============================

a = "Programacion"

for letra in a:
    if letra in "aeiou":
        print(letra)

# ==============================
# Ejercicio 13
# Recorre los números del 1 al 20.
# Si el número es par
# imprímelo.
# Si es impar
# usa continue.
# ==============================

for i in range(1,21):
    if i % 2 == 0:
        print(i)
    else:
        continue

# ==============================
# Ejercicio 14
# Recorre la lista:
# [4, 7, 10, 15, 18]
# e imprime solo los números
# mayores que 10.
# ==============================

a = [4, 7, 10, 15, 18]
for i in a:
    if i > 10:
        print(i)
    else:
        continue

# ==============================
# Ejercicio 15
# Pide al usuario una palabra.
# Recorre la palabra
# e imprime cada letra
# junto con su posición usando enumerate().
# ==============================

a = input("Dame una palabra:\n")

for i in enumerate(a):
    print (i)

# ==============================
# Ejercicio 16
# Recorre los números del 1 al 50.
# Si el número es 25
# termina el bucle usando break.
# ==============================

for i in range(1,51):
    if i == 25:
        break
    else:
        print(i)

# ==============================
# Ejercicio 17
# Recorre la lista:
# ["Ana", "Luis", "Pedro", "Maria"]
# e imprime cada nombre
# en mayúsculas.
# ==============================

a = ["Ana", "Luis", "Pedro", "Maria"]

for i in a:
    print(i.upper())

# ==============================
# Ejercicio 18
# Recorre los números del 1 al 20.
# Si el número es divisible
# entre 3 y 5
# imprime "Multiplo de 3 y 5".
# ==============================

for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} es multiplo de 3 o 5")
    else:
        print(i)


# ==============================
# Ejercicio 19
# Recorre la palabra "Python".
# Si la letra es "h"
# usa pass.
# Imprime todas las letras.
# ==============================

a = "Python"

for i in a:
    if i == "h":
        pass
    else:
        print(i)


# ==============================
# Ejercicio 20
# Recorre la lista
# [10, 20, 30, 40, 50]
# usando enumerate()
# e imprime:
# "Indice X -> Valor Y"
# ==============================

a = [10, 20, 30, 40, 50]

for i,a in enumerate(a):
    print (f"Indice {i}  -> Valor {a}")
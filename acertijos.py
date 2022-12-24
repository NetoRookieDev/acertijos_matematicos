def primera(numero):
    # n + (n + 1) = n + (n * (n + 1))
    return numero + (numero * (numero + 1))

# for i in range(1, 5):
#     print(i, " + ", i + 1, " = ", primera(i))

def segunda(numero):
    # n + (n + 3) = (n + (n * (n + 3)))
    return numero + (numero * (numero + 3))

# for i in range(1, 9):
#     if (i > 3) and (i < 8):
#         continue
#     print(i, " + ", i+3, " = ", segunda(i))

def tercera(a, b):
    # a + b = "a * b" + "a + b" + "a - b"
    return str(a * b) + str(a + b) + str(a - b)

def imprimir_tercera(a, b):
    print(a, " + ", b, " = ", tercera(a, b))

# imprimir_tercera(8, 2)
# imprimir_tercera(5, 4)
# imprimir_tercera(9, 6)
# imprimir_tercera(7, 5)
# imprimir_tercera(20, 3)

def cuarta(a, b):
    # a + b = "a + b" + "a - b"
    return str(a + b) + str(a - b)

def imprimir_cuarta(a, b):
    print(a, " + ", b, " = ", cuarta(a, b))

# imprimir_cuarta(6, 2)
# imprimir_cuarta(8, 1)
# imprimir_cuarta(1, 1)
# imprimir_cuarta(5, 3)
# imprimir_cuarta(7, 2)

def quinta(a, b):
    # a + b = "a - b" + "a + b"
    return str(a - b) + str(a + b)

def imprimir_quinta(a, b):
    print(a, " + ", b, " = ", quinta(a, b))

# imprimir_quinta(4, 2)
# imprimir_quinta(8, 1)
# imprimir_quinta(6, 5)
# imprimir_quinta(7, 3)

def sexta(a, b, c):
    # a, b, c = a * c - b
    return a * c - b

def imprimir_sexta(a, b, c):
    print(a, ", ", b, ", ", c, " = ", sexta(a, b, c))

# imprimir_sexta(3, 2, 4)
# imprimir_sexta(4, 3, 5)
# imprimir_sexta(5, 4, 6)
# imprimir_sexta(6, 5, 7)
# imprimir_sexta(7, 6, 8)

def sexta(numero):
    # n, n -1, n +2 = (n * (n + 1)) - (n - 1)
    return (numero * (numero + 1)) - (numero -1)

for i in range(3, 8):
    print(i, ", ", i - 1, ", ", i + 1, " = ", sexta(i))
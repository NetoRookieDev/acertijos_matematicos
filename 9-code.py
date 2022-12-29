# 2  =  6
# 3  =  12
# 4  =  20
# 5  =  30
# 6  =  42
# 9  =  ??

resultado = 0
for i in range(2, 10):
    if (i > 6) and (i < 9):
        continue
    numero = i
    resultado = i * (i + 1)
    print(numero, " = ", resultado)

# 2  =  6
# 3  =  12
# 4  =  20
# 5  =  30
# 6  =  42
# 9  =  90
# 1  +  4  =  5 
# 2  +  5  =  12
# 3  +  6  =  21
# 8  +  11  =  ??

resultado = 0
for i in range(1, 9):
    if (i > 3) and (i < 8):
        continue
    primero = i
    segundo = i + 3
    resultado = resultado + i + (i + 3)
    print(primero, " + ", segundo, " = ", resultado)

# 1  +  4  =  5 
# 2  +  5  =  12
# 3  +  6  =  21
# 8  +  11  =  40
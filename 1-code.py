# 1  +  2  =  3
# 2  +  3  =  8
# 3  +  4  =  15
# 4  +  5  =  ??

resultado = 0
for i in range(1, 5):
    primero = i
    segundo = i + 1
    resultado = resultado + i + (i + 1)
    print(primero, " + ", segundo, " = ", resultado)

# 1  +  2  =  3
# 2  +  3  =  8
# 3  +  4  =  15
# 4  +  5  =  24
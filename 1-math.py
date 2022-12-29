# 1  +  2  =  3
# 2  +  3  =  8
# 3  +  4  =  15
# 4  +  5  =  ??

def get_resultado(numero):
    return numero + (numero * (numero + 1))

for i in range(1, 5):
    primero = i
    segundo = i + 1
    resultado = get_resultado(i)
    print(primero, " + ", segundo, " = ", resultado)

# 1  +  2  =  3
# 2  +  3  =  8
# 3  +  4  =  15
# 4  +  5  =  24
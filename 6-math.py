# 3 ,  2 ,  4  =  10
# 4 ,  3 ,  5  =  17
# 5 ,  4 ,  6  =  26
# 6 ,  5 ,  7  =  37
# 7 ,  6 ,  8  =  ??

def get_resultado(numero):
    return (numero * (numero + 1)) - (numero -1)

for i in range(3, 8):
    primero = i
    segundo = i - 1
    tercero = i + 1
    resultado = get_resultado(i)
    print(primero, ", ", segundo, ", ", tercero, " = ", resultado)

# 3 ,  2 ,  4  =  10
# 4 ,  3 ,  5  =  17
# 5 ,  4 ,  6  =  26
# 6 ,  5 ,  7  =  37
# 7 ,  6 ,  8  =  50
# 2  =  6
# 3  =  12
# 4  =  20
# 5  =  30
# 6  =  42
# 9  =  ??

def get_novena(numero):
    return numero * (numero + 1)

for i in range(2, 10):
    if (i > 6) and (i < 9):
        continue
    print(i, " = ", get_novena(i))

# 2  =  6
# 3  =  12
# 4  =  20
# 5  =  30
# 6  =  42
# 9  =  90
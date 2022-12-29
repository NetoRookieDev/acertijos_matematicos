# 1  =  11
# 2  =  22
# 3  =  33
# 4  =  44
# 5  =  55
# 6  =  66
# 11  =  ??

def get_septima(numero):
    return numero * 11

for i in range(1, 12):
    if (i > 6) and (i < 11):
        continue
    numero = i
    resultado = get_septima(i)
    print(numero, " = ", resultado)

# 1  =  11
# 2  =  22
# 3  =  33
# 4  =  44
# 5  =  55
# 6  =  66
# 11  =  121
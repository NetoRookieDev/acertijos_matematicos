# 3  *  2  =  10
# 4  *  3  =  21
# 5  *  4  =  36
# 6  *  5  =  55
# 7  *  6  =  ??

def get_decima(numero):
    return (numero + (numero - 1)) * (numero - 1)

for i in range(3, 8):
    print(i, " * ", i - 1, " = ", get_decima(i))

# 3  *  2  =  10
# 4  *  3  =  21
# 5  *  4  =  36
# 6  *  5  =  55
# 7  *  6  =  78
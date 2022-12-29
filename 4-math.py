# 6  +  2  =  84
# 8  +  1  =  97
# 1  +  1  =  20
# 5  +  3  =  82
# 7  +  2  =  ??

def get_resultado(a, b):
    return str(a + b) + str(a - b)

def print_resultado(a, b):
    print(a, " + ", b, " = ", get_resultado(a, b))

print_resultado(6, 2)
print_resultado(8, 1)
print_resultado(1, 1)
print_resultado(5, 3)
print_resultado(7, 2)

# 6  +  2  =  84
# 8  +  1  =  97
# 1  +  1  =  20
# 5  +  3  =  82
# 7  +  2  =  95